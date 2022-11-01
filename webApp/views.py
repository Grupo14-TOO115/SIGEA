from django.shortcuts import render, redirect
from cliente.models import *
from autenticacion.models import *
from agente.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cliente.views import send_notificacion_mail, send_aprobacion_mail, send_rechazo_mail
from django.db.models import Q
from django.views.generic import TemplateView


# Create your views here.


def obtenerUsuario(request):
    usuario = Usuario.objects.get(user=request.user.pk)

    return usuario


def home(request):
    if request.user.pk:
        if obtenerUsuario(request).es_secretaria:
            return redirect('vista_secretaria')

        if obtenerUsuario(request).es_jefatura:
            return redirect('vista_jefatura')

        if obtenerUsuario(request).es_cajera:
            return redirect('vista_cajera')

        if obtenerUsuario(request).es_agente:
            return redirect('vista_agente')

        if obtenerUsuario(request).es_asociado:
            return redirect('vista_asociado')

    return render(request, 'paginas/home.html')


@login_required
def vista_secretaria(request):
    if not obtenerUsuario(request).es_secretaria:
        messages.warning(request, "Este apartado es solo para secretario/a")
        return redirect('home')

    return render(request, 'paginas/secretaria.html')


@login_required
def vista_jefatura(request):
    if not obtenerUsuario(request).es_jefatura:
        messages.warning(request, "Este apartado es solo para jefatura")
        return redirect('home')

    return render(request, 'paginas/jefatura.html')


@login_required
def vista_cajera(request):
    if not obtenerUsuario(request).es_cajera:
        messages.warning(request, "Este apartado es solo para cajero/a")
        return redirect('home')

    return render(request, 'paginas/cajera.html')


@login_required
def vista_agente(request):
    if not obtenerUsuario(request).es_agente:
        messages.warning(request, "Este apartado es solo para un agente")
        return redirect('home')

    return render(request, 'paginas/agente.html')


@login_required
def vista_asociado(request):
    if not obtenerUsuario(request).es_asociado:
        messages.warning(request, "Este apartado es solo para un asociado")
        return redirect('home')

    return render(request, 'paginas/asociado.html')


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


def solicitudes_espera(request):  # Este es para secretaría, solicitudes notificadas para correciones
    solicitudes = Solicitud.objects.filter(Q(es_revisado=True) & Q(es_validado=False) & Q(es_aprobado=False))
    return render(request, 'solicitudes_espera/index.html', {'solicitudes': solicitudes})


def solicitudes_validadas(request):  # Este es para jefatura
    solicitudes = Solicitud.objects.filter(Q(es_validado=True) & Q(es_revisado=True) & Q(es_aprobado=False))
    return render(request, 'recepcion_solicitudes_validadas/index.html', {'solicitudes': solicitudes})


def solicitudes(request):  # Este es para secretaría
    solicitudes = Solicitud.objects.filter(Q(es_revisado=False) & Q(es_validado=False) & Q(es_aprobado=False))
    return render(request, 'recepcion_solicitudes/index.html', {'solicitudes': solicitudes})


def solicitud(request, id_solicitud):
    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    domicilio = Domicilio.objects.get(cliente=solicitud.id_cliente.id_cliente)
    beneficiario = Beneficiario.objects.filter(solicitud=id_solicitud)
    return render(request, 'ver_solicitud/index.html',
                  {'solicitud': solicitud, 'domicilio': domicilio, 'beneficiario': beneficiario})


def beneficiarios(request, id_solicitud):  # Este es para secretaría
    beneficiarios = Beneficiario.objects.filter(solicitud=id_solicitud)
    return render(request, 'ver_solicitud/ver_beneficiarios.html', {'beneficiarios': beneficiarios})


def referencia(request, id_solicitud):  # Este es para secretaría
    referencia = ReferenciaPersonal.objects.filter(solicitud=id_solicitud)
    return render(request, 'ver_solicitud/referencia_personal.html', {'referencia': referencia})


def anexo(request, id_solicitud):
    anexo = Solicitud.objects.get(id_solicitud=id_solicitud)
    return render(request, 'consultar_documentos_anexos/index.html', {'anexo': anexo})


def documentoslegales(request, id_cliente):
    documentoslegales = DocumentoLegal.objects.filter(id_cliente=id_cliente)
    return render(request, 'ver_solicitud/documentos_legales.html', {'documentoslegales': documentoslegales})
