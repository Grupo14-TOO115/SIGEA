from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import *


class UserCreationFormExtended(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationFormExtended, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class DateInput(forms.DateInput):
    input_type = 'date'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        exclude = ['es_asociado','id_estadocivil']
        widgets = {
            'fecha_nacimiento': DateInput(attrs={'class': 'form-control'}),
        }



#FORMULARIO PARA LA ACTIVIDAD ECONOMICA
class ActEconoForm(forms.ModelForm):
    class Meta:
        model = ActividadEconomica
        fields = ['id_profesion','lugarTrabajo','telefono']

        widgets = {
            'id_profesion': forms.Select(choices=Profesion.objects.all(),attrs={"class": "form-control"}),
            'lugarTrabajo': forms.TextInput(attrs={"class": "form-control"}),

        }


#FORMULARIO PARA LA CAPACIDAD ECONOMICA
class CapacidadEconoForm(forms.ModelForm):

    class Meta:
        model = CapacidadEconomica
        fields = ['salario', 'gastosAFP', 'gastosISSS', 'gastosPersonales', 'prestamos', 'gastosEducacion','otrosIngresos']

        widgets = {
            'salario' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'gastosAFP': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'gastosISSS': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'gastosPersonales': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'gastosEducacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'prestamos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'otrosIngresos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),

        }



class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'


class EstadocivilForm(forms.ModelForm):

    class Meta:
        model = estado_civil
        fields = '__all__'
        widgets = {

        }

class DomicilioForm(forms.ModelForm):
    class Meta:
        model= Domicilio
        fields='__all__'
        exclude = ['cliente']
