# Generated by Django 4.1.2 on 2022-10-29 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0005_usuario_es_primeravez'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='es_primeraVez',
        ),
    ]
