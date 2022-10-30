from django.urls import path
from .views import *
from django.urls import path, include

urlpatterns2 = [
    path('documentos_legales', documentosLegales, name='documentos_legales'),
    path('documentos_legales/eliminar/<int:id_documento>', eliminarDocumentoLegal, name='eliminar_documento_legal'),
    path('anexar_foto', anexarFoto, name ='anexo_foto'),
]

urlpatterns = [
    path('<int:id_cliente>/', include(urlpatterns2)),
]
