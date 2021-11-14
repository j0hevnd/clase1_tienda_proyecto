from django.shortcuts import redirect, render

# modelo
from aplicaciones.productos.models import Producto

# formularios
from .forms import FormularioProductos


def producListAll(request):
    """
    Listamos todos los productos
    """
    productos = Producto.objects.all()
    
    context = {
        'productos': productos
    }
    return render(request, template_name="productos/productos.html", context=context)


def GuardarProducto(request):
    
    
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
    agregarproducto=  FormularioProductos()
    return render(request,'productos/agregar_producto.html',{'formulario':agregarproducto})           
            
                    
def editarproducto(request,pk):
    producto = Producto.objects.get(pk=pk)
    
    if request.method == 'POST':
        formulario = FormularioProductos(request.POST,instance=producto)
        
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
            return redirect(to = 'listaproductos')
            
def eliminarproducto(request,pk):
    producto = Producto.objects.get(pk=pk)
    producto.delete()
    return redirect(to = 'listaproductos')            