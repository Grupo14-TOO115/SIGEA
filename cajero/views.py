from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from cliente.models import *
from .models import *
from autenticacion.views import registrarUsuario
from webApp.views import *


def validarCajero(request):
    usuarios = Usuario.objects.all()

    existe = False

    for usua in usuarios:
        if request.user.pk == usua.user.pk:
            existe = True

    if existe and obtenerUsuario(request).es_cajera:
        return True

    messages.warning(request, "Este apartado es solo para cajero")

    return False


@login_required
def lista_solicitudes_pago(request):

    if not validarCajero(request):
        return redirect('home')

    busqueda = request.POST.get("buscar")
    solicitudes = SolicitudPago.objects.filter(pagado=False)

    if busqueda:
        solicitudes = SolicitudPago.objects.filter(
            Q(pagado=False) & (
            Q(id_cliente__identificacion__icontains=busqueda) |
            Q(id_cliente__nombres__icontains=busqueda) |
            Q(id_cliente__apellidos__icontains=busqueda))
        ).distinct()

    return render(request, 'lista_solicitudes_pago.html', {'solicitudes': solicitudes})


@login_required
def confirmar_pago(request, id_cliente):

    if not validarCajero(request):
        return redirect('home')

    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.es_asociado = True
    cliente.save()

    solicitudPagada = SolicitudPago.objects.get(id_cliente = cliente)
    solicitudPagada.pagado = True
    solicitudPagada.save()

    # se le crea un usuario
    registrarUsuario(cliente.id_cliente)

    return redirect('solicitudes_de_pago')