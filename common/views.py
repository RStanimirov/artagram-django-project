from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog.models import Post, Comments
from utils.calculate_db_time import calculate_db_response_time

# Create your common/views here.


def index(request):
    context = {'title': 'Index', }
    return render(request, 'common/index.html', context=context)


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'common/about.html', context=context)


def about_author(request):
    return render(request, 'common/about-author.html')


@login_required()
def statistics(request):
    # RS: in order to reduce the database queries we can prefetch related data by below query:
    all_posts = Post.objects.all().select_related('author').count()
    all_authors = User.objects.all().count()
    all_comments = Comments.objects.all().count()
    context = {
        'all_posts': all_posts,
        'all_authors': all_authors,
        'all_comments': all_comments,
    }
    calculate_db_response_time()
    return render(request, 'common/statistics.html', context=context)


@login_required()
def announcements(request):
    return render(request, 'common/announcements.html')


def django_facts(request):
    return render(request, 'common/django_facts.html')


def user_rank_system(request):
    return render(request, 'common/user-rank-system.html')


