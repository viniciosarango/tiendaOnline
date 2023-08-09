from django.contrib import admin
from gestionPedidos.models import Cliente
from gestionPedidos.models import Articulo
from gestionPedidos.models import Pedido
# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email', 'direccion', 'notas', 'get_foto_perfil_url')
    
    def get_foto_perfil_url(self, obj):
        if obj.foto_perfil:
            return obj.foto_perfil.url
        return '-'
    get_foto_perfil_url.short_description = 'Foto de perfil (URL)'

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'seccion', 'precio')


class PedidoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fecha', 'entregado')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Pedido, PedidoAdmin)
