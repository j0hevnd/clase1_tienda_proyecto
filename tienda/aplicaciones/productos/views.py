from django.shortcuts import render

# modelo
from models import Producto

# Create your views here.

def producListAll(request):
    """
    Listamos todos los productos
    """
    productos = Producto.objects.all()
    
    context = {
        'productos': productos
    }
    return render(request, template_name="productos/nombre_html.html", context=context)