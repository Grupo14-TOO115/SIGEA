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


#@login_required
def vista_secretaria(request):
    # if not obtenerUsuario(request).es_secretaria:
    #     messages.warning(request, "Este apartado es solo para secretario/a")
    #     return redirect('home')

    return render(request, 'paginas/secretaria.html')


#@login_required
def vista_jefatura(request):
    # if not obtenerUsuario(request).es_jefatura:
    #     messages.warning(request, "Este apartado es solo para jefatura")
    #     return redirect('home')

    return render(request, 'paginas/jefatura.html')


@login_required
def vista_cajera(request):
    if not obtenerUsuario(request).es_cajera:
        messages.warning(request, "Este apartado es solo para cajero/a")
        return redirect('home')

    return render(request, 'paginas/cajera.html')


@login_required
def vista_asociado(request):
    if not obtenerUsuario(request).es_asociado:
        messages.warning(request, "Este apartado es solo para un asociado")
        return redirect('home')

    return render(request, 'paginas/asociado.html')