from django.urls import path
from . import views

app_name = 'cards'

urlpatterns = [
    path('', views.index, name='cards-home'),  
    path('detail/<int:pk>/', views.card_detail, name='card-detail'),
    path('add/', views.add_card, name='add-card'),
]
