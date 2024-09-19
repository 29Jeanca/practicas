from django.utils import timezone
from django.db import models
from django.dispatch import receiver
from django.forms import ValidationError


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
            raise ValidationError('Ingrese un nombre. EL NOMBRE NO PUEDE ESTAR VACÍO')
        
        if not self.email:
            raise ValidationError('Ingrese un email. EL EMAIL NO PUEDE ESTAR VACÍO')
        
        if not self.age:
            raise ValidationError('Ingrese una edad. LA EDAD NO PUEDE ESTAR VACÍA')
    
    # Método para contar las mascotas
    def pets_adopted_count(self):
        return self.pets.count()  #hacer un count es lo que es hacer un lenght en javaScript
    
    # Método para listar las mascotas
    def pets_names(self):
        return ', '.join([pet.name for pet in self.pets.all()])
 
    def __str__(self):
        return self.name
    
class AnimalManager(models.Manager):
    def dogs_only(self):
        return self.filter(species='dog')
    
    def cats_only(self):
        return self.filter(species='cat')

class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    color = models.CharField(max_length=100)
    weight = models.FloatField()
    species = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AnimalManager()
    
    # Validaciones de vacíos
    def clean(self):
        if not self.age:
            raise ValidationError('Ingrese una edad. LA EDAD NO PUEDE ESTAR VACÍA')
        
        if not self.color:
            raise ValidationError('Ingrese un color. EL COLOR NO PUEDE ESTAR VACÍO')
        
        if not self.weight:
            raise ValidationError('Ingrese un peso. EL PESO NO PUEDE ESTAR VACÍO')
        
        if not self.species:
            raise ValidationError('Ingrese una especie. LA ESPECIE NO PUEDE ESTAR VACÍA')

    def __str__(self) -> str:
        return self.species
    
class PetManager(models.Manager):
    def older_than_five(self):
        return self.filter(age__gt=5)

class Pet(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE,related_name='pets')
    animal = models.ForeignKey(Animal,on_delete=models.CASCADE,related_name='pets')
    adoption_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PetManager()

    # Validaciones de vacíos
    def clean(self):
        if not self.name:
            raise ValidationError('Ingrese un nombre. EL NOMBRE NO PUEDE ESTAR VACÍO')
        
    #Método para calcular los días desde que fue adoptado	   
    def days_since_adopted(self):
        dias_adopcion = timezone.now() - self.adoption_date
        return dias_adopcion.days
    
    def __str__(self) -> str:
        return self.name 

    # Signal para asignar la fecha de adopción automáticamente
  
    
