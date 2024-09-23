# el rest frame work convierte la url de la view en una api accesible.
from rest_framework.routers import DefaultRouter
from .views import TodoView

router = DefaultRouter() # Creamos una ruta por defecto

router.register(r'todos',TodoView,basename='todo')

urlpatterns = router.urls # Usamos la ruta por defecto para mostrar las urls

# el router .register ejecuta un url con la app, luego usa la vista que tiene la logica, y se le asigna un nombre