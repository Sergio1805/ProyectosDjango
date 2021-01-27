from django.db import models

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=150)
    contenido =models.TextField()
    imagen = models.ImageField(default='null')
    publicado = models.BooleanField()
    #auto_now_add=True me permite registrar la fecha de creacion del registro
    creado = models.DateTimeField(auto_now_add=True)
    #auto_now=True me permite registrar la fecha cuando se modifique el registro
    actualizado = models.DateTimeField(auto_now=True)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    #models.Datefield() para guardar de manera manual
    creado = models.DateField()

class Autor(models.Model):
    nombre = models.CharField(max_length=150)
    apellido =models.CharField(max_length=150)
    sexo = models.CharField(max_length=1)
    Fecha_nacimiento = models.CharField(max_length=8)
    pais = models.CharField(max_length=50) 
    #auto_now_add=True me permite registrar la fecha de creacion del registro
    creado = models.DateTimeField(auto_now_add=True)
    #auto_now=True me permite registrar la fecha cuando se modifique el registro
    actualizado = models.DateTimeField(auto_now=True)

