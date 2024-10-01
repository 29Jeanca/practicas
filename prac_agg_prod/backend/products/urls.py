from django.urls import path
from .views import   AllProductsView
urlpatterns = [
    path('products/', AllProductsView.as_view(), name='all_products'), 
    #  path('products/add/', AddProduct.as_view(), name='add_product'), # CARGA DE DATOS

]