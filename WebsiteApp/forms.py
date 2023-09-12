from django import forms
from .models import Evento


# Formulario eventos

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['fecha', 'lugar', 'pais', 'estado', 'boton_compra']
        