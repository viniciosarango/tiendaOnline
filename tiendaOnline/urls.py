from django.contrib import admin
from django.urls import path, include
from gestionPedidos.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('gestion/', gestion, name='gestion'),
    path('mostrarClientes/', mostrarClientes, name='mostrarClientes'),
    path('articulos/', gestion),
    
    path('registrarArticulo/', registrarArticulo, name='registrarArticulo'),
    path('gestion/editarArticulo/<int:id>', editarArticulo, name='editarArticulo'),
    path('gestion/detallesArticulo/<int:id>', detallesArticulo, name='detallesArticulo'),
    path('actualizarArticulo/', actualizarArticulo, name='actualizarArticulo'),
    path('gestion/eliminarArticulo/<int:id>', eliminarArticulo, name='eliminarArticulo'),

    path('clientes/', clientes),

    path('registrarCliente/', registrarCliente),
    path('clientes/editarCliente/<int:id>', editarCliente),
    path('mostrarClientes/clientes/detallesCliente/<int:id>', detallesCliente),
    path('actualizarCliente/', actualizarCliente),
    path('clientes/eliminarCliente/<int:id>', eliminarCliente),

    path('accounts/', include('django.contrib.auth.urls')),
    path('salir/', salir, name='salir'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
