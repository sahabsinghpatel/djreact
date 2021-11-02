from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
    path('post-comment/', views.post_comment, name='post-comment'),
    path('<str:slug>/', views.blog_post, name='blog_post'),
]
