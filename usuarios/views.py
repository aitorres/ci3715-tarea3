from django.shortcuts import render, redirect # Se importan modulos para mostrar vistas y redirigir URLS
from django.contrib import messages # Se importa paquete para manejar mensajes de error
from django.views.decorators.csrf import csrf_exempt # Se importa decorador de inicio de sesion para eliminar problema
import datetime # Se importa manejador de fechas

# MODULO DE SEGURIDAD, la clase Seguridad incorpora los metodos de
# registrar usuario e ingresar usuarios, desarrollados utilizando TDD.
from .seguridad import Seguridad

# Se configura la variable como global para mantener el estado entre una vista y otra
global manejador_seguridad
manejador_seguridad = Seguridad() # Instancia del manejador de seguridad

# Se guarda como variable global el usuario logueado en este momento, si es None es porque no esta logueado.
global usuario
usuario = None

@csrf_exempt
def login(request):
    '''
    LOGIN. Controlador de la vista que se encarga de manejar la pagina para iniciar
    sesion. Redirige al perfil si estas logueado; en caso contrario, intenta interpretar
    el formulario y realizar login o reportar un error si los datos son incorrectos. En caso
    de que lo sean, o si no se ha llenado el formulario (primer acceso), solo carga el formulario
    como pagina web.
    '''
    
    global usuario # Guarda estado del usuario
    
    # Verifica si ya estas logueado, y si lo estas, redirige a la pagina de perfil
    if usuario:
        redirect('/perfil')

    # Si hiciste submit del formulario, intenta manejar el flujo de inicio de sesion
    if request.method == 'POST':
        # Tomo los valores del formulario
        email = request.POST['inputEmail']
        clave = request.POST['inputPassword']
        
        # Guardo en autenticar el resultado del intento de login
        autenticar = manejador_seguridad.ingresarUsuario(email, clave)
    
        if autenticar:
            # CASO: LOGIN CORRECTO, REDIRIGIR A PERFIL
            usuario = email
            return redirect('/perfil')
        else:
            # CASO: LOGIN INCORRECTO, GUARDAR ERROR PARA MOSTRAR
            messages.warning(request, "Ocurrio un error al iniciar sesion.")
    
    # Redirige al formulario de login como pagina web
    return render(request, 'login.html')

def logout(request):
    '''
    Controlador que maneja la vista de LOGOUT. Si se accede aca,
    se elimina el usuario que esta logueado y se muestra un mensaje
    de logout satisfactorio.
    '''
    
    # Guardamos globalmente el usuario como None para saber que esta deslogueado
    global usuario
    usuario = None
    
    # Redirige a la vista de cierre de sesion con su mensaje
    return render(request, 'logout.html')

@csrf_exempt
def register(request):
    '''
    Controlador que se encarga de la logica de la vista REGISTRO.
    Si se accede habiendo iniciado sesion, se redirige al perfil. Si se
    reciben datos de formulario, intenta registrar el usuario y dependiendo de eso
    redirige al perfil o muestra un mensaje de error. Finalmente, si no se redirige,
    muestra la interfaz con el formulario de registro.
    '''
    
    # Se trae la variable usuario global
    global usuario 
    
    # Si estas logueado, te redirige al perfil
    if usuario:
        redirect('/perfil')

    # Flujo para manejar las variables recibidas del formulario
    if request.method == 'POST':
        # Guardamos las tres respuestas del formulario
        email = request.POST['inputEmail']
        clave1 = request.POST['inputPassword']
        clave2 = request.POST['inputPassword2']
    
        # Intentamos registrar el usuario con los metodos de seguridad.py
        registrar_usuario = manejador_seguridad.registrarUsuario(email, clave1, clave2)

        # Verificamos si el intento de registro fue exitoso
        if registrar_usuario:
            # CASO: REGISTRO EXITOSO, almaceno el usuario de manera global y redirigo a
            # su perfil.
            usuario = email
            return redirect('/perfil')
        else:
            # CASO: REGISTRO FALLIDO, muestra un error en la interfaz
            messages.warning(request, "Ocurrio un error al registrarse.")

    # Se muestra la vista del formulario de registro
    return render(request, 'register.html')

def perfil(request):
    '''
    Controlador que maneja la vista de perfil de usuario, que es la vista
    que se muestra cuando se esta correctamente logueado en el sistema. La funcionalidad
    basica es mostrar su correo como usuario logueado y la fecha del dia en que se conecta.
    Ademas muestra un link para cerrar sesion.
    '''
    
    global usuario # Se trae la variable usuario global
    
    # Si no se esta logueado, redirige a la vista de login
    if not usuario:
        return redirect('/')
    
    # Buscamos la fecha del momento y cargamos la vista de perfil en la interfaz web
    # con el correo del usuario y la fecha.
    fecha = datetime.datetime.now()
    return render(request, 'perfil.html', {'correo': usuario, 'fecha': fecha})
