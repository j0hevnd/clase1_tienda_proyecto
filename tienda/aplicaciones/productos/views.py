from django.shortcuts import render
from .forms import FormularioProductos
from aplicaciones.productos.models import Producto
# modelo


# Create your views here.

def VistaProducto(request):
    
    
    # Creamos una istancia para el formulario
    if request.method == 'POST':
        formulario = FormularioProductos(request.POST)
        
        #validamos el formulario
        if formulario.is_valid():
            formulario_data = formulario.cleaned_data()
            #obtenemos los datos del formulario
            nombre = formulario_data.get("nombre")
            descripcion = formulario_data.get("descripcion")
            precio = formulario_data.get("precio")
            stock = formulario_data.get("stock")
            imangen = formulario_data.get("imagen")
            # Guardamos la informacion obtenida del formulario en la Base de datos
            Producto.objects.create(
                nombre = nombre,
                descripcion = descripcion,
                precio = precio,
                stock = stock,
                imagen = imangen
            )
            
            
                    