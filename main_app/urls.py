from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('llamas/', views.llamas_index, name='index'),
    path('llamas/<int:llama_id>/', views.llamas_detail, name='detail'),
    # the new route used to show a form and create a llama
    path('llamas/create/', views.LlamaCreate.as_view(), name='llamas_create'),
    path('llamas/<int:pk>/update/',  views.LlamaUpdate.as_view(), name='llamas_update'),
    path('llamas/<int:pk>/delete/', views.LlamaDelete.as_view(), name='llamas_delete'),
]

