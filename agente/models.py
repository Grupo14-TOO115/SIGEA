from django.utils.translation import gettext_lazy as _
from django.db import models
from cliente.models import *

class DocumentoLegal(models.Model):
    id_documento = models.AutoField(primary_key=True, verbose_name="Documento ID")
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=False)
    nombre = models.CharField(max_length=20, null=False, blank=False)
    imagen = models.ImageField(upload_to='fotografias/', null=False)
    
    class Meta:
        db_table='documentos_legales'
        ordering=["id_documento"]

    def __str__(self):
        return self.nombre