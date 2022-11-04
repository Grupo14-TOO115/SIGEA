from django.urls import path
from .views import *
from django.urls import path, include
# enlaces para mostrar las vistas (URLS)

urlpatterns2 = [
    path('crearActividad/', crear_actividad_economica, name='crear_actividad_economica'),
    path('crearCapacidadEconomica', crear_capacidad_economica, name='crear_capacidad_economica'),
    path('localidad/', localidad, name='localidad'),
    path('estado_civil', crear_estadocivil, name='estado_civil'),

    # editar solicitud
    path('editar_cliente', editar_cliente, name='editar_cliente'),
    path('editar_localidad', editar_localidad, name='editar_localidad'),
    path('editar_actividad_economica', editar_actividad_economica, name='editar_actividad_economica'),
    path('editar_capacidad_economica', editar_capacidad_economica, name='editar_capacidad_economica'),
    path('editarAnexo',editarAnexo,name='editarAnexo'),

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

     path('export/<int:id_cliente>', export_recibo_pdf, name="export-pdf" ),
]
