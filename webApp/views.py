from django.shortcuts import render, redirect
from cliente.models import *
from autenticacion.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def obtnerUsuario(request):
    usuario = Usuario.objects.get(pk=request.user.pk)

    return usuario


def home(request):
    if request.user.pk:
        if obtnerUsuario(request).es_secretaria:
            return redirect('vista_secretaria')

        if obtnerUsuario(request).es_jefatura:
            return redirect('vista_jefatura')

        if obtnerUsuario(request).es_cajera:
            return redirect('vista_cajera')

        if obtnerUsuario(request).es_agente:
            return redirect('vista_agente')

        if obtnerUsuario(request).es_asociado:
            return redirect('vista_asociado')

    return render(request, 'paginas/home.html')


@login_required
def vista_secretaria(request):
    if not obtnerUsuario(request).es_secretaria:
        messages.warning(request, "Este apartado es solo para secretario/a")
        return redirect('home')

    return render(request, 'paginas/secretaria.html')


@login_required
def vista_jefatura(request):
    if not obtnerUsuario(request).es_jefatura:
        messages.warning(request, "Este apartado es solo para jefatura")
        return redirect('home')

    return render(request, 'paginas/jefatura.html')


@login_required
def vista_cajera(request):
    if not obtnerUsuario(request).es_cajera:
        messages.warning(request, "Este apartado es solo para cajero/a")
        return redirect('home')

    return render(request, 'paginas/cajera.html')


@login_required
def vista_agente(request):
    if not obtnerUsuario(request).es_agente:
        messages.warning(request, "Este apartado es solo para un agente")
        return redirect('home')

    return render(request, 'paginas/agente.html')


@login_required
def vista_asociado(request):
    if not obtnerUsuario(request).es_asociado:
        messages.warning(request, "Este apartado es solo para un asociado")
        return redirect('home')

    return render(request, 'paginas/asociado.html')


def documentos_anexos(request):
    return render(request, 'consultar_documentos_anexos/consultar.html')