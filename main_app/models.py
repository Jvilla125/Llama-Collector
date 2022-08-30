from django.db import models
from django.urls import reverse

# Create your models here.
class Llama(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('detail', kwargs={'llama_id': self.id})
