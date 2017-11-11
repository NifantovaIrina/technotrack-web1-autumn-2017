from django.db import models

# Create your models here.
from django.conf import settings

class Blog(models.Model):
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    description = models.TextField()
    title = models.CharField(max_length=300)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)