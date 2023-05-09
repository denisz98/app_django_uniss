from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from unisssApp.models import Clase,Profesor,Estudiante
from unisssApp.form import FormularioClase, FormularioProfesor,FormularioEstudiante
# Create your views here.




def clase(request):
    clases = Clase.objects.all()
    
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

            return redirect("/clase/")
    
    return render(request,'Clase/insertar.html',{"claseFormularios":claseFormularios,"miformulario":miformulario})



def editar_clase(request,id_clase):
    
    clase = get_object_or_404(Clase, idClase=id_clase)
    miformulario = FormularioClase(initial={'nombreClase':clase.nombre,'agno':clase.agno,'disciplina':clase.disciplina,'profesor':clase.profesor})
    if request.method == "POST":
        miformulario = FormularioClase(data = request.POST)
        if miformulario.is_valid():
            clase.nombreClase = miformulario.cleaned_data["nombreClase"]
            clase.agno = miformulario.cleaned_data["agno"]
            clase.disciplina = miformulario.cleaned_data["disciplina"]
            clase.profesor = miformulario.cleaned_data["profesor"]
            clase.save()
            return redirect("/clase/")
    return render(request,'Clase/editar.html',{"miformulario":miformulario})

def eliminar_clase(request,id_clase):
    
    clase= Clase.objects.get(pk = id_clase)
    
    clase.delete()
    
    return redirect("/clase/")




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




def editar_profesor(request,id_profesor):
    
    profesor = get_object_or_404(Profesor, idProfesor=id_profesor)
    miformulario = FormularioProfesor(initial={'nombreProfesor':profesor.nombre,'ci':profesor.ci,'telefono':profesor.telefono,'grado_cientifico':profesor.grado_cientifico,'categoria_docente':profesor.categoria_docente})
    if request.method == "POST":
        miformulario = FormularioProfesor(data = request.POST)
        if miformulario.is_valid():
            profesor.nombre = miformulario.cleaned_data["nombreProfesor"]
            profesor.ci = miformulario.cleaned_data["ci"]
            profesor.telefono = miformulario.cleaned_data["telefono"]
            profesor.grado_cientifico = miformulario.cleaned_data["grado_cientifico"]
            profesor.categoria_docente = miformulario.cleaned_data["grado_cientifico"]
            profesor.save()
            return redirect("/profesor/")
    return render(request,'Profesor/editar.html',{"miformulario":miformulario})

def eliminar_profesor(request,id_profesor):
    
    profesor= Profesor.objects.get(pk = id_profesor)
    
    profesor.delete()
    
    return redirect("/profesor/")



# ==========================================================Estudiante====================================================
def estudiante(request):

    estudiantes = Estudiante.objects.all()
    estudiante = []
    for i in estudiantes:
        e = []
        for j in i.clase.all():
            e.append(Clase.objects.get(pk =j.idClase))
        estudiante.append({'idEstudiante':i.idEstudiante,'nombre':i.nombre,"ci":i.ci,'telefono':i.telefono,'direccion':i.direccion,'agno_academico':i.agno_academico,'clase':e})

    return render(request,'Estudiante/Estudiante.html',{"estudiante":estudiante})


def insertar_estudiante(request):
    if request.method == 'POST':
        form = FormularioEstudiante(request.POST)
        if form.is_valid():
            estudiante = Estudiante()
            estudiante.nombre_clase = form.cleaned_data['nombreClase']
            estudiante.nombre = form.cleaned_data['nombre']
            estudiante.ci = form.cleaned_data['ci']
            estudiante.direccion = form.cleaned_data['direccion']
            estudiante.telefono = form.cleaned_data['telefono']
            estudiante.agno_academico = form.cleaned_data['agno_academico']

            estudiante.save()

            estudiante.clase.set(estudiante.nombre_clase)

            return redirect('/estudiante/')
    else:
        form = FormularioEstudiante()

    return render(request, 'Estudiante/insertar.html', {'miformulario': form})





def editar_estudiante(request,id_estudiante):
    
    estudiante = get_object_or_404(Estudiante, idEstudiante=id_estudiante)
    miformulario = FormularioEstudiante(initial={'nombre':estudiante.nombre,'ci':estudiante.ci,'telefono':estudiante.telefono,'direccion':estudiante.direccion,'agno_academico':estudiante.agno_academico})
    if request.method == "POST":
        miformulario = FormularioEstudiante(data = request.POST)
        if miformulario.is_valid():
            estudiante.nombre = miformulario.cleaned_data["nombre"]
            estudiante.ci = miformulario.cleaned_data["ci"]
            estudiante.telefono = miformulario.cleaned_data["telefono"]
            estudiante.direccion = miformulario.cleaned_data["direccion"]
            estudiante.agno_academico = miformulario.cleaned_data["agno_academico"]
            estudiante.save()
            return redirect("/estudiante/")
        
    return render(request,'Estudiante/editar.html',{"miformulario":miformulario})

def eliminar_estudiante(request,id_estudiante):
    
    estudiante= Estudiante.objects.get(pk = id_estudiante)
    
    estudiante.delete()
    
    return redirect("/estudiante/")