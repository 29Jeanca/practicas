from django.contrib import admin
from django.urls import path
from pets import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('owners/', views.owner_index, name='owner_index')
    
]
