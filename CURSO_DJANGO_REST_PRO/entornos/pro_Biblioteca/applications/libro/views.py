
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView 

from .models import *

class ListLibros(ListView):
    #model = Autor
    template_name = "libros/lista.html"
    context_object_name="lista_libros"

    def get_queryset(self):        
        palabra=self.request.GET.get("nombre",'')
        f1=self.request.GET.get("fecha1",'')
        f2=self.request.GET.get("fecha2",'')
        if f1 and f2:
            return Libro.objects.listar_libros2(palabra,f1,f2)
        else:
            return Libro.objects.listar_libros(palabra)
            
        
    