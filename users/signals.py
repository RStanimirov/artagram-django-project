"""
RS: create a signal in this module so that every time a user is registered,
a profile is attached to them. The built-in User will be the 'sender' and the 'receiver' will be a decorator
assigned to functions which will create the profile and then save it.
--> add the def ready(self) method in users/apps.py
"""

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from users.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

