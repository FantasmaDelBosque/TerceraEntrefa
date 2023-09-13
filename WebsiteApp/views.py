from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Evento, Discos
from .forms import EventoForm, DiscosForm


# from django.views.generic import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import DeleteView, UpdateView, CreateView
# from .models import Curso, Profesor
# from .forms import CursoFormulario, ProfesorFormulario

# Create your views here.

# def evento(req, fecha, lugar, pais, estado, boton_compra):

#     evento = Evento(fecha=fecha, lugar=lugar, pais=pais, estado=estado, boton_compra=boton_compra)
#     evento.save()

#     return HttpResponse(f"""
#     <p>Fecha: {evento.fecha} Lugar: {evento.lugar} País: {evento.pais} Estado: {evento.estado}  </p>
#     """)
    
# def listar_eventos(req):
#     lista = Evento.objects.all()
#     return render(req, "lista_eventos.html", {"lista_eventos": lista})


def eventos(req):
    return render(req, "eventos.html")

def inicio(req):
    return render(req, "inicio.html")

def discografia(req): 
    return render(req, "discografia.html")

def biografia(req):
    return render(req, "biografia.html")

def shop(req):
    return render(req, "shop.html")

def lista_eventos(request):
    eventos = Evento.objects.all()  # pylint: disable=no-member
    return render(request, 'lista_eventos.html', {'eventos': eventos})

def lista_disco(request):
    disco = Evento.objects.all()  # pylint: disable=no-member
    return render(request, 'lista_disco.html', {'disco': disco})

# forms

# def agregarEvento(req):

#     print('metho', req.method)
#     print('POST', req.POST)
#     if req.method == 'POST':
#         return render(req, "agregarEvento.html" )
#         pass
#     else:
#         return render(req, "agregarEvento.html" )

# def agregarEvento(req):

#     if req.method == 'POST':
#         # Si la solicitud es POST, procesa los datos del formulario
#         form = EventoForm(req.POST)
#         if form.is_valid():
#             # Si el formulario es válido, guarda el evento en la base de datos
#             form.save()
#             # Redirige a la página de inicio o a donde desees después de guardar
#             return redirect('Inicio')  
#     else:
#         # Si la solicitud no es POST, muestra el formulario en blanco
#         form = EventoForm()
    
#     return render(req, 'agregarEvento.html', {'form': form})




# def agregarEvento(req):
#     if req.method == 'POST':
#         # Si la solicitud es POST, procesa los datos del formulario
#         form = EventoForm(req.POST)
#         if form.is_valid():
#             # Si el formulario es válido, guarda el evento en la base de datos
#             form.save()
#             # Redirige a la página de inicio después de guardar el evento
#             return redirect('inicio')  
#     else:
#         # Si la solicitud no es POST, muestra el formulario en blanco
#         form = EventoForm()
    
#     # Recupera todos los eventos de la base de datos
#     eventos = Evento.objects.all() # pylint: disable=no-member
    
#     # Renderiza el HTML 'lista_eventos' con los eventos
#     return render(req, 'lista_eventos.html', {'eventos': eventos, 'form': form})





def agregarEvento(req):
    if req.method == 'POST':
        # Si la solicitud es POST, procesa los datos del formulario
        form = EventoForm(req.POST)
        if form.is_valid():
            # Si el formulario es válido, guarda el evento en la base de datos
            form.save()
            # Redirige a la página de lista de eventos después de guardar el evento
            return redirect('lista_eventos') 
    else:
        # Si la solicitud no es POST, muestra el formulario en blanco
        form = EventoForm() # pylint: disable=no-member
    
    return render(req, 'agregarEvento.html', {'form': form})



def agregarDisco(req):
    if req.method == 'POST':
        form = DiscosForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_disco')
    else:
        form = DiscosForm() # pylint: disable=no-member
    
    return render(req, 'agregarDisco.html', {'form': form})


