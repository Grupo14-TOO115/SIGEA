from .views import *
from django.urls import path, include

urlpatterns2 = [
    path('ver_solicitud_jefatura/<int:id_solicitud>', solicitud, name='ver_solicitud_jefatura'),
    path('consultar_documentos_anexos_jefatura/<int:id_solicitud>', anexo, name='consultar_documentos_anexos_jefatura'),
    path('ver_solicitud/ver_beneficiarios_jefatura/<int:id_solicitud>', beneficiarios, name='ver_beneficiarios_jefatura'),
    path('ver_solicitud/referencia_personal_jefatura/<int:id_solicitud>', referencia, name='referencia_personal_jefatura'),
]

urlpatterns = [
    path('recepcion_solicitudes_validadas', solicitudes_validadas, name='recepcion_solicitudes_validadas'),
    path('recepcion_solicitudes_validadas/', include(urlpatterns2)),

    #envio de e-mial
    path('solicitud-aprobada/<int:id_solicitud>', aprobado, name='solicitud-validada'),
    path('solicitud-rechazada/<int:id_solicitud>', rechazado, name='solicitud-rechazada'),
    path('send/aprobacion/<int:id_cliente>', send_aprobacion_mail, name='send_aprobacion_mail'), #Para envio de email de solicitud Aprobada
    path('send/rechazo/<int:id_cliente>', send_rechazo_mail, name='send_rechazo_mail'), #Para envio de email de solicitud Rechazada
]
