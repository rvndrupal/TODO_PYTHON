from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView 

from .models import *

class ListAutores(ListView):
    #model = Autor
    template_name = "autor/lista.html"
    context_object_name="lista_autores"

    def get_queryset(self):        
        #return Autor.objects.all()
        #cone el manager
        return Autor.objects.listar_autores()
    
#buscar por campo de texto
class ListAutores2(ListView):
    #model = Autor
    template_name = "autor/lista.html"
    context_object_name="lista_autores"

    def get_queryset(self):        
        #return Autor.objects.all()
        #cone el manager
        palabra=self.request.GET.get("nombre",'')
        #return Autor.objects.buscar_autor(palabra)
        return Autor.objects.buscar_autor2(palabra)
    
    