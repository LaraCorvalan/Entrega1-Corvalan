from django.urls import path
from myApp import views

urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path('about/', views.about, name = 'Sobre mi'),
    path('libros/', views.formLibros, name = 'Libros'),
    path('autores/', views.formAutor, name = 'Autores'),
    path('libros-lista/', views.mostrarLibros, name = 'mostrarLibros'),
    path('reseñas/', views.formReseñas, name = 'Reseñas'),
    path('libros-lista/search/', views.search, name = 'Search'),
    path('lista-reseñas/', views.reseñas, name = 'lista_reseñas')


]