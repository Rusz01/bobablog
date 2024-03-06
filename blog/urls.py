from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
   path('', views.home, name='home'),
   path('blog', views.blog, name='blog'),
   path('blogpost/<str:slug>', views.blogpost, name='blog'),
   path('contact', views.contact, name='contact'),
]
