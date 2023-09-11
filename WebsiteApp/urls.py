from django.urls import path
from .views import  inicio, eventos, discografia, biografia

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('eventos/', eventos, name="Eventos"),
    path('discografia/', discografia, name="Discografia"),
    path('biografia/', biografia, name="Biografia")
]
