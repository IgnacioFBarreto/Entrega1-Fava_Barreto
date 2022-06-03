from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("alumnos", views.alumnos, name="alumnos"),
    path("profesores", views.profesores, name="profesores"),
    path("carreras", views.carreras, name="carreras"),
    path("carrera_formulario", views.carrera_formulario, name="carrera_formulario"),
    path("profesor_formulario", views.profesor_formulario, name="profesor_formulario"),
    path("alumno_formulario", views.alumno_formulario, name="alumno_formulario"),
    path("buscar_carrera", views.buscar_carrera, name="buscar_carrera"),
    path("buscar", views.buscar),
    path("resultado_buscar", views.buscar)
]