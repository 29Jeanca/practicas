from django.contrib import admin
from django.urls import path
from pets.views import AnimalCreateView, animal_list
from pets import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('owners/', views.owner_index, name='owner_index'),
    path('owners/<int:id>/', views.owner_show, name='owner_show'),
    path('create/', AnimalCreateView.as_view(), name='create_animal'),
    path('animals/', animal_list, name='list_animals'),
]

    
