from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from webApp.views import *
from cliente.views import *
from cajero.models import SolicitudPago


def validarJefatura(request):
    usuarios = Usuario.objects.all()

    existe = False

    for usua in usuarios:
        if request.user.pk == usua.user.pk:
            existe = True

    if existe and obtenerUsuario(request).es_jefatura:
        return True

    messages.warning(request, "Este apartado es solo para jefatura")

    return False


# SOLICITUD APROBADA POR JEFATURA
@login_required
def aprobado(request, id_solicitud):

    if not validarJefatura(request):
        return redirect('home')

    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    solicitud.es_revisado = True
    solicitud.es_validado = True
    solicitud.es_aprobado = True

    id_cliente = solicitud.id_cliente.id_cliente

    send_aprobacion_mail(id_cliente)

    solicitud.save()

    solicitudPago = SolicitudPago()

    solicitudPago.id_cliente = solicitud.id_cliente
    solicitudPago.pagado = False
    solicitudPago.save()

    messages.success(request, "La solicitud fue aprobada. Se notificó por correo al cliente.")
    return redirect('recepcion_solicitudes_validadas')


# SOLICITUD RECHAZADA POR JEFATURA
@login_required
def rechazado(request, id_solicitud):

    if not validarJefatura(request):
        return redirect('home')

    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    solicitud.es_aprobado = False
    # primero envia el correo
    id_cliente = solicitud.id_cliente.id_cliente
    send_rechazo_mail(id_cliente)
    # luego se borra
    solicitud.delete()
    messages.success(request, "La solicitud fue rechazada. Se notificó por correo al cliente.")
    return redirect('recepcion_solicitudes_validadas')


@login_required
def solicitudes_validadas(request):  # Este es para jefatura

    if not validarJefatura(request):
        return redirect('home')

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


@login_required
def solicitud(request, id_solicitud):

    if not validarJefatura(request):
        return redirect('home')

    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    domicilio = Domicilio.objects.get(cliente=solicitud.id_cliente.id_cliente)
    beneficiario = Beneficiario.objects.filter(solicitud=id_solicitud)
    return render(request, 'ver_solicitud/index.html',
                  {'solicitud': solicitud, 'domicilio': domicilio, 'beneficiario': beneficiario})

@login_required
def beneficiarios(request, id_solicitud):

    if not validarJefatura(request):
        return redirect('home')

    beneficiarios = Beneficiario.objects.filter(solicitud=id_solicitud)
    return render(request, 'ver_solicitud/ver_beneficiarios.html', {'beneficiarios': beneficiarios, 'id_solicitud': id_solicitud})


@login_required
def referencia(request, id_solicitud):

    if not validarJefatura(request):
        return redirect('home')

    referencia = ReferenciaPersonal.objects.filter(solicitud=id_solicitud)
    return render(request, 'ver_solicitud/referencia_personal.html', {'referencia': referencia, 'id_solicitud': id_solicitud})


@login_required
def anexo(request, id_solicitud):

    if not validarJefatura(request):
        return redirect('home')

    anexo = Solicitud.objects.get(id_solicitud=id_solicitud)
    return render(request, 'consultar_documentos_anexos/index.html', {'anexo': anexo, 'id_solicitud': id_solicitud})
