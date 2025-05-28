from django.urls import path
from . import views

app_name = 'favorites'

urlpatterns = [
    path('', views.favorite_list, name='favorites-home'),
    path('toggle/<int:card_id>/', views.toggle_favorite, name='toggle-favorite'),
]
