from django.shortcuts import get_object_or_404
from users.models import User
from blog.models import Post


def validate_rank(username):
    """RS: this helper function calculates the rank of the user, depending on how many posts they have posted.
    Valid Artagram ranks are: Apprentice, Artisan, Craftsman, Master."""
    current_user = get_object_or_404(User, username=username)
    all_user_posts = Post.objects.all().filter(author=current_user)
    total_user_posts = all_user_posts.count()

    if total_user_posts < 4:
        user_rank = 'Apprentice'
        rank_image = '/static/blog/icons/rank-1.png'
    elif 4 <= total_user_posts < 8:
        user_rank = 'Artisan'
        rank_image = '/static/blog/icons/rank-2.png'
    elif 8 <= total_user_posts < 16:
        user_rank = "Craftsman"
        rank_image = '/static/blog/icons/rank-3.png'
    else:
        user_rank = "Master"
        rank_image = '/static/blog/icons/rank-4.png'
    return user_rank, rank_image


def validate_total_posts(username):
    current_user = get_object_or_404(User, username=username)
    all_user_posts = Post.objects.all().filter(author=current_user)
    total_user_posts = all_user_posts.count()
    return total_user_posts
