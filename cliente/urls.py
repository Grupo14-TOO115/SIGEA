from django.urls import path
from .views import *
from django.urls import path, include
# enlaces para mostrar las vistas (URLS)

urlpatterns2 = [
    path('crearActividad/', crear_actividad_economica, name='crear_actividad_economica'),
    path('crearCapacidadEconomica', crear_capacidad_economica, name='crear_capacidad_economica'),
    path('localidad/', localidad, name='localidad'),
    path('estado_civil', crear_estadocivil, name='estado_civil'),

    path('gestionarReferencias', GestionarReferencias, name='gestionarReferencias'),
    path('gestionarReferencias/validar', ValidarReferencias, name='validarReferencias'),    
    path('gestionarReferencias/crear', GuardarReferenciaPersonal, name='crearReferencia'),
    path('gestionarReferencias/editar', EditarReferenciaPersonal, name='editarReferencia'),
    path('gestionarReferencias/editar/<int:id_referencia>', EditarReferenciaPersonal, name='editarReferencia'),
    path('gestionarReferencias/eliminar/<int:id_referencia>', EliminarReferenciaPersonal, name='eliminarReferencia'),

    path('gestionarBeneficiarios', GestionarBeneficiarios, name='gestionarBeneficiarios'),
    path('validarBeneficiarios', validarBeneficiario, name='validarBeneficiarios'),
    path('gestionarBeneficiarios/crear', GuardarBeneficiario, name='crearBeneficiario'),
    path('gestionarBeneficiarios/editar', EditarBeneficiario, name='editarBeneficiario'),
    path('gestionarBeneficiarios/editar/<int:id_beneficiario>', EditarBeneficiario, name='editarBeneficiario'),
    path('gestionarBeneficiarios/eliminar/<int:id_beneficiario>', EliminarBeneficiario, name='eliminarBeneficiario'),

    path('guardarAnexos',GuardarAnexo,name='guardarAnexos')
]

urlpatterns = [
    path('crear', crear_cliente, name='crear_cliente'),
    path('clientes', clientes, name='clientes'),
    path('secretario', clientes, name='secretario'),
    path('solicitud/<int:id_solicitud>/', include(urlpatterns2)),
    path('listaclientes', asociados, name='cliente_list_view'),

    path('listaclientes/decicion/aprobado/<int:id_cliente>', aprobado, name='aprobado'),
    path('listaclientes/decicion/rechazado/<int:id_cliente>', rechazado, name='rechazado'),

    path('pdf/<int:id_cliente>/', render_pdf_view, name='cliente-pdf-view'), #Emitir carnet de Cliente Asociado

    path('send/noticificacion/<int:id_cliente>', send_mail, name='send_mail'), #Para envio de email de notificacion de solicitud erronea en datos.
    path('send/aprobacion/<int:id_cliente>', send_mail1, name='send_mail1'), #Para envio de email de solicitud Aprobada
    path('send/rechazo/<int:id_cliente>', send_mail2, name='send_mail2') #Para envio de email de solicitud Rechazada

]
