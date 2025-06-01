from django.urls import path
from . import views

app_name = 'favorites'

urlpatterns = [
    path('', views.favorite_list, name='favorites-home'),
    path('toggle/<int:card_id>/', views.toggle_favorite, name='toggle-favorite'),
    path('toggle/game/<int:game_id>/', views.toggle_favorite_game, name='toggle-favorite-game'),
    path('toggle/blog/<int:blog_id>/', views.toggle_favorite_blog, name='toggle-favorite-blog'),
    path('games/', views.favorite_games_list, name='favorites-games'),
    path('blogs/', views.favorite_blogs_list, name='favorites-blogs'),
]
