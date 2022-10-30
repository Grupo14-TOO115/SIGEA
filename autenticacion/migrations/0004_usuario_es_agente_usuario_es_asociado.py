# Generated by Django 4.1.2 on 2022-10-27 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0003_usuario_es_cajera'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='es_agente',
            field=models.BooleanField(default=False, help_text='Indica si es agente'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='es_asociado',
            field=models.BooleanField(default=False, help_text='Indica si es asociado'),
        ),
    ]