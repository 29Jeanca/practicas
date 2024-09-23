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

# def owner_index(request):
#     owners = Owner.objects.all()
#     if not owners:
#         print("No owners found in the database.")
#     return render(request, 'pets/allOwners.html', {'owners': owners})
def owner_index():
    owners = Owner.objects.all().values()  
    return JsonResponse(list(owners), safe=False)  

def owner_show(id):
    # Buscamos el owner por el ID proporcionado en la URL
    owner = Owner.objects.get(pk=id)
        
    # Retornamos el owner en formato JSON usando el método to_dict() que debes haber definido
    return JsonResponse(owner.to_dict(), safe=False)

#    def owner_show(request, id):
#     # Buscamos el owner por el ID proporcionado en la URL
#     owner = Owner.objects.get(pk=id)
        
#     # Retornamos el owner en formato JSON usando el método to_dict() que debes haber definido
#     return render(request, 'pets/OneOwner.html', {'owner': owner})
