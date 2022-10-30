from django.shortcuts import render, redirect
from .forms import *
from .models import *
from cliente.models import *

def documentosLegales(request, id_cliente):
    form = DocumentoLegalForm(request.POST or None, request.FILES or None)
    cliente = cliente = Cliente.objects.get(id_cliente=id_cliente)

    if form.is_valid():
        docLegal = form.save(commit=False)
        docLegal.id_cliente = cliente
        docLegal.save()
        
    documentosAgregados = listarDocumentosLegalesAgregados(cliente)
    form = DocumentoLegalForm()
    return render(request, 'anexos/anexDocumentoLegales.html', {'formulario': form, 'documentos': documentosAgregados})

def eliminarDocumentoLegal(request, id_cliente, id_documento):
    documento = DocumentoLegal.objects.get(id_documento=id_documento)
    documento.delete()
    return redirect('documentos_legales', id_cliente)

def listarDocumentosLegalesAgregados(cliente):
    documentos = DocumentoLegal.objects.filter(id_cliente=cliente)
    return documentos

def anexarFoto(request, id_cliente):
    formulario = AnexoImagen(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        clienteConfoto = formulario.save(commit=False)
        cliente = Cliente.objects.get(id_cliente=id_cliente)
        cliente.fotografia = clienteConfoto.fotografia
        cliente.save()
        return redirect('home')

    return render(request, 'anexos/fotoAsociado.html', {'form': formulario})