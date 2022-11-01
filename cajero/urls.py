from django.urls import path
from .views import *
from django.urls import path

urlpatterns = [
    path('solicitudes', lista_solicitudes_pago, name='solicitudes_de_pago'),
    path('solicitudes/<int:id_cliente>', confirmar_pago, name = 'confirmar_pago'),
    path('export/<int:id_cliente>', export_pdf, name="export-pdf" ),
]