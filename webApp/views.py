from django.shortcuts import render, redirect
from cliente.models import *
from autenticacion.models import *
from agente.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.views.generic import TemplateView


def obtenerUsuario(request):
    usuario = Usuario.objects.get(user=request.user.pk)

    return usuario


def home(request):
    if request.user.pk:
        usuarios = Usuario.objects.all()

        existe = False

        for usua in usuarios:
            if request.user.pk == usua.user.pk:
                existe = True

        if existe:
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
    usuarios = Usuario.objects.all()

    existe = False

    for usua in usuarios:
        if request.user.pk == usua.user.pk:
            existe = True

    if existe and obtenerUsuario(request).es_secretaria:
        return render(request, 'paginas/secretaria.html')

    messages.warning(request, "Este apartado es solo para secretario/a")

    return redirect('home')

@login_required
def vista_jefatura(request):
    usuarios = Usuario.objects.all()

    existe = False

    for usua in usuarios:
        if request.user.pk == usua.user.pk:
            existe = True

    if existe and obtenerUsuario(request).es_jefatura:
        return render(request, 'paginas/jefatura.html')

    messages.warning(request, "Este apartado es solo para jefatura")

    return redirect('home')


@login_required
def vista_cajera(request):
    usuarios = Usuario.objects.all()

    existe = False

    for usua in usuarios:
        if request.user.pk == usua.user.pk:
            existe = True

    if existe and obtenerUsuario(request).es_cajera:
        return render(request, 'paginas/cajera.html')

    messages.warning(request, "Este apartado es solo para cajero/a")

    return redirect('home')


@login_required
def vista_asociado(request):
    usuarios = Usuario.objects.all()

    existe = False

    for usua in usuarios:
        if request.user.pk == usua.user.pk:
            existe = True

    if existe and obtenerUsuario(request).es_asociado:
        return render(request, 'paginas/asociado.html')

    messages.warning(request, "Este apartado es solo para un asociado")
    return redirect('home')


@login_required
def vista_agente(request):
    usuarios = Usuario.objects.all()

    existe = False

    for usua in usuarios:
        if request.user.pk == usua.user.pk:
            existe = True

    if existe and obtenerUsuario(request).es_agente:
        return render(request, 'paginas/agente.html')

    messages.warning(request, "Este apartado es solo para un agente")
    return redirect('home')

def perfilAsociado(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    domicilio=Domicilio.objects.get(cliente=cliente)
    estadoCivil=cliente.id_estadocivil.id_tipoEstadocivil.nombre_tipoEstadocivil
    if estadoCivil == 'casado' or estadoCivil == 'comprometido' or estadoCivil == 'acompañado':
        estadoCivil=True
    else:
        estadoCivil=False
    return render(request,'perfilAsociado/index.html',{'cliente':cliente,'domicilio':domicilio,'estadoCivil':estadoCivil})