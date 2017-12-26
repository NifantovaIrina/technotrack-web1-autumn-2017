from django import forms

from comments.models import Comment
from posts.models import Post


class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


