from django import forms
from django.utils.translation import gettext_lazy as _
from .models import *


class DocumentoLegalForm(forms.ModelForm):
    class Meta:
        model = DocumentoLegal
        fields = '__all__'
        exclude = ['id_cliente', 'id_documento']