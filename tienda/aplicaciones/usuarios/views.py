from django.http.request import HttpHeaders
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def bienvenida(request):
    return render(request,'bienvenida.html')

def login_view(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if(user is not None):
            login(request, user)
            return redirect('bienvenida')
    return render(request, 'login.html')

def register_view(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username = username, email = email, password = password)
        user.save()
        return redirect('login')
    return render(request, 'registrarse.html')

def logout_view(request):
    logout(request)
    return redirect('bienvenida')
