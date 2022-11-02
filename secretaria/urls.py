from django.urls import path
from .views import *
from django.urls import path, include

urlpatterns = [
    path('recepcion_solicitudes', solicitudes, name='recepcion_solicitudes'),
    path('solicitudes_espera', solicitudes_espera, name='solicitudes_espera'),

    path('ver_solicitud_secretaria/<int:id_solicitud>', solicitud, name='ver_solicitud_secretaria'),
    path('ver_solicitud_espera_secretaria/<int:id_solicitud>', solicitud_espera, name='ver_solicitud_espera_secretaria'),
    path('consultar_documentos_anexos_secretaria/<int:id_solicitud>', anexo, name='consultar_documentos_anexos_secretaria'),
    path('ver_solicitud/ver_beneficiarios_secretaria/<int:id_solicitud>', beneficiarios, name='ver_beneficiarios_secretaria'),
    path('ver_solicitud/referencia_personal_secretaria/<int:id_solicitud>', referencia, name='referencia_personal_secretaria'),

     #acciones con correos
    path('solicitud-revisada/<int:id_solicitud>', revisado, name='solicitud-revisada'),
    path('solicitud-validada/<int:id_solicitud>', validado, name='solicitud-validada'),
    path('solicitud-Validada/<int:id_solicitud>', validado2, name='solicitud-Validada'),
    path('send/notificacion/<int:id_cliente>', send_notificacion_mail, name='send_notificacion_mail'),
]