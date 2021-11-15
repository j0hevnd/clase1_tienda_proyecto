from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render

# modelo
from aplicaciones.productos.models import Producto

# formularios
from .forms import FormularioProductos


def producListAll(request):
    """
    Lista todos los productos
    """
    productos = Producto.objects.all()
    
    context = {
        'productos': productos
    }
    return render(request, template_name="productos/productos.html", context=context)


def guardarProducto(request):
    """
    Guarda producto en la base de datos
    """
    
    # Creamos una istancia para el formulario
    if request.method == 'POST':
        formulario = FormularioProductos(request.POST,request.FILES)
        #validamos el formulario
        # if formulario.is_valid():
        #     formulario_data = formulario.cleaned_data()
        #     #obtenemos los datos del formulario
        #     nombre = formulario_data.get("nombre")
        #     descripcion = formulario_data.get("descripcion")
        #     precio = formulario_data.get("precio")
        #     stock = formulario_data.get("stock")
        #     imagen = formulario_data.get("imagen")
        #     # Guardamos la informacion obtenida del formulario en la Base de datos
        #     Producto.objects.create(
        #         nombre = nombre,
        #         descripcion = descripcion,
        #         precio = precio,
        #         stock = stock,
        #         imagen = imagen
        #     )
        #     # Tenemos que hacer un redirect o HttpResponseRedirect 
        #     # despues de una solicitud éxitosa de un método POST
        #     return redirect('app_productos:lista_productos')
        if formulario.is_valid():
            formulario.save()
            return redirect('app_productos:lista_productos')
    agregar_producto=  FormularioProductos()
    return render(request,'productos/agregar_producto.html',{'formulario':agregar_producto})           
            
                    
def editarProducto(request, pk):
    """
    Edita un producto seleccionado
    
    Args:
        pk: id de producto a editar
    """
    
    producto = Producto.objects.get(pk=pk)
    
    if request.method == 'POST':
        formulario = FormularioProductos(request.POST, instance=producto)
        
        #validamos el formulario
        if formulario.is_valid():
            formulario_data = formulario.cleaned_data()
            #obtenemos los datos del formulario
            nombre = formulario_data.get("nombre")
            descripcion = formulario_data.get("descripcion")
            precio = formulario_data.get("precio")
            stock = formulario_data.get("stock")
            imagen = formulario_data.get("imagen")
            # Guardamos la informacion obtenida del formulario en la Base de datos
            Producto.objects.create(
                nombre = nombre,
                descripcion = descripcion,
                precio = precio,
                stock = stock,
                imagen = imagen
            )
            return redirect(to = 'app_productos:lista_productos')
            
    context = {
        'producto': producto
    }
    return render(request, template_name="productos/tempalte_para_editar.html", context=context)


def eliminarProducto(request,pk):
    """
    Elimina un producto seleccionado
    
    Args:
        pk: id del producto a eliminaar
    """
    producto = Producto.objects.get(pk=pk)
    producto.delete()
    
    return redirect(to = 'app_productos:lista_productos')


### HOME

def homeView(request):
    """
    Pagina de inicio
    """       
    
    return render(request, template_name='home/home.html')


def aboutView(request):
    """
    Pagina de nosotros
    """       
    
    return render(request, template_name='home/about.html')