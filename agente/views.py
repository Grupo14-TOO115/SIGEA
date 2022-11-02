from django.shortcuts import render, redirect
from .forms import *
from .models import *
from cliente.models import *
from django.http import HttpResponse
from .forms import *
from django.template.loader import get_template
from django.db.models import Q
from xhtml2pdf import pisa
from django.contrib import messages
from .models import *
from webApp.views import *

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
    formulario = AnexoImagen(request.POST or None)

    if formulario.is_valid():
        clienteConfoto = formulario.save(commit=False)
        cliente = Cliente.objects.get(id_cliente=id_cliente)
        cliente.fotografia = clienteConfoto.fotografia
        cliente.save()
        messages.success(request, "Se guardo con exito")
        return redirect('vista_agente')


    return render(request, 'anexos/fotoAsociado.html', {'form': formulario})

def generar_carnet(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    template_path = 'Asociados/Pdf_carnet.html'
    context = {'clientes': cliente, 'fecha_expedicion': date.today()}
    
    response = HttpResponse(content_type='application/pdf')
    
    response['Content-Disposition'] ='filename="Carnet Asociado.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

#@login_required
def asociados(request):
    # if not obtenerUsuario(request).es_agente:
    #     messages.warning(request, "Este apartado es solo para un agente")
    #     return redirect('home')
        
    busqueda = request.POST.get("buscar")
    asociados = Cliente.objects.filter(es_asociado=True)

    if busqueda:
        asociados = Cliente.objects.filter(
            Q(es_asociado=True) & (
            Q(identificacion__icontains=busqueda) |
            Q(nombres__icontains=busqueda) |
            Q(apellidos__icontains=busqueda))
        ).distinct()
        
    return render(request, 'Asociados/lista_asociados.html', {'asociados': asociados})