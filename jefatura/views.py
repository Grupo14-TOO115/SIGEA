from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from webApp.views import *
from cliente.views import *

# SOLICITUD APROBADA POR JEFATURA
def aprobado(request, id_solicitud):
    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    solicitud.es_revisado = True
    solicitud.es_validado = True
    solicitud.es_aprobado = True
    id_cliente = solicitud.id_cliente.id_cliente
    send_aprobacion_mail(id_cliente)
    solicitud.save()
    messages.success(request, "La solicitud fue aprobada. Se notificó por correo al cliente.")
    return redirect('recepcion_solicitudes_validadas')


# SOLICITUD RECHAZADA POR JEFATURA
def rechazado(request, id_solicitud):
    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    solicitud.es_aprobado = False
    # primero envia el correo
    id_cliente = solicitud.id_cliente.id_cliente
    send_rechazo_mail(id_cliente)
    # luego se borra
    solicitud.delete()
    messages.success(request, "La solicitud fue rechazada. Se notificó por correo al cliente.")
    return redirect('recepcion_solicitudes_validadas')


def solicitudes_validadas(request):  # Este es para jefatura
    solicitudes = Solicitud.objects.filter(Q(es_validado=True) & Q(es_revisado=True) & Q(es_aprobado=False))
    return render(request, 'recepcion_solicitudes_validadas/index.html', {'solicitudes': solicitudes})

# Envio de correo al cliente de estado de su solicitud "APROBADA"
def send_aprobacion_mail(id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    mail = cliente.correo
    welcome_mail = create_mail(
        mail,
        'RESOLUCION DE SOLICITUD',
        'envio/SolicitudAprobada.html',
        {
            'cliente': cliente
        }
    )
    welcome_mail.send(fail_silently=False)

# Envio de correo al cliente de estado de su solicitud "RECHAZADA"
def send_rechazo_mail(id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    mail = cliente.correo
    welcome_mail = create_mail(
        mail,
        'RESOLUCION DE SOLICITUD',
        'envio/SolicitudRechazada.html',
        {
            'cliente': cliente
        }
    )
    welcome_mail.send(fail_silently=False)

def solicitud(request, id_solicitud):
    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    domicilio = Domicilio.objects.get(cliente=solicitud.id_cliente.id_cliente)
    beneficiario = Beneficiario.objects.filter(solicitud=id_solicitud)
    return render(request, 'ver_solicitud/index.html',
                  {'solicitud': solicitud, 'domicilio': domicilio, 'beneficiario': beneficiario})

def beneficiarios(request, id_solicitud):
    beneficiarios = Beneficiario.objects.filter(solicitud=id_solicitud)
    return render(request, 'ver_solicitud/ver_beneficiarios.html', {'beneficiarios': beneficiarios, 'id_solicitud': id_solicitud})


def referencia(request, id_solicitud):
    referencia = ReferenciaPersonal.objects.filter(solicitud=id_solicitud)
    return render(request, 'ver_solicitud/referencia_personal.html', {'referencia': referencia, 'id_solicitud': id_solicitud})


def anexo(request, id_solicitud):
    anexo = Solicitud.objects.get(id_solicitud=id_solicitud)
    return render(request, 'consultar_documentos_anexos/index.html', {'anexo': anexo, 'id_solicitud': id_solicitud})
