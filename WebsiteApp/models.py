from django.db import models

# Create your models here.

class Evento(models.Model):
    fecha = models.DateField()
    lugar = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    boton_compra = models.URLField(blank=True)

    # def __str__(self):
    #     return f'{self.fecha} - {self.lugar}'python manage.py makemigrations


class Discos(models.Model):
    titulo = models.CharField(max_length=100)
    año_lanzamiento = models.PositiveIntegerField()
    portada = models.ImageField(upload_to='discos/', null=True, blank=True)
    url_compra = models.URLField(blank=True)

    # def __str__(self):
    #     return self.titulo

class Biografia(models.Model):
    nombre = models.CharField(max_length=100)
    instrumento = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='biografia/', null=True, blank=True)

    # def __str__(self):
    #     return self.nombre    


class Shop(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='shop/', null=True, blank=True)
    categoria = models.CharField(max_length=50)
    disponible = models.BooleanField(default=True)

    # def __str__(self):
    #     return self.nombre