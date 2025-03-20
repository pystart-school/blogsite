from django.urls import path
from . import views

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
]