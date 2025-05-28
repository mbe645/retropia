from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('', views.comment_list, name='comments-home'),
    path('add/', views.add_comment, name='add-comment'),
]
