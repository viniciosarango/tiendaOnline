

from django.db import models
from PIL import Image
import os
from django.core.files.base import ContentFile

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    direccion = models.CharField(max_length=150, default='')
    notas = models.TextField(blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='clientes/fotos_perfil', blank=True, null=True)
    
    
    
    

class Articulo (models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=30)
    precio = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    foto_articulo = models.ImageField(upload_to='articulos/fotos_articulo', blank=True, null=True)
    

class Pedido (models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
    