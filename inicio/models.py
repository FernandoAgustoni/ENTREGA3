from django.db import models

# Create your models here.
class Celular (models.Model):
    modelo= models.CharField (max_length=20)
    marca= models.CharField (max_length=20)
    
    def __str__(self):
       return f"Soy el celular {self.modelo} {self.marca}"
    
        
    