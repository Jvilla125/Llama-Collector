from django.shortcuts import render
from .models import Llama

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<center><h1>Hello World</center></h1>')

def about(request):
    return render(request, 'about.html')

def llamas_index(request):
    llamas = Llama.objects.all()
    return render(request, 'llamas/index.html', {'llamas': llamas})