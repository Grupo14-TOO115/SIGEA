from django.urls import path
from .views import *
from django.urls import path, include
# enlaces para mostrar las vistas (URLS)

urlpatterns2 = [
    path('crearActividad/', crear_actividad_economica, name='crear_actividad_economica'),
    path('crearCapacidadEconomica', crear_capacidad_economica, name='crear_capacidad_economica'),
    path('localidad/', localidad, name='localidad'),
    path('estado_civil', crear_estadocivil, name='estado_civil'),
]

urlpatterns = [
    path('crear', crear_cliente, name='crear_cliente'),
    path('solicitud/<int:id_solicitud>/', include(urlpatterns2)),
    path('listaclientes', asociados, name='cliente_list_view'),

    path('listaclientes/decicion/aprobado/<int:id_cliente>', aprobado, name='aprobado'),
    path('listaclientes/decicion/rechazado/<int:id_cliente>', rechazado, name='rechazado'),

    path('pdf/<int:id_cliente>/', render_pdf_view, name='cliente-pdf-view'),
    path('send/mail/<int:id_cliente>', send_mail, name='send_mail')
]
