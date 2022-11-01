from django.urls import path
from .views import *
from django.urls import path, include

urlpatterns2 = [
    path('generar_carnet', generar_carnet, name='cliente-pdf-view'),
    path('documentos_legales', documentosLegales, name='documentos_legales'),
    path('documentos_legales/eliminar/<int:id_documento>', eliminarDocumentoLegal, name='eliminar_documento_legal'),
    path('anexar_foto', anexarFoto, name ='anexo_foto'),
]

urlpatterns = [
    path('lista_asociados', asociados, name='cliente_list_view'),
    path('lista_asociados/<int:id_cliente>/', include(urlpatterns2)),
]