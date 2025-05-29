from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.page_list, name='pages-home'),
    path('<slug:slug>/', views.page_detail, name='page-detail'),
]
