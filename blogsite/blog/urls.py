from django.urls import path
from . import views
from .views import CustomPasswordChangeDoneView, CustomPasswordChangeView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('post/delete/<int:pk>/', views.post_delete, name='post_delete'),

    path('login/', views.user_login, name='user_login'),  # Custom login view
    path('logout/', views.user_logout, name='user_logout'),  # Custom logout view
    path('register/', views.user_register, name='register'),

    path('change_email/', views.user_change_email, name='change_email'),

    path('change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('password-change-done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    

    # Password Reset Views
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='blog/password_reset_form.html'
    ), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='blog/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='blog/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='blog/password_reset_complete.html'
    ), name='password_reset_complete'),
]