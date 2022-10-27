from django.shortcuts import render
from cliente.models import Solicitud


# Create your views here.


def home(request):
    return render(request, 'paginas/home.html')


def documentos_anexos(request):
    return render(request, 'consultar_documentos_anexos/consultar.html')


def solicitudes(request):
    solicitudes = Solicitud.objects.all()
    return render(request, 'recepcion_solicitudes/index.html', {'solicitudes': solicitudes})


def solicitudes_revisadas(request):
    solicitudes = Solicitud.objects.all()
    return render(request, 'recepcion_solicitudes_revisadas/index.html', {'solicitudes': solicitudes})


def solicitud(request, id_solicitud):
    solicitud = Solicitud.objects.get(id_solicitud=id_solicitud)
    return render(request, 'ver_solicitud/index.html', {'solicitud': solicitud})
