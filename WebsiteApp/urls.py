from django.urls import path
from .views import  inicio, eventos, discografia, biografia

urlpatterns = [
    path('', inicio),
    path('eventos/', eventos),
    path('discografia/', discografia),
    path('biografia/', biografia)
]
