from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer


class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# Importamos del rest_framework el viewsets para usar los metedos como el GET, POST, PUT, DELETE

# Usamos el modelo al que le vamos a aplicar la logica

# Usamos el serializador para agrupar la información


# La clase, tiene la heredacion de ModelViewSet para usar los metodos de la API

# Usamos la consulta para traer todos los datos que esten guardados en la BD

# Por ultimo usamos el serializador para mostrar la información en la API