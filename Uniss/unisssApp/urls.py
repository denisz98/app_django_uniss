from django.urls import path
from unisssApp import views
urlpatterns = [
       path('clase/', views.clase ),
           path('hola/', views.hola_mundo ),


    
]
