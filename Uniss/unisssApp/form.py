from django import forms
from .models import Clase, Disciplina,Profesor

class FormularioClase(forms.Form):
    
   nombreClase =  forms.CharField(required=True)
   agno =  forms.CharField(required=True)
   disciplina =  forms.ModelChoiceField (label = "Disciplina",queryset=Disciplina.objects.all())
   profesor =  forms.ModelChoiceField (label ="Profesor",queryset=Profesor.objects.all())
    
class FormularioProfesor(forms.Form):
    
   nombreProfesor =forms.CharField (label = "Nombre",required=True)
   ci =  forms.CharField(label = "Carnet identidad",required=True)
   telefono =  forms.CharField(label ="Teléfono",required=True)
   grado_cientifico =  forms.CharField(label = "Grado científico",required=True)
   categoria_docente =  forms.CharField(label = "Categoría docente",required=True)
   
   
class FormularioEstudiante(forms.Form):
    
   nombreClase =forms.ModelMultipleChoiceField (label = "Clases",queryset=Clase.objects.all())
   nombre =  forms.CharField(label = "Nombre",required=True)
   ci =  forms.CharField(label = "Carnet identidad",required=True)
   direccion =  forms.CharField(label = "Dirección",required=True)
   telefono =  forms.CharField(label ="Teléfono",required=True)
   agno_academico =  forms.CharField(label = "Año académico",required=True)