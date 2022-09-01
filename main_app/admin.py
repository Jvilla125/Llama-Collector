from django.contrib import admin

from .models import Llama, Feeding, Toy
# Register your models here.
admin.site.register(Llama)
admin.site.register(Feeding)
admin.site.register(Toy)