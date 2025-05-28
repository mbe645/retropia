from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.game_list, name='games-home'),
    path('<int:game_id>/', views.game_detail, name='game-detail'),
]
