from django.contrib import admin
from users.models import Profile, Role

# Register your users/models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'bio', 'user_role')
    list_filter = ('user',)
    actions = ['delete_selected']


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'description')
    actions = ['delete_selected']
