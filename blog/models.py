from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from utils.size_validator import validate_max_size

# Create your blog/models here.


class Post(models.Model):
    """RS: below 'author' foreign key manages a One-to-Many Relationship --> one author can have multiple posts,
    but a post can have only one author; if the author is deleted, then the post will also be deleted.
    Further down, 'likes' is a Many-to-Many Relationship with the User model:
     --> users will have multiple likes, and blog posts can have multiple likes."""

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=600)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    artwork = models.ImageField(default='default-artwork.png', upload_to='artworks', validators=(validate_max_size,))
    likes = models.ManyToManyField(User, related_name='p_likes')

    def __str__(self):
        return self.title

    @property
    def number_of_comments(self):
        return Comments.objects.filter(post_commented=self).count()

    def number_of_likes(self):
        return self.likes.count()

    # RS: we may need to resize the uploaded images by overriding the save method of the Post model.
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.artwork.path)
        if img.width > 600:
            output_max_size = (600, 600)
            img.thumbnail(output_max_size)
            img.save(self.artwork.path)
        elif img.width < 600:
            output_min_size = (600, 600)
            img.thumbnail(output_min_size)
            img.save(self.artwork.path)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comments(models.Model):
    """RS: the Comments model links a comment with the post and the user."""

    post_commented = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user_who_commented = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=255)
    comment_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Comments'


