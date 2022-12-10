from django.contrib import admin
from mail.models import Contact

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'message')
    actions = ['delete_selected']


