from django.urls import path
from blog.views import like_post
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, search_posts

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post_like/<int:pk>', like_post, name='post-like'),
    path('posts/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('posts_search/', search_posts, name='search-posts'),
]



