from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from webApp.views import *
from cliente.views import *


def validarSecretaria(request):
    usuarios = Usuario.objects.all()

    existe = False

    for usua in usuarios:
        if request.user.pk == usua.user.pk:
            existe = True

    if existe and obtenerUsuario(request).es_secretaria:
        return True

    messages.warning(request, "Este apartado es solo para secretaria")

    return False


@login_required
def solicitudes(request):

    if not validarSecretaria(request):
        return redirect('home')

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
@login_required
def revisado(request, id_solicitud):

    if not validarSecretaria(request):
        return redirect('home')

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
@login_required
def validado(request, id_solicitud):

    if not validarSecretaria(request):
        return redirect('home')

    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    solicitud.es_revisado = True
    solicitud.es_validado = True
    solicitud.es_aprobado = False
    solicitud.save()
    messages.success(request, "La solicitud fue enviada a Jefatura exitosamente ")

    return redirect('recepcion_solicitudes')


# SOLICITUD REVISADA Y VALIDADA
@login_required
def validado2(request, id_solicitud):

    if not validarSecretaria(request):
        return redirect('home')

    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    solicitud.es_revisado = True
    solicitud.es_validado = True
    solicitud.es_aprobado = False
    solicitud.save()
    messages.success(request, "La solicitud fue enviada a Jefatura exitosamente ")

    return redirect('solicitudes_espera')

@login_required
def solicitudes_espera(request):  # Este es para secretaría, solicitudes notificadas para correciones

    if not validarSecretaria(request):
        return redirect('home')

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
@login_required
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


@login_required
def solicitud(request, id_solicitud):

    if not validarSecretaria(request):
        return redirect('home')

    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    domicilio = Domicilio.objects.get(cliente=solicitud.id_cliente.id_cliente)
    beneficiario = Beneficiario.objects.filter(solicitud=id_solicitud)
    return render(request, 'ver_solicitud_secretaria/solicitudes.html',
                  {'solicitud': solicitud, 'domicilio': domicilio, 'beneficiario': beneficiario})


@login_required
def solicitud_espera(request, id_solicitud):

    if not validarSecretaria(request):
        return redirect('home')

    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    domicilio = Domicilio.objects.get(cliente=solicitud.id_cliente.id_cliente)
    beneficiario = Beneficiario.objects.filter(solicitud=id_solicitud)
    return render(request, 'ver_solicitud_secretaria/solicitudes_espera.html',
                  {'solicitud': solicitud, 'domicilio': domicilio, 'beneficiario': beneficiario})


@login_required
def beneficiarios(request, id_solicitud):

    if not validarSecretaria(request):
        return redirect('home')

    beneficiarios = Beneficiario.objects.filter(solicitud=id_solicitud)
    return render(request, 'ver_solicitud_secretaria/ver_beneficiarios.html', {'beneficiarios': beneficiarios, 'id_solicitud': id_solicitud})


@login_required
def referencia(request, id_solicitud):

    if not validarSecretaria(request):
        return redirect('home')

    referencia = ReferenciaPersonal.objects.filter(solicitud=id_solicitud)
    return render(request, 'ver_solicitud_secretaria/referencia_personal.html', {'referencia': referencia, 'id_solicitud': id_solicitud})


@login_required
def anexo(request, id_solicitud):

    if not validarSecretaria(request):
        return redirect('home')

    anexo = Solicitud.objects.get(id_solicitud=id_solicitud)
    return render(request, 'consultar_documentos_anexos_secretaria/index.html', {'anexo': anexo, 'id_solicitud': id_solicitud})
