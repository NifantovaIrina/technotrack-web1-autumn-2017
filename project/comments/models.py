from django.db import models

# Create your models here.
from django.conf import settings

from posts.models import Post


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post)