from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Llama, Toy  # Llama and Toy class 
from .forms import FeedingForm

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def llamas_index(request):
    llamas = Llama.objects.all()
    return render(request, 'llamas/index.html', {'llamas': llamas})

def llamas_detail(request, llama_id):
    llama = Llama.objects.get(id=llama_id)
    toys_llama_doesnt_have = Toy.objects.exclude(id__in = llama.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'llamas/detail.html', {
        'llama': llama, 'feeding_form': feeding_form, 'toys': toys_llama_doesnt_have
    })

# associating a toy to a Llama
def assoc_toy(request, llama_id, toy_id):
    Llama.objects.get(id=llama_id).toys.add(toy_id)
    return redirect('detail', llama_id=llama_id)

class LlamaCreate(CreateView):
    model = Llama 
    fields = ['name', 'breed', 'description'] # or it can be listed as fields = 
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

# function for toy_index (Toy list)
class ToyList(ListView):
    model = Toy

# funtcion for toy_details
class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy 
    success_url = '/toys/'