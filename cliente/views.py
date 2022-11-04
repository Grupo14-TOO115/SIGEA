from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from .models import *


# Create your views here.

def crear_cliente(request):
    # se almacena un formulario del modelo cliente (con datos or vacio)
    formulario = ClienteForm(request.POST or None, request.FILES or None)

    # si es el formulario es valido ...
    if formulario.is_valid():
        # al guardar el formulario, se guarda el objeto en la DB y en la variable cliente
        cliente = formulario.save()

        # se crea un objeto "solicitud"
        solicitud = Solicitud()

        # se le asigna el cliente a la solicitud
        solicitud.id_cliente = cliente

        # AQUI SE ALMACENACENA EL OBJETO SOLICITUD "FALTA id_actividadEconomica"
        solicitud.save()

        # SE DEBE HACER UN PROCESO SIMILAR PARA ALMACENAR LO DEMAS
        # MODIFICAR EL MODELO DE SOLICTUD YA QUE FALTAN VARIAS LLAVES FORANEAS

        # messages.success(request, "Se envio la solicitud exitosamente!")
        return redirect('localidad', solicitud.id_solicitud)

    # si el formulario no es valido renderiza la pagina, envia a la pagina el request y el formulario
    return render(request, 'cliente/crear.html', {'formulario': formulario})


@login_required
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/index.html', {'clientes': clientes})


def crear_capacidad_economica(request, id_solicitud):
    formulario_CapacidadEconomica = CapacidadEconoForm(request.POST or None, request.FILES or None)

    # si es el formulario es valido ...

    if formulario_CapacidadEconomica.is_valid():
        solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
        actividadEconomica = ActividadEconomica.objects.get(id_actividadEconomica=solicitud.id_actividadEconomica.id_actividadEconomica )

        capacidadEconomica = formulario_CapacidadEconomica.save(commit=False)
        capacidadEconomica.total= capacidadEconomica.salario + capacidadEconomica.otrosIngresos - capacidadEconomica.gastosAFP - capacidadEconomica.gastosISSS - capacidadEconomica.gastosPersonales - capacidadEconomica.gastosEducacion - capacidadEconomica.prestamos

        # se le asigna una capacidad economica a la actividad economica
        actividadEconomica.id_capacidadEconomica = capacidadEconomica
        capacidadEconomica.save()
        actividadEconomica.save()

        # messages.success(request, "Se guardo con exito")
        return redirect('gestionarReferencias',id_solicitud)

    # si el formulario no es valido renderiza la pagina, envia a la pagina el request y el formulario
    return render(request, 'capacidadEconomica/crear.html', {'formulario_CapacidadEconomica': formulario_CapacidadEconomica})


def crear_actividad_economica(request, id_solicitud):
    formulario_ActividadEconomica = ActEconoForm(request.POST or None)

    # si es el formulario es valido ...

    if formulario_ActividadEconomica.is_valid():

        # al guardar el formulario, se guarda el objeto en la DB y en la variable cliente

        actEconomica = formulario_ActividadEconomica.save()

        # se crea un objeto "solicitud"
        solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)

        # se le asigna actividad economica a la solicitud
        solicitud.id_actividadEconomica = actEconomica
        solicitud.save()

        # messages.success(request, "Se envio la solicitud exitosamente!")
        return redirect('crear_capacidad_economica', solicitud.id_solicitud)

        # si el formulario no es valido renderiza la pagina, envia a la pagina el request y el formulario
    return render(request, 'actividadEconomica/crear.html', {'formulario_ActividadEconomica': formulario_ActividadEconomica})


def crear_estadocivil(request, id_solicitud):
    formulario_estadocivil = EstadocivilForm(request.POST or None)

    if formulario_estadocivil.is_valid():
        estadocivil = formulario_estadocivil.save()

        # Al objeto "cliente" en el atributo "id_estadocivil" se le asigna el objeto "estadocivil" recién creado.
        cliente = getClientePorIdDeSolicitud(id_solicitud)
        cliente.id_estadocivil = estadocivil

        # se guarda el objeto en la DB, almacenando los atributos que faltaban
        cliente.save()

        return redirect('crear_actividad_economica', id_solicitud)

    return render(request, 'estado_civil/registrar.html', {'formulario_estadocivil': formulario_estadocivil})


def localidad(request, id_solicitud):

    formularioDomicilio = DomicilioForm(request.POST or None)

    if formularioDomicilio.is_valid():
        domicilio = formularioDomicilio.save(commit=False)
        domicilio.cliente = getClientePorIdDeSolicitud(id_solicitud)
        domicilio.save()
        return redirect('estado_civil', id_solicitud)

    return render(request, 'localidad/localidad.html',{'formulario':formularioDomicilio})
#-----------------------------CRUD GESTIONAR REFERENCIAS---------------------------------------------------------------
def GestionarReferencias(request,id_solicitud):
    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    referencias=solicitud.referenciapersonal_set.filter(solicitud=solicitud)
    contador=referencias.count()
    return render(request,'referenciaPersonal/index.html',{'referencias': referencias,'id_solicitud':id_solicitud,'contador':contador})

def ValidarReferencias(request,id_solicitud):
    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    referencias=solicitud.referenciapersonal_set.filter(solicitud=solicitud)
    contador=referencias.count()
    if contador<=2:
        messages.info(request,'Es necesario agregar al menos 2 referencias')
    return redirect('gestionarReferencias',id_solicitud)



def EditarReferenciaPersonal(request,id_solicitud,id_referencia):
    referencia=ReferenciaPersonal.objects.get(id_referencia=id_referencia)
    formulario=ReferenciaForm(request.POST or None, instance=referencia)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('gestionarReferencias',id_solicitud)
    return render(request, 'referenciaPersonal/editar.html', {'formulario': formulario,'id_solicitud':id_solicitud})

def GuardarReferenciaPersonal(request,id_solicitud):
    formulario=ReferenciaForm(request.POST or None)
    if formulario.is_valid():
        solicitud=Solicitud.objects.get(id_solicitud=id_solicitud)
        referencia=formulario.save(commit=False)
        referencia.solicitud=solicitud
        referencia.save()
        return redirect('gestionarReferencias', id_solicitud)

    return render(request, 'referenciaPersonal/crear.html',{'formulario': formulario,'id_solicitud':id_solicitud})

def EliminarReferenciaPersonal(request, id_solicitud,id_referencia):
    referencia=ReferenciaPersonal.objects.get(id_referencia=id_referencia)
    referencia.delete()
    return redirect('gestionarReferencias',id_solicitud)
#------------------------------------CRUD BENEFICIARIO---------------------------------------------------------------
def GestionarBeneficiarios(request, id_solicitud):
    solicitud=Solicitud.objects.get(id_solicitud=id_solicitud)
    beneficiarios=solicitud.beneficiario_set.filter(solicitud=solicitud)
    contador=beneficiarios.count()
    contadorPorcentaje=0
    for beneficiario in beneficiarios:
        contadorPorcentaje+=beneficiario.porcentaje
    if contadorPorcentaje > 100:
        messages.info(request,'El porcentaje en los beneficiarios ha sido sobrepasado')

    return render(request, 'beneficiario/Index.html', {'beneficiarios':beneficiarios,'id_solicitud':id_solicitud,'contador':contador,'contadorPorcentaje':contadorPorcentaje})

def validarBeneficiario(request, id_solicitud):
    solicitud=Solicitud.objects.get(id_solicitud=id_solicitud)
    beneficiarios=solicitud.beneficiario_set.filter(solicitud=solicitud)
    contador=beneficiarios.count()
    if contador < 1:
        messages.info(request, 'Es necesario agregar al menos 1 Beneficiario')
    return redirect('gestionarBeneficiarios',id_solicitud)

def GuardarBeneficiario(request, id_solicitud):
    formulario=BeneficiarioForm(request.POST or None)
    if formulario.is_valid():
        solicitud=Solicitud.objects.get(id_solicitud=id_solicitud)
        beneficiario=formulario.save(commit=False)
        beneficiario.solicitud=solicitud
        beneficiario.save()
        return redirect('gestionarBeneficiarios',id_solicitud)
    return render(request,'beneficiario/crear.html',{'formulario':formulario, 'id_solicitud':id_solicitud})

def EditarBeneficiario(request,id_solicitud, id_beneficiario):
    beneficiario=Beneficiario.objects.get(id_beneficiario=id_beneficiario)
    formulario=BeneficiarioForm(request.POST or None, instance=beneficiario)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('gestionarBeneficiarios',id_solicitud )
    return render(request, 'beneficiario/editar.html', {'formulario': formulario, 'id_solicitud':id_solicitud})

def EliminarBeneficiario(request,id_solicitud,id_beneficiario):
    beneficiario=Beneficiario.objects.get(id_beneficiario=id_beneficiario)
    beneficiario.delete()
    return redirect('gestionarBeneficiarios',id_solicitud)


def getClientePorIdDeSolicitud(id_solicitud):
    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    cliente = Cliente.objects.get(id_cliente=solicitud.id_cliente.id_cliente)
    return cliente

# Creacion de un email, en general
def create_mail(email, subject, template_path, context):

    template = get_template(template_path)
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject=subject,
        body='',
        from_email=settings.EMAIL_HOST_USER,
        to=[
            email
        ],

    )
    mail.attach_alternative(content, 'text/html')
    return mail

def send_usuario_mail(id_cliente, username, password):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    mail = cliente.correo
    welcome_mail = create_mail(
        mail,
        'CREDENCIALES DE USUARIO',
        'cliente/EnvioCredenciales.html',
        {
            'cliente': cliente,
            'username': username,
            'contraseña': password,
        }
    )
    welcome_mail.send(fail_silently=False)


def GuardarAnexo(request, id_solicitud):

    formulario = AnexoForm(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        anexo = formulario.save()

        solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)

        solicitud.id_anexo = anexo

        solicitud.save()

        messages.success(request, "Se envio la solicitud correctamente")

        return redirect('home')

    return render(request,'anexo/crear.html',{'formulario':formulario})

#generar recibo de pago
def export_recibo_pdf(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    template_path = 'recibo/recibo_pdf.html'
    context = {'cliente': cliente, 'fecha': date.today()}
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] ='filename="recibo_de_pago.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
