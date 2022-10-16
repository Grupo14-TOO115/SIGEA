from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

'''
# transportista
@login_required
def clientes(request):
    cliente = Cliente.objects.filter(id_usuario=request.user.id)
    return render(request, 'cliente/index.html', {'cliente': transportistas})'''

def crear_cliente(request):
    formulario = ClienteForm(request.POST or None)

    if formulario.is_valid():
        formulario.save()

        messages.success(request, "Se agrego el cliente exitosamente!")
        return redirect('home')

    return render(request, 'cliente/crear.html', {'formulario': formulario})

'''
@login_required
def editar_tr(request, id):
    transportista = Transportista.objects.get(id_transportista=id)
    formulario = TransportistaForm2(request.POST or None, instance=transportista)
    if formulario.is_valid() and request.POST:
        formulario.save()
        messages.success(request, "Se han almacenado las modificaciones exitosamente!")
        return redirect('cliente')
    return render(request, 'cliente/editar.html', {'formulario': formulario})


@login_required
def eliminar_tr(request, id):
    if Informe.objects.filter(id_transportista=id):
        messages.error(request, "Este transportista esta ligado a un informe por lo que no se puede eliminar")
    else:
        transportista = Transportista.objects.get(id_transportista=id)
        temp = transportista.identificacion
        transportista.delete()
        messages.success(request, "Se ha eliminado el transportista con identificacion: " + temp)

    return redirect('cliente')'''
