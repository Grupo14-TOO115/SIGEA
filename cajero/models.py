from django.db import models
from django.utils.translation import gettext_lazy as _
from cliente.models import *

class SolicitudPago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.PROTECT, null=False, blank=False,default=1)
    pagado = models.BooleanField(null=False, default=False)

    class Meta:
        db_table = 'solicitud_pago'