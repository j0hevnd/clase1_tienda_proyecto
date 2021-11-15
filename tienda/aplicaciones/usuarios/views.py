from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def login_view(request):
    """
    Loguear un usuario
    """
    print(request.POST)
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if(user is not None):
            login(request, user)
            return redirect('app_productos:lista_productos')
        
    return render(request, 'usuarios/login-vista.html')


def register_view(request):
    """
    Registra un usuario en la base de datos
    """
    
    if(request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username = username, email = email, password = password)
        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        if 'staff' in request.POST:
            user.is_staff = True
        user.save()
        
        return redirect('app_usuarios:login')
    return render(request, 'usuarios/registro.html')


def logout_view(request):
    """
    Cerrar sesión
    """
    logout(request)
    return redirect('app_usuarios:login')
