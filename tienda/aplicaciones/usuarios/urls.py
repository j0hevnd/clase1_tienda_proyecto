from os import name
from django.urls import path

import views


# Este es el nombre que le ponemos a las rutas de cada proyecto,
# así cuando lo llamemos al HTML sea mas amigable y mejora la comprensión de las rutas
app_name = 'app_usuarios'

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('registrar/', views.register_view, name="registrar"),
    path('logout/', views.logout_view, name="logout"),
]