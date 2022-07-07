from django.db import models

# Create your models here.

class Despacho(models.Model):
    nroorden = models.CharField(max_length=6, primary_key=True, verbose_name='Nro Orden')
    destinatario = models.CharField(max_length=25, verbose_name='Destinatario')
    direccion = models.CharField(max_length=25, null=True, blank=True, verbose_name='Direccion')
    estado = models.CharField(max_length=25, null=True, blank=True, verbose_name='Estado')

