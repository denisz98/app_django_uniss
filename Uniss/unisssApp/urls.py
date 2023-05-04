from django.urls import path
from unisssApp import views
urlpatterns = [
    path('clase/', views.clase, name="Clase"),
    path('insertar_clase/', views.insertar_clase,name="insertar_clase"),
    path('hola/', views.hola_mundo),
    
    
    path('profesor/', views.profesor, name="Profesor"),
    path('insertar_profesor/', views.insertar_profesor,name="insertar_profesor"),



]
