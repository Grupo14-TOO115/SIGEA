# Generated by Django 4.1.2 on 2022-11-03 02:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('es_secretaria', models.BooleanField(default=False, help_text='Indica si es secretaria')),
                ('es_jefatura', models.BooleanField(default=False, help_text='Indica si es jefatura')),
                ('es_cajera', models.BooleanField(default=False, help_text='Indica si es cajera')),
                ('es_agente', models.BooleanField(default=False, help_text='Indica si es agente')),
                ('es_asociado', models.BooleanField(default=False, help_text='Indica si es asociado')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
