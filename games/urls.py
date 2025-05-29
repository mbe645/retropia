from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.game_list, name='games-home'),
    path('<int:pk>/', views.game_detail, name='game-detail'),
    path('add/', views.add_game, name='add-game'),
]
