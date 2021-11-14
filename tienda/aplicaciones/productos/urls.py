from django.urls import path

import views

# Este es el nombre que le ponemos a las rutas de cada proyecto,
# así cuando lo llamemos al HTML sea mas amigable y mejora la comprensión de las rutas
app_name = 'app_productos'

urlpatterns = [
    path('lista-productos/', views.producListAll, name="lista_productos"),
    path('agregar-producto/', views.guardarProducto, name='agregar_producto'),
    path('editar-producto/<int:pk>' , views.editarProducto, name='editar_producto'),
    path('eliminar-producto/<int:pk>', views.eliminarProducto, name='eliminar_producto'),
]