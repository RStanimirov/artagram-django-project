from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from users.models import Profile


class UserRegisterForm(UserCreationForm):
    """RS: we shall use this UserRegistrationForm which inherits from the built-in UserCreationForm
    in order to add some custom features, such as the 1) desired form fields, 2) validation for unique username
    and validation for unique email."""

    email = forms.EmailField()

    class Meta:
        model = User  # RS: whenever this form validates, it will create a new user.
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
            raise ValidationError("This username or email already exists. Please use a unique username and email.")
        return self.cleaned_data


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']
