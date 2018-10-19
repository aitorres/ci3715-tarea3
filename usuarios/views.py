from django.shortcuts import render
from django.http import HttpResponse
import datetime

from .seguridad import Seguridad

global manejador_seguridad
manejador_seguridad = Seguridad()

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def register(request):
    return render(request, 'register.html')

def perfil(request):
    return render(request, 'perfil.html')

