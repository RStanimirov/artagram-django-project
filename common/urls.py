from django.urls import path
from common.views import index, about, statistics, django_facts, about_author, user_rank_system, announcements


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about-website'),
    path('about-the-author/', about_author, name='about-author'),
    path('announcements', announcements, name='announcements'),
    path('django-facts/', django_facts, name='django-facts'),
    path('stats', statistics, name='blog-stats'),
    path('rank-system/', user_rank_system, name='rank-system'),
]
