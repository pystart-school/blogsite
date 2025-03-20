from django import forms
from .models import Post
from django.contrib.auth.models import User
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class EmailChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']