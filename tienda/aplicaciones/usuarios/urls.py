from os import name
from django.urls import path

import views

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('registrar/', views.register_view, name="registrar"),
    path('logout/', views.logout_view, name="logout"),
]