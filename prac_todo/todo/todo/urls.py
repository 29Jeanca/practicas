from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include('todos.urls'))
]

# Llamamos la url que se creo en la app, para mostrarlo en el proyecto
