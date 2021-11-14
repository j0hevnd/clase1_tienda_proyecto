from django.urls import path

from .views import *

# Este es el nombre que le ponemos a las rutas de cada proyecto,
# así cuando lo llamemos al HTML sea mas amigable y mejora la comprensión de las rutas
app_name = 'app_productos'

urlpatterns = [
    path('lista-productos/', producListAll, name="lista_productos"),
    path('agregar-producto/', guardarProducto, name='agregar_producto'),
    path('editar-producto/<int:pk>' , editarProducto, name='editar_producto'),
    path('eliminar-producto/<int:pk>', eliminarProducto, name='eliminar_producto'),
    path('inicio/', homeView, name='home'),
    path('nosotros/', aboutView, name='about'),
]