from django import forms

class FormLibros(forms.Form):
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
    titulo = forms.CharField(max_length=100)
    autor = forms.CharField(max_length=100)
    fecha_publicacion = forms.DateField()
    paginas = forms.IntegerField()
    sinopsis = forms.CharField(widget=forms.Textarea)
    genero = forms.ChoiceField(choices=generos)


class FormAutor(forms.Form):
    nombre = forms.CharField(max_length=100)
    biografia = forms.CharField(widget=forms.Textarea)
    libros = forms.CharField(max_length=100)


class FormReseña(forms.Form):
    PUNTAJE = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]
    libro = forms.CharField()
    reseña = forms.CharField(widget=forms.Textarea)
    estrellas = forms.ChoiceField(choices=PUNTAJE)

