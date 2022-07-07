# Generated by Django 4.0.5 on 2022-07-07 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('nroorden', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Nro Orden')),
                ('destinatario', models.CharField(max_length=25, verbose_name='Destinatario')),
                ('direccion', models.CharField(blank=True, max_length=25, null=True, verbose_name='Direccion')),
                ('estado', models.CharField(blank=True, max_length=25, null=True, verbose_name='Estado')),
            ],
        ),
    ]