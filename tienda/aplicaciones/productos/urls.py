from django.urls import path

import views


app_name = 'app_productos'
urlpatterns = [
    path('lista-productos/', views.producListAll, name="lista_productos"),
    path('agregar-producto/', views.GuardarProducto, name='agregar_producto'),
    path('editar-producto/<int:pk>' , views.editarproducto, name='editar_producto'),
    path('eliminar-producto/<int:pk>', views.eliminarproducto, name='eliminar_producto'),
]