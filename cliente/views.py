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

        messages.success(request, "Se guardo con exito")
        # return redirect('falta alexander', id_solicitud)
        return redirect('home')

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

        # Recupera un objeto del tipo cliente que coincida con el id_cliente.
        solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
        cliente = Cliente.objects.get(id_cliente=solicitud.id_cliente.id_cliente)

        # Al objeto "cliente" en el atributo "id_estadocivil" se le asigna el objeto "estadocivil" recién creado.
        cliente.id_estadocivil = estadocivil

        # se guarda el objeto en la DB, almacenando los atributos que faltaban
        cliente.save()

        return redirect('crear_actividad_economica', id_solicitud)

    return render(request, 'estado_civil/registrar.html', {'formulario_estadocivil': formulario_estadocivil})


#@login_required
def localidad(request, id_solicitud):

    formularioDomicilio = DomicilioForm(request.POST or None)

    if formularioDomicilio.is_valid():
        solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
        cliente = Cliente.objects.get(id_cliente=solicitud.id_cliente.id_cliente)

        domicilio = formularioDomicilio.save(commit=False)
        domicilio.cliente = cliente
        domicilio.save()
        return redirect('estado_civil', id_solicitud)

    return render(request, 'localidad/localidad.html',{'formulario':formularioDomicilio})

# Metodo para listar los asociados ya aprobados
def asociados(request):
    asociados = Cliente.objects.filter(es_asociado=True)
    return render(request, 'cliente/lista_clientes_asociados.html', {'asociados': asociados})


def aprobado(request, id_cliente):
    solicitud = Solicitud.objects.get(id_cliente=id_cliente)
    solicitud.es_aprobado = True
    solicitud.save()

    return redirect('home')


def rechazado(request, id_cliente):
    solicitud = Solicitud.objects.get(id_cliente=id_cliente)
    solicitud.es_aprobado = False
    solicitud.delete()

    return redirect('home')

# Creacion de PDF para carnet Asociado
def render_pdf_view(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente = id_cliente)
    template_path = 'cliente/Pdf_carnet.html'
    context = {'clientes': cliente}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download:
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display:
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

# Notificacion al correo de incongruencias en datos en la solicitud de Asociado
def send_notificacion_mail(id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    mail = cliente.correo
    welcome_mail = create_mail(
        mail,
        'INFORMACION IMPORTANTE',
        'cliente/NotificarCliente.html',
        {
            'cliente': cliente
        }
    )
    welcome_mail.send(fail_silently=False)

def send_mail(request,id_cliente):
    send_notificacion_mail(id_cliente)

    return  redirect('home')


# Envio de correo al cliente de estado de su solicitud "APROBADA"
def send_aprobacion_mail(id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    mail = cliente.correo
    welcome_mail = create_mail(
        mail,
        'RESOLUCION DE SOLICITUD',
        'cliente/SolicitudAprobada.html',
        {
            'cliente': cliente
        }
    )
    welcome_mail.send(fail_silently=False)

def send_mail1(request,id_cliente):
    send_aprobacion_mail(id_cliente)

    return  redirect('home')

# Envio de correo al cliente de estado de su solicitud "RECHAZADA"
def send_rechazo_mail(id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    mail = cliente.correo
    welcome_mail = create_mail(
        mail,
        'RESOLUCION DE SOLICITUD',
        'cliente/SolicitudRechazada.html',
        {
            'cliente': cliente
        }
    )
    welcome_mail.send(fail_silently=False)

def send_mail2(request,id_cliente):
    send_rechazo_mail(id_cliente)

    return  redirect('home')