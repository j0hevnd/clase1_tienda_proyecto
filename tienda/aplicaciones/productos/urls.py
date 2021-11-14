from django.urls import path

from .views import GuardarProducto, editarproducto, eliminarproducto, producListAll

urlpatterns = [
    path('lista-productos/', producListAll, name="lista_productos"),
    path('agregar-producto/', GuardarProducto, name='agregar_producto'),
    path('editar-producto/<int:pk>' , editarproducto, name='editar_producto'),
    path('eliminar-producto/<int:pk>', eliminarproducto, name='eliminar_producto'),
]