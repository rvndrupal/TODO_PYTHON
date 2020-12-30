from django.shortcuts import render

from django.views.generic import ListView, DetailView,CreateView,TemplateView

from django.urls import reverse_lazy

from .models import *

# Create your views here.

#Lista de todos los empleados
class ListAllEmpleados(ListView):
    template_name='persona/list_all.html'
    model=Empleado
    context_object_name='lp'  #array que se manda al html

#Listar por area de la empresa
'''
class ListporArea(ListView):
    template_name='persona/list_dep.html'
    queryset=Empleado.objects.filter(
        departamento__short_name='sis'   #departamaento__short_name  es la realacion con departamento y que se traiga el nombre
    )
'''
#Listar segunda manera correcta
class ListporArea(ListView):
    template_name='persona/list_dep.html'
    
    def get_queryset(self):
        dep=self.kwargs['dep'] #obtengo el valor de la url
        lista = Empleado.objects.filter(
        departamento__short_name=dep   #departamaento__short_name  es la realacion con departamento y que se traiga el nombre
        )
        return lista
    
    
#listar por caja
class ListporCaja(ListView):
    template_name='persona/list_dep_caja.html'
    context_object_name='lp' 
    
    def get_queryset(self):
        emp = self.request.GET.get("empleado", '') #obtengo el valor de la caja html dep
       
        lista = Empleado.objects.filter(
        first_name=emp   #departamaento__short_name  es la realacion con departamento y que se traiga el nombre
        )
        return lista
    
#Habilidades del empleado relacion manytomany
class ListaHabilidades(ListView):
    template_name='persona/list_Habilidades.html'
    context_object_name='lph' 
    
    def get_queryset(self):
        empleado=Empleado.objects.get(id=2) #Obtengo un empleado especifico
        Habi=empleado.habilidades.all() #con la funcion all se trae todas sus habilidades.
        return  Habi
    
    
#Detalles de una vista el  famoso ver más
class Empleado_DetailView(DetailView):
    template_name = "persona/Detalle_persona.html"
    model = Empleado
    
    #Se pueden mandar datos de otro tipo
    def get_context_data(self, **kwargs):
        context = super(Empleado_DetailView, self).get_context_data(**kwargs)
        context["titulo"] = "Empleado del mes" 
        return context
    


#Crear empleados


class SuccessView(TemplateView):
    template_name = "persona/success.html"

class EmpleadosCreateView(CreateView):
    model = Empleado
    template_name = "persona/add-persona.html"
    #fields=['first_name','last_name','job']
    fields=('__all__')
    #success_url='.' #con esto le digo que se valla a la misma pagina
    #muy importante agregar la libreria arriba reverse_lazy
    success_url=reverse_lazy('persona_app:add_empleado')
    
    Video-> 51