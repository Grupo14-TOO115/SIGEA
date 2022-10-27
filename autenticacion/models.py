from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    es_secretaria = models.BooleanField(default=False, help_text='Indica si es secretaria')
    es_jefatura = models.BooleanField(default=False, help_text='Indica si es jefatura')
    es_cajera = models.BooleanField(default=False, help_text='Indica si es cajera')
    es_agente = models.BooleanField(default=False, help_text='Indica si es agente')
    es_asociado = models.BooleanField(default=False, help_text='Indica si es asociado')

    def __str__(self):
        return "El Usuario extendido depende del User: " + self.user.pk.__str__() + " - " + self.user.username

