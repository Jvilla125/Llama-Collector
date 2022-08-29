from django.db import models

# Create your models here.
class Llama(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    
    
    
    
# class Llama:
#     def __init__(self, name, breed, description):
#         self.name = name
#         self.breed = breed
#         self.description = description

# llamas = [
#     Llama('Carl', 'Classic Llama', 'Classic llamas have double-coated fleece and are much larger than other llamas.'),
#     Llama('Spence', 'Wooly Llama', 'Wooly llamas are smaller than other llamas and have strong wool covering their body.'),
#     Llama('Ken', 'Vicuna Llama', 'Vicuna Llamas coats are orange colored and have rare and valuable wool.')
# ]
