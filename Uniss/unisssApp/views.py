from django.shortcuts import render,redirect
from django.http import HttpResponse
from unisssApp.models import Clase,Profesor,Estudiante
from unisssApp.form import FormularioClase, FormularioProfesor
# Create your views here.

def hola_mundo(request):
    return HttpResponse ("Hola mundo :)")



def clase(request):
    clases = Clase.objects.all()
    print('lolo',clases)
    
    return render(request,'Clase/Clase.html',{"otro_nombre":clases})


def insertar_clase(request):
    
    miformulario = FormularioClase()
    claseFormularios = Clase.objects.all()
    
    if request.method == "POST":
        miformulario = FormularioClase(data = request.POST)
        if miformulario.is_valid():
            
            clase = Clase()
            
            clase.nombre = miformulario.cleaned_data["nombreClase"]
            clase.agno = miformulario.cleaned_data["agno"]
            clase.disciplina = miformulario.cleaned_data["disciplina"]
            clase.profesor = miformulario.cleaned_data["profesor"]

            clase.save()

            return redirect("/insertar_clase/")
    
    return render(request,'Clase/insertar.html',{"claseFormularios":claseFormularios,"miformulario":miformulario})

# ==========================================================Profesor====================================================


def profesor(request):
    profesores = Profesor.objects.all()
    
    return render(request,'Profesor/Profesor.html',{"profesor":profesores})


def insertar_profesor(request):
    
    miformulario = FormularioProfesor()
    profesorFormularios = Profesor.objects.all()
    
    if request.method == "POST":
        miformulario = FormularioProfesor(data = request.POST)
        if miformulario.is_valid():
            
            profesor = Profesor()
            
            profesor.nombre = miformulario.cleaned_data["nombreProfesor"]
            profesor.ci = miformulario.cleaned_data["ci"]
            profesor.telefono = miformulario.cleaned_data["telefono"]
            profesor.grado_cientifico = miformulario.cleaned_data["grado_cientifico"]
            profesor.categoria_docente = miformulario.cleaned_data["categoria_docente"]

            profesor.save()

            return redirect("/insertar_profesor/")
    
    return render(request,'Profesor/insertar.html',{"profesorFormularios":profesorFormularios,"miformulario":miformulario})














# ==========================================================Estudiante====================================================