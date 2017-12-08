from django import forms

from comments.models import Comment


class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
