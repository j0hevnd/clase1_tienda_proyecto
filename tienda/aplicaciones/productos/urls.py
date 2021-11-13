from django.urls import path

from .views import *

urlpatterns = [
    path('listaproductos/',producListAll,name="listaproductos"),
    path('agregarproducto/',GuardarProducto,name='agregarproducto'),
]