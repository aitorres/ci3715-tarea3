from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import datetime

from .seguridad import Seguridad

global manejador_seguridad
manejador_seguridad = Seguridad()

global usuario
usuario = None

@csrf_exempt
def login(request):
    global usuario

    if usuario:
        redirect('/perfil')

    if request.method == 'POST':
        email = request.POST['inputEmail']
        clave = request.POST['inputPassword']
    
        autenticar = manejador_seguridad.ingresarUsuario(email, clave)

        if autenticar:
            usuario = email
            return redirect('/perfil')
        else:
            messages.warning(request, "Ocurrio un error al iniciar sesion.")

    return render(request, 'login.html')

def logout(request):
    global usuario
    usuario = None
    return render(request, 'logout.html')

@csrf_exempt
def register(request):
    global usuario 

    if usuario:
        redirect('/perfil')

    if request.method == 'POST':
        
        email = request.POST['inputEmail']
        clave1 = request.POST['inputPassword']
        clave2 = request.POST['inputPassword2']

        registrar_usuario = manejador_seguridad.registrarUsuario(email, clave1, clave2)

        if registrar_usuario:
            usuario = email
            return redirect('/perfil')
        else:
            messages.warning(request, "Ocurrio un error al registrarse.")

    return render(request, 'register.html')

def perfil(request):
    if not usuario:
        return redirect('/')

    fecha = datetime.datetime.now()
    return render(request, 'perfil.html', {'correo': usuario, 'fecha': fecha})