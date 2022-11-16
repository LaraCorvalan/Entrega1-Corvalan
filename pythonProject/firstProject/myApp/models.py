from django.db import models

# Create your models here.
class Libro(models.Model):
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
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    paginas = models.IntegerField()
    sinopsis = models.TextField()
    genero = models.CharField(max_length=40, choices=generos)
    

# class Genero(models.Model):
#     generos = (
#         ('terror', 'terror'),
#         ('romance', 'romance'), 
#         ('drama', 'drama'), 
#         ('comics', 'comics'), 
#         ('ficcion', 'ficcion'), 
#         ('infantil', 'infantil'), 
#         ('historia', 'historia'), 
#         ('juvenil', 'juvenil'), 
#     )
#     nombre = models.CharField(
#         max_length=40,
#         choices=generos
#     )

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField(null = True)
    libros = models.CharField(max_length=100, null = True)
    

class Reseña(models.Model):
    PUNTAJE = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]
    libro= models.CharField(max_length=150, null=False, default='Unknown')
    reseña = models.TextField()
    estrellas = models.IntegerField(choices = PUNTAJE)