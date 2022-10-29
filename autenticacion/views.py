from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from cliente.models import Cliente
from .forms import *
from .models import Usuario
from datetime import date
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager
# Create your views here.


def salir(request):
    logout(request)
    return redirect('login')


def entrar(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            nom_user = formulario.cleaned_data.get("username")
            pas_user = formulario.cleaned_data.get("password")

            usuario = authenticate(username=nom_user, password=pas_user)

            if usuario is not None:
                if usuario.last_login is None:
                    login(request, usuario)

                    return redirect('change_password')

                login(request, usuario)

                redireccion = request.GET.get('next', '/')

                return redirect(redireccion)
            else:
                messages.error(request, "Esta cuenta esta inactiva")
        else:
            messages.error(request, "Usuario o contraseña incorrecta")

    formulario = AuthenticationForm()

    return render(request, "login/login.html", {'formulario': formulario})


def asignarUsername(id_solicitud):
    usuario = User.objects.get(pk=id_solicitud)

    inicial_1 = usuario.first_name[:1]
    inicial_2 = usuario.last_name[:1]
    año = date.today().year.__str__()[2:]
    correlativo = "-" + usuario.pk.__str__()

    username = inicial_1 + inicial_2 + año + correlativo

    usuario.username = username

    usuario.save()


def registrarUsuario(id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)

    if cliente:
        # se crear un objeto usuario
        usuario = User()

        # genera una contraeña aletoria
        password = BaseUserManager().make_random_password(6)
        print(password) # esto deberia de mandarse por correo

        # se le asignan todos los campos de cliente
        usuario.username = 'temp'
        usuario.password = make_password(password)
        usuario.first_name = cliente.nombres
        usuario.last_name = cliente.apellidos
        usuario.email = cliente.correo

        # se almacena en la BD
        usuario.save()

        # se le asigna un nombre de usuario, se la pasa el id
        asignarUsername(usuario.pk)

        # se crea un usuario del modulo autenticacion
        rol = Usuario()

        # se asigna un rol y el correspendiente usuario al que pertenece
        rol.es_asociado = True
        rol.user = usuario
        rol.es_primeraVez = True

        # se almacena en la BD
        rol.save()

        #mandar correo


def error_404(request, exception):
    messages.warning(request, "La página solicitada no se encuentra")
    return redirect('inicio')


def error_500(request, exception=None):
    messages.info(request, " El servidor encontró una condición inesperada que le impide completar la petición")
    return redirect('inicio')


def error_403(request, exception=None):
    messages.info(request, "El servidor ha recibido la petición, pero rechaza enviar una respuesta")
    return redirect('inicio')


def error_400(request, exception=None):
    messages.info(request, "El servidor no puede procesar la petición debido a un error del cliente")
    return redirect('inicio')
