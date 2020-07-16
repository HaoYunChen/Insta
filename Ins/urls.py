"""Insta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Ins.views import Helo, PostDetailView, PostsView, PostCreateView, PostUpdateView, PostDeleteView, addLike, UserDetailView, addComment, follow, ProfileUpdateView

urlpatterns = [
    path('helo', Helo.as_view(), name = 'helo'),
    path('', PostsView.as_view(), name = 'posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'), #<int:pk> i gave u an integer as a primary key
    path('post/new', PostCreateView.as_view(), name = 'post_create'),
    path('posts/update/<int:pk>', PostUpdateView.as_view(), name = 'post_update'),
    path('posts/delete/<int:pk>', PostDeleteView.as_view(), name = 'post_delete'),
    path('like', addLike, name='addLike'),
    path('user/<int:pk>/', UserDetailView.as_view(), name = 'user_detail'),
    path('comment', addComment, name='addComment'),
    path('togglefollow', follow, name='togglefollow'),
    path('user/update/<int:pk>', ProfileUpdateView.as_view(), name = 'profile_update'),
]
