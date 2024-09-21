from django.http import JsonResponse
from django.shortcuts import render

from pets.models import Owner

# Create your views here.
def index(request):
    # Aquí puedes agregar la lógica necesaria para la vista principal
    return render(request, 'pets/index.html')

def about(request):
    # Aquí puedes agregar la lógica necesaria para la vista 'about'
    return render(request, 'pets/about.html')

def owner_index(request):
    owners = Owner.objects.all().values()  # Obtenemos todos los owners en la base de datos
    return JsonResponse(list(owners), safe=False) 