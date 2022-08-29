from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('llamas/', views.llamas_index, name='index'),
    path('llamas/<int:llama_id>/', views.llamas_detail, name='detail'),
]

