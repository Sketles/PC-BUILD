from django import forms
from django.forms import ModelForm
from .models import Despacho

class VehiculoForm(ModelForm):
    class Meta:
        model = Despacho
        fields = ['nroorden', 'destinatario', 'direccion', 'estado']