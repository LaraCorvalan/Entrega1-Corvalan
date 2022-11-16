from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    paginas = models.IntegerField()
    sinopsis = models.TextField()
    genero = models.CharField(max_length=40)
    def __str__(self) -> str:
        return f"Titulo: {self.titulo} - autor: {self.autor} "

class Genero(models.Model):
    generos = (
        ('terror', 'terror'),
        ('romance', 'romance'), 
        ('drama', 'drama'), 
        ('comics', 'comics'), 
        ('ficcion', 'ficcion'), 
        ('infantil', 'infantil'), 
        ('historia', 'historia'), 
        ('juvenil', 'juvenil'), 
    )
    nombre = models.CharField(
        max_length=40,
        choices=generos
    )

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()
    libros = models.CharField(max_length=100)
    