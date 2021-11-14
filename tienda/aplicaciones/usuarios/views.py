from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def bienvenida(request):
    return render(request,'bienvenida.html')

def login_view(request):
    """
    Espacion para comentar que hace la función
    """
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
    Espacion para comentar que hace la función
    """
    if(request.method == 'POST'):        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username = username, email = email, password = password)
        if 'staff' in request.POST:
            user.is_staff = True
        user.save()
        
        return redirect('app_usuarios:login')
    return render(request, 'usuarios/registro.html')


def logout_view(request):
    """
    Espacion para comentar que hace la función
    """
    logout(request)
    return redirect('app_productos:lista_productos')
