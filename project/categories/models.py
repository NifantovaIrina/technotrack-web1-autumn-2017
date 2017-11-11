from django.db import models
from posts.models import Post


class Category(models.Model):
    name = models.CharField(max_length=300)
    posts = models.ManyToManyField(Post, blank=True)
