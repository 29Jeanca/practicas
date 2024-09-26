from django.urls import path
from .views import AllProductsView
urlpatterns = [
    path('products/', AllProductsView.as_view(), name='all_products'), # CARGA DE DATOS
]