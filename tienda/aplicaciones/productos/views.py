from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required # para proteger rutas


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


# protegemos ruta para que solo puedan acceder usuarios logueados
@login_required(login_url='app_usuarios:login') 
def guardarProducto(request):
    """
    Guarda producto en la base de datos
    """
    # Creamos una istancia para el formulario
    if request.method == 'POST':
        formulario = FormularioProductos(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('app_productos:lista_productos')
        
    agregar_producto=  FormularioProductos()
    
    return render(request,'productos/agregar_producto.html',{'formulario':agregar_producto})           
        
        
# protegemos ruta para que solo puedan acceder usuarios logueados
@login_required(login_url='app_usuarios:login')                    
def editarProducto(request, pk):
    """
    Edita un producto seleccionado
    
    Args:
        pk: id de producto a editar
    """
    
    producto = Producto.objects.get(pk=pk)
    
    if request.method == 'GET':
        producto_form = FormularioProductos(instance=producto)
    
    if request.method == 'POST':
        formulario = FormularioProductos(request.POST, instance=producto)
        
        #validamos el formulario
        if formulario.is_valid():
            formulario.save()
            return redirect(to = 'app_productos:lista_productos')
            
    context = {
        'formulario': producto_form
    }
    return render(request, template_name="productos/agregar_producto.html", context=context)


@login_required(login_url='app_usuarios:login') 
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