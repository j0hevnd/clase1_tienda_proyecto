from django.urls import path

from .views import GuardarProducto, editarproducto, eliminarproducto, producListAll

urlpatterns = [
    path('listaproductos/',producListAll,name="listaproductos"),
    path('agregarproducto/',GuardarProducto,name='agregarproducto'),
    path('editarproducto/<int:pk>' ,editarproducto,name='editarproducto'),
    path('eliminarproducto/<int:pk>',eliminarproducto,name='eliminarproducto'),

]