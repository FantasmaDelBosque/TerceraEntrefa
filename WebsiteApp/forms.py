from django import forms
from .models import Evento, Discos, Shop



# Formulario eventos

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['fecha', 'lugar', 'pais', 'estado', 'boton_compra']
             
class DiscosForm(forms.ModelForm):
    class Meta:
        model = Discos
        fields = ['titulo', 'year_lanzamiento', 'portada', 'url_compra']       

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'categoria', 'disponible']
