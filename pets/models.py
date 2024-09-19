from django.db import models
from django.forms import ValidationError

# Create your models here.
class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Validaciones de vacíos
    def clean(self):    
        if not self.name:
            return ValidationError('Ingrese un nombre. EL NOMBRE NO PUEDE ESTAR VACÍO')
        
        if not self.email:
            return ValidationError('Ingrese un email. EL EMAIL NO PUEDE ESTAR VACÍO')
        
        if not self.age:
            return ValidationError('Ingrese una edad. LA EDAD NO PUEDE ESTAR VACÍA')
    
    # Método para contar las mascotas
    def pets_adopted_count(self):
        return self.pets.count()  #hacer un count es lo que es hacer un lenght en javaScript
    
    # Método para listar las mascotas
    def pets_names(self):
        return ', '.join([pet.name for pet in self.pets.all()])
 
    def __str__(self):
        return self.name
    
class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    color = models.CharField(max_length=100)
    weight = models.FloatField()
    species = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.age
    
class Pet(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE,related_name='pets')
    animal = models.ForeignKey(Animal,on_delete=models.CASCADE)
    adoption_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name 

    
