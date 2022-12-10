from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from users.models import User
from utils.helper_functions import validate_rank, validate_total_posts

# Create your users/views here.


def register(request):
    if request.method == 'GET':
        form = UserRegisterForm()
    else:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Now you can login.')
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context=context)


class Login(LoginView):
    """RS: we inherit the built-in LoginView which will handle the logic. Below we are customising the messages
    it flashes when the users are trying to login with wrong credentials."""

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Welcome {self.request.user}. Now you are logged in.')
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.warning(self.request, f'You may be trying to log in without a valid account. '
                                       f'Please click on the Register button to register your account. '
                                       f'If you have an account, but it is inactive, please contact the site admin.')
        return response


class Logout(LogoutView):
    """RS: we inherit the built-in LogoutView which can be further customised if needed."""


@login_required()
def profile(request):
    """RS: view and update the user profile by means of creating two forms --> u_form and p_form.
    Important notice: include the enctype in the html form info --> enctype='multipart/form-data'"""

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    username = request.user.username
    user_rank = validate_rank(username)[0]
    rank_image = validate_rank(username)[1]
    total_posts = validate_total_posts(username)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user_rank': user_rank,
        'total_posts': total_posts,
        'rank_image': rank_image
    }
    return render(request, 'users/profile.html', context=context)


@login_required()
def user_profile(request, username):
    """RS: this view handles two functionalities:
        1) if the user is authenticated (logged-in), they can view another user's profile; if the requested
        username is not existing in the database, an exception will be raised.
        2) we are rendering here the ranking system of Artagram with our custom validate_rank helper function."""

    requested_user = get_object_or_404(User, username=username)
    username = requested_user.username
    user_rank = validate_rank(username)[0]
    rank_image = validate_rank(username)[1]
    total_user_posts = validate_total_posts(username)

    context = {
        'requested_user': requested_user,
        'user_rank': user_rank,
        'total_user_posts': total_user_posts,
        'rank_image': rank_image
    }
    return render(request, 'users/user_profile.html', context=context)



