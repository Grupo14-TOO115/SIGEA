from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from cliente.models import *
from .models import *
from autenticacion.views import registrarUsuario
from xhtml2pdf import pisa
from django.template.loader import get_template


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

def export_pdf(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    template_path = 'prueba.html'
    context = {'cliente': cliente}
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] ='filename="tezst recibo_de_pago.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response