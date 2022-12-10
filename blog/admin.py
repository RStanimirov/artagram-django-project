from django.contrib import admin
from .models import Post, Comments
admin.site.disable_action('delete_selected')

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'date_posted')
    list_filter = ('date_posted',)
    search_fields = ('content__icontains',)


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('post_commented', 'user_who_commented', 'comment_content')
    actions = ['delete_selected']


