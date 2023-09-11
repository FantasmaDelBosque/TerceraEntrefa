from django.shortcuts import render
from django.http import HttpResponse, HttpRequest




# from django.views.generic import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import DeleteView, UpdateView, CreateView
# from .models import Curso, Profesor
# from .forms import CursoFormulario, ProfesorFormulario

# Create your views here.


def inicio(req):
    return render(req, "inicio.html")

def eventos(req):
    return render(req, "eventos.html")

def discografia(req): 
    return render(req, "discografia.html")

def biografia(req):
    return render(req, "biografia.html")