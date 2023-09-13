from django.urls import path
from .views import  inicio, eventos, discografia, biografia, shop
from . import views 



urlpatterns = [
    path('', inicio, name="Inicio"),
    path('eventos/', eventos, name="Eventos"),
    path('discografia/', discografia, name="Discografia"),
    path('biografia/', biografia, name="Biografia"),
    path('shop/', shop, name="Shop"),
    # Formularios
    path('agregarEvento/',views.agregarEvento, name='agregarEvento'),
    path('lista_eventos/',views.lista_eventos, name='lista_eventos'),
    path('agregarDisco/',views.agregarDisco, name='agregarDisco'),
    path('lista_disco/',views.lista_disco, name='lista_disco'),
]