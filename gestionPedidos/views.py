from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from PIL import Image

from .models import Cliente
from .models import Articulo

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.http import request
import tempfile
import os
from django.core.files.base import ContentFile

from gestionPedidos.models import Articulo
from gestionPedidos.models import Cliente

# Create your views here.


def inicio (request):
    articuloListado = Articulo.objects.all()
    return render(request, 'inicio.html', {'articulo':articuloListado})    

def salir(request):
    logout(request)
    return redirect('/')


@login_required
def gestion(request):
    articuloListado = Articulo.objects.all()
    return render(request, 'listar_articulos.html', {'articulo':articuloListado})

def mostrarClientes(request):
    clienteListado = Cliente.objects.all()
    return render(request, 'mostrar_clientes.html', {'cliente':clienteListado})




def articulos(request):
    articuloListado = Articulo.objects.all()
    return render(request, 'listar_articulos.html', {'articulo':articuloListado})






def editarArticulo(request, id):
    articulo = Articulo.objects.get(id = id)
    return render(request, 'editar_articulos.html', {'articulo': articulo})






def eliminarArticulo (request, id):
    articulo = Articulo.objects.get(id = id)
    articulo.delete()
    return redirect('/gestion/')

# clientes

def clientes(request):
    clienteListado = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'cliente':clienteListado})

def registrarCliente(request):
    nombre = request.POST['nombre']
    telefono = request.POST['telefono']
    email = request.POST['email']
    direccion = request.POST['direccion']  
    notas = request.POST['notas']    
    foto_perfil = request.FILES.get('foto_perfil')
    cliente = Cliente.objects.create(nombre=nombre, telefono=telefono, email=email, direccion=direccion, notas=notas)
    if foto_perfil:
        cliente.foto_perfil = foto_perfil
    cliente.save()
    return redirect('/clientes/')

def registrarArticulo(request):
    nombre = request.POST['nombre']
    seccion = request.POST['seccion']
    precio = request.POST['precio']
    descripcion = request.POST['descripcion']    
    foto_articulo = request.FILES.get('foto_articulo')    
    articulo = Articulo.objects.create(nombre=nombre, seccion=seccion, precio=precio, descripcion=descripcion)    
    if foto_articulo:
        articulo.foto_articulo = foto_articulo    
    articulo.save()    
    return redirect('/gestion/')

def editarCliente(request, id):
    cliente = Cliente.objects.get(id = id)
    return render(request, 'editar_clientes.html', {'cliente': cliente})


def detallesCliente(request, id):
    cliente = get_object_or_404(Cliente, id = id)
    #cliente = Cliente.objects.get(id = id)
    return render(request, 'detalles_cliente.html', {'cliente': cliente})

def detallesArticulo(request, id):
    articulo = get_object_or_404(Articulo, id = id)
    #cliente = Cliente.objects.get(id = id)
    return render(request, 'detalles_articulo.html', {'articulo': articulo})

def actualizarCliente(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    telefono = request.POST['telefono']
    email = request.POST['email']
    notas = request.POST['notas']    
    cliente = Cliente.objects.get(id = id)    
    cliente.nombre = nombre
    cliente.telefono = telefono
    cliente.email = email
    cliente.notas = notas   
    if 'foto_perfil' in request.FILES:
        cliente.foto_perfil = request.FILES['foto_perfil']
    cliente.save()
    return redirect('/clientes/')


def actualizarArticulo(request):
    id = request.POST['id']
    nombre = request.POST['nombre']
    seccion = request.POST['seccion']
    precio = request.POST['precio']    
    
    articulo = Articulo.objects.get(id = id)    
    articulo.nombre = nombre
    articulo.seccion = seccion
    articulo.precio = precio
    
    if 'foto_articulo' in request.FILES:
        articulo.foto_articulo = request.FILES['foto_articulo']
    articulo.save()
    return redirect('/gestion/')


def eliminarCliente (request, id):
    cliente = Cliente.objects.get(id = id)
    cliente.delete()
    return redirect('/clientes/')