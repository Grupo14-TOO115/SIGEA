from django.urls import path

import cliente.views
from .views import *

# enlaces para mostrar las vistas (URLS)
# path(para pasar parametros, llamado a las  views, nombre de la url)

urlpatterns = [
    path('', home, name='home'),

    path('secretaria', vista_secretaria, name='vista_secretaria'),

    path('jefatura', vista_jefatura, name='vista_jefatura'),

    path('cajera', vista_cajera, name='vista_cajera'),

    path('agente', vista_agente, name='vista_agente'),

    path('asociado', vista_asociado, name='vista_asociado'),

    path('recepcion_solicitudes', solicitudes, name='recepcion_solicitudes'),
    path('solicitudes_espera', solicitudes_espera, name='solicitudes_espera'),
    path('recepcion_solicitudes_validadas', solicitudes_validadas, name='recepcion_solicitudes_validadas'),
    path('ver_solicitud/<int:id_solicitud>', solicitud, name='ver_solicitud'),
    path('consultar_documentos_anexos/<int:id_solicitud>', anexo, name='consultar_documentos_anexos'),
    path('ver_solicitud/ver_beneficiarios/<int:id_solicitud>', beneficiarios, name='ver_beneficiarios'),
    path('ver_solicitud/referencia_personal/<int:id_solicitud>', referencia, name='referencia_personal'),
    path('ver_solicitud/documentos_legales/<int:id_cliente>', documentoslegales, name='documentos_legales'),

    path('solicitud-revisada/<int:id_solicitud>', revisado, name='solicitud-revisada'),
    path('solicitud-validada/<int:id_solicitud>', validado, name='solicitud-validada'),
    path('solicitud-Validada/<int:id_solicitud>', validado2, name='solicitud-Validada'),
    path('solicitud-aprobada/<int:id_solicitud>', aprobado, name='solicitud-validada'),
    path('solicitud-rechazada/<int:id_solicitud>', rechazado, name='solicitud-rechazada'),
]
