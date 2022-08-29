from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Llama:
    def __init__(self, name, breed, description):
        self.name = name
        self.breed = breed
        self.description = description

llamas = [
    Llama('Carl', 'Classic Llama', 'Classic llamas have double-coated fleece and are much larger than other llamas.'),
    Llama('Spence', 'Wooly Llama', 'Wooly llamas are smaller than other llamas and have strong wool covering their body.'),
    Llama('Ken', 'Vicuna Llama', 'Vicuna Llamas coats are orange colored and have rare and valuable wool.')
]

def home(request):
    return HttpResponse('<center><h1>Hello World</center></h1>')

def about(request):
    return render(request, 'about.html')

def llamas_index(request):
    return render(request, 'llamas/index.html', {'llamas': llamas})