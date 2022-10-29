from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from cliente.models import *
from .models import *
from autenticacion.views import registrarUsuario


def lista_solicitudes_pago(request):
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


def confirmar_pago(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.es_asociado = True
    cliente.save()

    solicitudPagada = SolicitudPago.objects.get(id_cliente = cliente)
    solicitudPagada.pagado = True
    solicitudPagada.save()

    # se le crea un usuario
    registrarUsuario(cliente.id_cliente)

    return redirect('solicitudes_de_pago')