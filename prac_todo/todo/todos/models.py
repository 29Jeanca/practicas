from django.db import models

# Create your models here.
class Todo(models.Model):
    titulo = models.CharField(max_length=200)
    estado = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.titulo
    
# Creamos el modelo con la estructura de la tabla de la BD 