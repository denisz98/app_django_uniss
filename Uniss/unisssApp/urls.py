from django.urls import path
from unisssApp import views
urlpatterns = [
    path('clase/', views.clase, name="Clase"),
    path('insertar_clase/', views.insertar_clase,name="insertar_clase"),
    path('editar_clase/<int:id_clase>', views.editar_clase,name="editar_clase"),
    path('eliminar_clase/<int:id_clase>', views.eliminar_clase,name="eliminar_clase"),
    
    
    path('profesor/', views.profesor, name="Profesor"),
    path('insertar_profesor/', views.insertar_profesor,name="insertar_profesor"),
    path('editar_profesor/<int:id_profesor>', views.editar_profesor,name="editar_profesor"),
    path('eliminar_profesor/<int:id_profesor>', views.eliminar_profesor,name="eliminar_profesor"),

    path('estudiante/', views.estudiante, name="Estudiante"),
    path('insertar_estudiante/', views.insertar_estudiante,name="insertar_estudiante"),
    path('editar_estudiante/<int:id_estudiante>', views.editar_estudiante,name="editar_estudiante"),
    path('eliminar_estudiante/<int:id_estudiante>', views.eliminar_estudiante,name="eliminar_estudiante"),

]
