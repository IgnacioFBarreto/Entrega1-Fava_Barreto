from django.db import models

# Create your models here.

class Carrera(models.Model):

    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()

class Alumno(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    dni = models.IntegerField()
    email = models.EmailField()
    carrera = models.CharField(max_length=40)
    comision = models.IntegerField()

class Profesor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    dni = models.IntegerField()
    email = models.EmailField()
    carrera = models.CharField(max_length=40)