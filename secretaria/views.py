from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from webApp.views import *
from cliente.views import *

def solicitudes(request):
    busqueda = request.POST.get("buscar")
    solicitudes = Solicitud.objects.filter(Q(es_revisado=False) & Q(es_validado=False) & Q(es_aprobado=False))

    if busqueda:
        solicitudes = Solicitud.objects.filter(
            Q(es_revisado=False) & Q(es_validado=False) & Q(es_aprobado=False) & (
            Q(id_cliente__identificacion__icontains=busqueda) |
            Q(id_cliente__nombres__icontains=busqueda) |
            Q(id_cliente__apellidos__icontains=busqueda))
        ).distinct()
    
    return render(request, 'recepcion_solicitudes/index.html', {'solicitudes': solicitudes})

# SOLICITUD NO VALIDADA, EN ESPERA, NOTIFICADA AL CLIENTE
def revisado(request, id_solicitud):
    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    solicitud.es_revisado = True
    solicitud.es_validado = False
    solicitud.es_aprobado = False
    id_cliente = solicitud.id_cliente.id_cliente
    send_notificacion_mail(id_cliente)
    solicitud.save()
    messages.success(request, "Se envió notificación al cliente mediante correo.")
    return redirect('recepcion_solicitudes')


# SOLICITUD REVISADA Y VALIDADA
def validado(request, id_solicitud):
    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    solicitud.es_revisado = True
    solicitud.es_validado = True
    solicitud.es_aprobado = False
    solicitud.save()
    messages.success(request, "La solicitud fue enviada a Jefatura exitosamente ")

    return redirect('recepcion_solicitudes')


# SOLICITUD REVISADA Y VALIDADA
def validado2(request, id_solicitud):
    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    solicitud.es_revisado = True
    solicitud.es_validado = True
    solicitud.es_aprobado = False
    solicitud.save()
    messages.success(request, "La solicitud fue enviada a Jefatura exitosamente ")

    return redirect('solicitudes_espera')

def solicitudes_espera(request):  # Este es para secretaría, solicitudes notificadas para correciones
    busqueda = request.POST.get("buscar")
    solicitudes = Solicitud.objects.filter(Q(es_revisado=True) & Q(es_validado=False) & Q(es_aprobado=False))

    if busqueda:
        solicitudes = Solicitud.objects.filter(
            Q(es_revisado=True) & Q(es_validado=False) & Q(es_aprobado=False) & (
            Q(id_cliente__identificacion__icontains=busqueda) |
            Q(id_cliente__nombres__icontains=busqueda) |
            Q(id_cliente__apellidos__icontains=busqueda))
        ).distinct()
        
    return render(request, 'solicitudes_espera/index.html', {'solicitudes': solicitudes})

# Notificacion al correo de incongruencias en datos en la solicitud de Asociado
def send_notificacion_mail(id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    mail = cliente.correo
    welcome_mail = create_mail(
        mail,
        'INFORMACION IMPORTANTE',
        'notificar/NotificarCliente.html',
        {
            'cliente': cliente
        }
    )
    welcome_mail.send(fail_silently=False)

def solicitud(request, id_solicitud):
    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    domicilio = Domicilio.objects.get(cliente=solicitud.id_cliente.id_cliente)
    beneficiario = Beneficiario.objects.filter(solicitud=id_solicitud)
    return render(request, 'ver_solicitud_secretaria/solicitudes.html',
                  {'solicitud': solicitud, 'domicilio': domicilio, 'beneficiario': beneficiario})

def solicitud_espera(request, id_solicitud):
    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    domicilio = Domicilio.objects.get(cliente=solicitud.id_cliente.id_cliente)
    beneficiario = Beneficiario.objects.filter(solicitud=id_solicitud)
    return render(request, 'ver_solicitud_secretaria/solicitudes_espera.html',
                  {'solicitud': solicitud, 'domicilio': domicilio, 'beneficiario': beneficiario})

def beneficiarios(request, id_solicitud):
    beneficiarios = Beneficiario.objects.filter(solicitud=id_solicitud)
    return render(request, 'ver_solicitud_secretaria/ver_beneficiarios.html', {'beneficiarios': beneficiarios, 'id_solicitud': id_solicitud})


def referencia(request, id_solicitud):
    referencia = ReferenciaPersonal.objects.filter(solicitud=id_solicitud)
    return render(request, 'ver_solicitud_secretaria/referencia_personal.html', {'referencia': referencia, 'id_solicitud': id_solicitud})

def anexo(request, id_solicitud):
    anexo = Solicitud.objects.get(id_solicitud=id_solicitud)
    return render(request, 'consultar_documentos_anexos_secretaria/index.html', {'anexo': anexo, 'id_solicitud': id_solicitud})
