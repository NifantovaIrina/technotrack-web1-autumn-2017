from django.db import models
from application import settings
from posts.models import Post


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
