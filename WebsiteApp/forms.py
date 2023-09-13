from django import forms
from .models import Evento, Discos



# Formulario eventos

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['fecha', 'lugar', 'pais', 'estado', 'boton_compra']
        
        
class DiscosForm(forms.ModelForm):
    class Meta:
        model = Discos
        fields = ['titulo', 'año_lanzamiento', 'portada', 'url_compra']       