from django.contrib import admin
from django.urls import path 
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
urlpatterns = [
    
    path('',PostListView.as_view(template_name='blog/home.html'),name="Blog-home"),
    path('post/new/',PostCreateView.as_view(template_name='blog/postcreate.html'),name="Blog-post_create"),
    path('post/<int:pk>/update',PostUpdateView.as_view(template_name='blog/post_update.html'),name="Blog-post_update"),
    path('post/<int:pk>/delete',PostDeleteView.as_view(template_name='blog/post_delete.html'),name="Blog-post_delete"),
    path('post/<int:pk>/',PostDetailView.as_view(template_name='blog/post_detail.html'),name="Blog-post_detail"),
    path('about/',views.about,name="Blog-about")
]
