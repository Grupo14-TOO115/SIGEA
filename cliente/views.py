from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from autenticacion.views import registrarUsuario
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

        # AQUI SE ALMACENACENA EL OBJETO SOLICITUD "FALTA id_actividadEconomica"
        solicitud.save()

        # SE DEBE HACER UN PROCESO SIMILAR PARA ALMACENAR LO DEMAS
        # MODIFICAR EL MODELO DE SOLICTUD YA QUE FALTAN VARIAS LLAVES FORANEAS

        # messages.success(request, "Se envio la solicitud exitosamente!")
        return redirect('localidad', solicitud.id_solicitud)

    # si el formulario no es valido renderiza la pagina, envia a la pagina el request y el formulario
    return render(request, 'cliente/crear.html', {'formulario': formulario})


@login_required
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/index.html', {'clientes': clientes})


def crear_capacidad_economica(request, id_solicitud):
    formulario_CapacidadEconomica = CapacidadEconoForm(request.POST or None, request.FILES or None)

    # si es el formulario es valido ...

    if formulario_CapacidadEconomica.is_valid():
        solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
        actividadEconomica = ActividadEconomica.objects.get(id_actividadEconomica=solicitud.id_actividadEconomica.id_actividadEconomica )

        capacidadEconomica = formulario_CapacidadEconomica.save(commit=False)
        capacidadEconomica.total= capacidadEconomica.salario + capacidadEconomica.otrosIngresos - capacidadEconomica.gastosAFP - capacidadEconomica.gastosISSS - capacidadEconomica.gastosPersonales - capacidadEconomica.gastosEducacion - capacidadEconomica.prestamos

        # se le asigna una capacidad economica a la actividad economica
        actividadEconomica.id_capacidadEconomica = capacidadEconomica
        capacidadEconomica.save()
        actividadEconomica.save()

        messages.success(request, "Se guardo con exito")
        # return redirect('falta alexander', id_solicitud)
        return redirect('home')

    # si el formulario no es valido renderiza la pagina, envia a la pagina el request y el formulario
    return render(request, 'capacidadEconomica/crear.html', {'formulario_CapacidadEconomica': formulario_CapacidadEconomica})


def crear_actividad_economica(request, id_solicitud):
    formulario_ActividadEconomica = ActEconoForm(request.POST or None)

    # si es el formulario es valido ...

    if formulario_ActividadEconomica.is_valid():

        # al guardar el formulario, se guarda el objeto en la DB y en la variable cliente

        actEconomica = formulario_ActividadEconomica.save()

        # se crea un objeto "solicitud"
        solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)

        # se le asigna actividad economica a la solicitud
        solicitud.id_actividadEconomica = actEconomica
        solicitud.save()

        # messages.success(request, "Se envio la solicitud exitosamente!")
        return redirect('crear_capacidad_economica', solicitud.id_solicitud)

        # si el formulario no es valido renderiza la pagina, envia a la pagina el request y el formulario
    return render(request, 'actividadEconomica/crear.html', {'formulario_ActividadEconomica': formulario_ActividadEconomica})


def crear_estadocivil(request, id_solicitud):
    formulario_estadocivil = EstadocivilForm(request.POST or None)

    if formulario_estadocivil.is_valid():
        estadocivil = formulario_estadocivil.save()

        # Recupera un objeto del tipo cliente que coincida con el id_cliente.
        solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
        cliente = Cliente.objects.get(id_cliente=solicitud.id_cliente.id_cliente)

        # Al objeto "cliente" en el atributo "id_estadocivil" se le asigna el objeto "estadocivil" recién creado.
        cliente.id_estadocivil = estadocivil

        # se guarda el objeto en la DB, almacenando los atributos que faltaban
        cliente.save()

        return redirect('crear_actividad_economica', id_solicitud)

    return render(request, 'estado_civil/registrar.html', {'formulario_estadocivil': formulario_estadocivil})


def localidad(request, id_solicitud):

    formularioDomicilio = DomicilioForm(request.POST or None)

    if formularioDomicilio.is_valid():
        solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
        cliente = Cliente.objects.get(id_cliente=solicitud.id_cliente.id_cliente)

        domicilio = formularioDomicilio.save(commit=False)
        domicilio.cliente = cliente
        domicilio.save()
        return redirect('estado_civil', id_solicitud)

    return render(request, 'localidad/localidad.html',{'formulario':formularioDomicilio})

