from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView     #Tiene todas las caracteristicas de las vistas
from django.views.generic import TemplateView, ListView,DetailView

#modelos
from applications.persona.models import  Empleado
from .models import *

# Create your views here.
from .forms import *


class SuccessView(TemplateView):
    template_name = "departamento/succes_dep.html"
    

#Departamento lista de departamentos

class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/listar.html"
    context_object_name='Dep'  #array que se manda al html
    paginate_by=5  #Genera la páginacion
    
    
    def get_queryset(self):
        dep = self.request.GET.get("depa", '') #obtengo el valor de la caja html dep       
        lista = Departamento.objects.filter(
        #first_name=emp   #departamaento__short_name  es la realacion con departamento y que se traiga el nombre
         name__icontains=dep  #este hace la magia por si no tiene valor devuelva todos
        )
        return lista
    
#Detalle Departamento
class DepartamentoDetailView(DetailView):
    template_name = "departamento/Detalle_departamento.html"
    model = Departamento
    context_object_name='Dep'
    
    


class NewDepartamentoView(FormView):
    template_name="departamento/new_departamento.html"
    form_class=NewdepartamentoForm
    success_url=reverse_lazy('departamento_app:succes_departamento')
    
    def form_valid(self, form):
        print("Cargando el formulario")
        #Se crea la toma de Valores para el Departamento
        depa=Departamento(
            name=form.cleaned_data["departamento"],  #se tomando los valores del formulario y se igual a los campos departamento
            short_name=form.cleaned_data["shorname"]  #se tomando los valores del formulario y se igual a los campos departamento
        )
        depa.save() #se guardan los datos en depa y se pueden pasar al departamento de empleado
        
        nombre=form.cleaned_data["nombre"] #recuperamos valores del Formulario
        apellido=form.cleaned_data["apellidos"] #recuperamos valores del Formulario
        Empleado.objects.create(
            first_name=nombre,  #se iguala a los campos del model empleado
            last_name=apellido,  #se iguala a los campos del model empleado
            job='1',
            departamento=depa
        )#con la funcion create no es necesario mandar a llamr a save()
        
        return super(NewDepartamentoView, self).form_valid(form)