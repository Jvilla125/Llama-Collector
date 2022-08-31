from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Llama # Llama class 
from .forms import FeedingForm

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<center><h1>Hello World</center></h1>')

def about(request):
    return render(request, 'about.html')

def llamas_index(request):
    llamas = Llama.objects.all()
    return render(request, 'llamas/index.html', {'llamas': llamas})

def llamas_detail(request, llama_id):
    llama = Llama.objects.get(id=llama_id)
    feeding_form = FeedingForm()
    return render(request, 'llamas/detail.html', {
        'llama': llama, 'feeding_form': feeding_form
    })

class LlamaCreate(CreateView):
    model = Llama 
    fields = '__all__' # or it can be listed as fields = ['name', 'breed', 'description']
    success_url = '/llamas/'

class LlamaUpdate(UpdateView):
    model = Llama
    fields = ['breed', 'description']

class LlamaDelete(DeleteView):
    model = Llama
    success_url = '/llamas/'

def add_feeding(request, llama_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.llama_id = llama_id
        new_feeding.save()
    return redirect('detail', llama_id=llama_id)
