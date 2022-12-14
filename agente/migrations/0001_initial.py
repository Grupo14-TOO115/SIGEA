# Generated by Django 4.1.3 on 2022-11-03 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cliente", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DocumentoLegal",
            fields=[
                (
                    "id_documento",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Documento ID"
                    ),
                ),
                ("nombre", models.CharField(max_length=20)),
                ("imagen", models.ImageField(upload_to="fotografias/")),
                (
                    "id_cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="cliente.cliente",
                    ),
                ),
            ],
            options={
                "db_table": "documentos_legales",
                "ordering": ["id_documento"],
            },
        ),
    ]
