from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog-home'),
    path('create/', views.create_blogpost, name='create-blogpost'),
    path('edit/<int:pk>/', views.edit_blogpost, name='edit-blogpost'),
    path('<int:pk>/', views.blog_detail, name='blog-detail'),
]
