from django import forms


class Carrera_form(forms.Form):
    nombre = forms.CharField(max_length=40)
    comision = forms.IntegerField()

class Profesor_form(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    dni = forms.IntegerField()
    email = forms.EmailField()
    carrera = forms.CharField(max_length=40)

class Alumno_form(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    dni = forms.IntegerField()
    email = forms.EmailField()
    carrera = forms.CharField(max_length=40)
    comision = forms.IntegerField()