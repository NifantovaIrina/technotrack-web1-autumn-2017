from django import forms
from django.urls import reverse_lazy, reverse

from posts.models import Post


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'categories', )
