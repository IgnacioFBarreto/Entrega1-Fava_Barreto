from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Alumno, Carrera, Profesor
from django.template import loader
from app_coder.forms import *

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def carreras(request):
    carrera = Carrera.objects.all()
    datos = {"datos": carrera}
    return render(request, "carreras.html", datos)

def alumnos(request):
    alumno = Alumno.objects.all()
    datos = {"datos": alumno}
    return render(request, "alumnos.html", datos)

def profesores(request):
    profesor = Profesor.objects.all()
    datos = {"datos": profesor}
    return render(request, "profesores.html", datos)

def carrera_formulario(request):
    if request.method == "POST":
        
        mi_form = Carrera_form(request.POST)

        if mi_form.is_valid():
            datos = mi_form.cleaned_data
            carrera = Carrera(nombre=datos['nombre'], comision=datos['comision'])
            carrera.save()
            return render(request, "carreras.html")

    return render(request, "carrera_formulario.html")

def profesor_formulario(request):
    if request.method == "POST":
        
        mi_form = Profesor_form(request.POST)

        if mi_form.is_valid():
            datos = mi_form.cleaned_data
            profesor = Profesor(nombre=datos['nombre'], apellido=datos['apellido'], edad=datos['edad'], dni=datos['dni'], email=datos['email'], carrera=datos['carrera'])
            profesor.save()
            return render(request, "profesores.html")

    return render(request, "profesor_formulario.html")

def alumno_formulario(request):
    if request.method == "POST":
        
        mi_form = Alumno_form(request.POST)

        if mi_form.is_valid():
            datos = mi_form.cleaned_data
            alumno = Alumno(nombre=datos['nombre'], apellido=datos['apellido'], edad=datos['edad'], dni=datos['dni'], email=datos['email'], carrera=datos['carrera'], comision=datos['comision'])
            alumno.save()
            return render(request, "alumnos.html")

    return render(request, "alumno_formulario.html")

def buscar_carrera(request):
    return render(request, "buscar_carrera.html")
def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        carreras = Carrera.objects.filter(nombre__icontains = nombre)
        return render(request, "resultado_buscar.html", {"carreras": carreras})
    else:
        return HttpResponse("Campo vacío")