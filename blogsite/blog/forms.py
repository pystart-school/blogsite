from django import forms
from .models import Post
from django.contrib.auth.models import User
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add email field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Include email in the fields

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