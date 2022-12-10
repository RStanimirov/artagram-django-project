from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.http import HttpResponseRedirect
from django.urls import reverse
from blog.models import Post, Comments
from blog.forms import NewCommentForm

#  create your blog/views here:


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    # RS: below we are getting the user from url.
    # -- if the user exists, he will be returned into the user variable;
    # -- if the user does not exist, will result in 404.
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        """RS: Here we retrieve all the comments from our current Post object,
        store them (the query) in a local variable comments_related, then send it further as a context
        to our post_detail template.
        Also, we retrieve the current post primary key, and check if the currently logged-in user
        has liked or not this post."""

        data = super().get_context_data(**kwargs)

        comments_related = Comments.objects.filter(post_commented=self.get_object()).order_by('-comment_date')
        data['comments'] = comments_related
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance=self.request.user)

        likes_related = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_related.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_related.number_of_likes()
        data['post_is_liked'] = liked
        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comments(comment_content=request.POST.get('comment_content'),
                               user_who_commented=self.request.user,
                               post_commented=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'artwork', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'artwork', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # RS: below method tests if the current user is the author by means of the UserPassesTesMixin.
    # --> user will not be able to update other user's posts.
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def like_post(request, pk):
    """RS: 'post_id' will be our button identification in our template post_detail.html.
    Every time a logged-in user clicks the Like button, we will retrieve his id
    and then will check if that user already liked or not the current blogpost. """

    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


@login_required()
def search_posts(request):
    query = request.GET.get('p')
    object_list = Post.objects.filter(content__icontains=query)
    context = {
        'posts': object_list,
    }
    return render(request, "blog/search_posts.html", context=context)
