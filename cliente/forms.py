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


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('__all__')
