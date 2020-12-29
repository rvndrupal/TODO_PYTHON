from django.shortcuts import render

from django.views.generic import ListView

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
    
  