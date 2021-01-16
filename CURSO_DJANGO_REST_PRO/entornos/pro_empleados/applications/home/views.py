from django.shortcuts import render

from django.views.generic import TemplateView, ListView, CreateView 

#modelos
from .models import *

#importar el forms

from .forms import *



class PruebaView(TemplateView):
    template_name= "home/prueba.html"
    

class  PruebaListView(ListView):
    template_name = "home/prueba2.html"
    context_object_name='numeros'
    queryset= ['0','10','20','30']
    
class ListaPrueba3(ListView):
    template_name = "home/lista_prueba3.html"
    context_object_name='lp3'
    model=Prueba3
    
'''
class Prueba3CreateView(CreateView):
    model = Prueba3
    template_name = "home/add.html"
    fields=['titulo','subtitulo','cantidad']
    success_url='/'
'''    
class Prueba3CreateView(CreateView):
    model = Prueba4
    template_name = "home/add.html"
    #fields=['titulo','subtitulo','cantidad']
    form_class=PruebasForm  #toma todo lo del forms
    success_url='/'

    
    

