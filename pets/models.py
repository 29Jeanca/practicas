from django.db import models

# Create your models here.
class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal,on_delete=models.CASCADE)
    adoption_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name 

    
