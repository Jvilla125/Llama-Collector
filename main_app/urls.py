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
    path('llamas/<int:llama_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    # adding new routes for toys below
    path('llamas/<int:llama_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    # creating a toys view page (create an html and add to views.py)
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    # Creating a toys detail page using their primary key as their id
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    # Creating a create toys page 
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    # Create an update and delete page
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]

