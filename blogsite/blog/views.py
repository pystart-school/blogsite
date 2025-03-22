from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.http import HttpResponseForbidden
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import EmailChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm  # Import the custom form

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()  # Fetch all comments related to the post

    if request.method == 'POST':
        if request.user.is_authenticated:  # Ensure the user is logged in to comment
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('post_detail', pk=post.pk)  # Redirect after comment submission
        else:
            return redirect('user_login')  # Redirect to login if the user is not authenticated
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Check if the user is the author of the post
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    # If the request method is POST, delete the post
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    # Otherwise, render the confirmation page
    return render(request, 'blog/post_delete.html', {'post': post})



# Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Handle redirect manually
                next_url = request.GET.get('next') or settings.LOGIN_REDIRECT_URL
                return redirect(next_url)
    else:
        form = AuthenticationForm()

    return render(request, 'blog/login.html', {'form': form})

# Logout view
def user_logout(request):
    logout(request)
    return redirect('post_list')  # Redirect to post list after logout


def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')  # Redirect to login after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


@login_required
def user_change_email(request):
    if request.method == 'POST':
        form = EmailChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Or wherever you want
    else:
        form = EmailChangeForm(instance=request.user)
    return render(request, 'blog/change_email.html', {'form': form})


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'blog/change_password.html'
    success_url = reverse_lazy('password_change_done')


class CustomPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'blog/password_change_done.html'
    success_url = reverse_lazy('home')