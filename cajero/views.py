from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from cliente.models import *
from .models import *

def lista_solicitudes_pago(request):
    busqueda = request.POST.get("buscar")
    solicitudes = SolicitudPago.objects.filter(pagado =  False)

    if busqueda:
        solicitudes = SolicitudPago.objects.filter(
            Q(id_cliente__identificacion__icontains = busqueda) |
            Q(id_cliente__nombres__icontains = busqueda) |
            Q(id_cliente__apellidos__icontains = busqueda)
        ).distinct()

    return render(request, 'lista_solicitudes_pago.html', {'solicitudes': solicitudes})

def confirmar_pago(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente = id_cliente)
    cliente.es_asociado = True
    cliente.save()



    solicitudPagada = SolicitudPago.objects.get(id_cliente = cliente)
    solicitudPagada.pagado = True
    solicitudPagada.save()

    return redirect('solicitudes_de_pago')