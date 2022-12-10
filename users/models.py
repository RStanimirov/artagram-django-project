from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from utils.size_validator import validate_max_size

# Create your users/models here.


class Role(models.Model):
    role_name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.role_name


class Profile(models.Model):
    """RS: we are extending the Default User model of Django to have One-to-One Relationship
    with our Profile Model i.e. one user can have one profile and one profile can be linked to only one user."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default-user.png', upload_to='profile_pics', validators=(validate_max_size,))
    bio = models.CharField(max_length=255, blank=True)
    user_role = models.ForeignKey(Role, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # RS: in order to resize the uploaded images, we will override the save method of the Profile model.
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_max_size = (300, 300)
            img.thumbnail(output_max_size)
            img.save(self.image.path)
