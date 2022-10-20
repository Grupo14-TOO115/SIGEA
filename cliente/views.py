from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def crear_cliente(request):
    # se almacena un formulario del modelo cliente (con datos or vacio)
    formulario = ClienteForm(request.POST or None, request.FILES or None)

    # si es el formulario es valido ...
    if formulario.is_valid():
        # al guardar el formulario, se guarda el objeto en la DB y en la variable cliente
        cliente = formulario.save()

        # se crea un objeto "solicitud"
        solicitud = Solicitud()

        # se le asigna el cliente a la solicitud
        solicitud.id_cliente = cliente

        # se guarda el objeto en la DB, almacenando los atributos que faltaron
        # con sus valores por defecto (revisar modelo.py)
        solicitud.save()

        # SE DEBE HACER UN PROCESO SIMILAR PARA ALMACENAR LO DEMAS
        # MODIFICAR EL MODELO DE SOLICTUD YA QUE FALTAN VARIAS LLAVES FORANEAS

        messages.success(request, "Se envio la solicitud exitosamente!")
        return redirect('home')

    # si el formulario no es valido renderiza la pagina, envia a la pagina el request y el formulario
    return render(request, 'cliente/crear.html', {'formulario': formulario})


@login_required
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/index.html', {'clientes': clientes})

@login_required
def localidad(request):
    return render(request, 'localidad/localidad.html')
