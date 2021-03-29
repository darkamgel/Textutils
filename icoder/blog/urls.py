from django.contrib import admin
from django.urls import path, include
from . import views
import slugify

urlpatterns = [
    path('', views.blogHome, name="bloghome"),
    #API to post comment
    path('postComment',views.postComment,name="postComment"),
    path('<str:slug>', views.blogPost, name="blogPost"),
    
]
