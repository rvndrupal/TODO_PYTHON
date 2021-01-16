from django.shortcuts import render

from django.views.generic import ListView, DetailView,CreateView,TemplateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import *

# Create your views here.

#inicio del proyecto uno

class InicioView(TemplateView):
    template_name = "inicio.html"


#Lista de todos los empleados del sistema
class ListAllEmpleados(ListView):
    template_name='persona/list_all.html'
    #model=Empleado  #ya no se pasa por el queryset
    context_object_name='lp'  #array que se manda al html
    paginate_by=5  #Genera la páginacion
    
    def get_queryset(self):
        emp = self.request.GET.get("empleado", '') #obtengo el valor de la caja html dep       
        lista = Empleado.objects.filter(
        #first_name=emp   #departamaento__short_name  es la realacion con departamento y que se traiga el nombre
        first_name__icontains=emp  #este hace la magia por si no tiene valor devuelva todos
        )
        return lista
    
    
#Lista de todos los empleados del sistema pestaña admin
class ListAllEmpleadosAdmin(ListView):
    template_name='persona/lista_empleados_admin.html'
    #model=Empleado  #ya no se pasa por el queryset
    context_object_name='empleados'  #array que se manda al html
    paginate_by=5  #Genera la páginacion
    ordering='first_name'
    
    def get_queryset(self):
        emp = self.request.GET.get("empleado", '') #obtengo el valor de la caja html dep       
        lista = Empleado.objects.filter(
        #first_name=emp   #departamaento__short_name  es la realacion con departamento y que se traiga el nombre
        first_name__icontains=emp  #este hace la magia por si no tiene valor devuelva todos
        )
        return lista
    

#Listar por area de la empresa
'''
class ListporArea(ListView):
    template_name='persona/list_dep.html'
    queryset=Empleado.objects.filter(
        departamento__short_name='sis'   #departamaento__short_name  es la realacion con departamento y que se traiga el nombre
    )
'''
#Listar segunda manera correcta
#Con esta consulta puedes listar los departamentos y ver cuantos empleado hay por departamento
#se podria decir que es la inversa de la consulta 
class ListporArea(ListView):
    template_name='persona/list_dep.html'
    context_object_name='empleados'
    
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
    template_name = "persona/add-persona.html"
    model = Empleado   
    #fields=['first_name','last_name','job']
    #fields=('__all__') mostrar todos
    fields=['first_name','last_name','job','departamento','habilidades']
    #success_url='.' #con esto le digo que se valla a la misma pagina
    #muy importante agregar la libreria arriba reverse_lazy
    success_url=reverse_lazy('persona_app:lista_admin')
    
    #Validando los datos y juntando el full_name esta funcion esta muy chingona
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        #empleado=form.save() #guarda todo en la base de datos
        empleado=form.save(commit=False) #guarda todo en la variable sin pasar a la base mejor para no hacer carga doble        
        empleado.full_name=empleado.first_name + ' ' + empleado.last_name
        empleado.save() #se vuelve a guardar muy chingo por que esto es desde la base de datos.
        return super(EmpleadosCreateView, self).form_valid(form)
    
    
    
    #Actualizaciones con update
class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields=['first_name','last_name','job','departamento','habilidades']
    success_url=reverse_lazy('persona_app:lista_admin')
    
    #Post se hace primero que el form_valid
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        #request.POST['full_name'] = request.POST['first_name']+ '-' + request.POST['last_name']
        print(request.POST['first_name'])
        return super().post(request, *args, **kwargs)

    
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        #empleado=form.save() #guarda todo en la base de datos
        empleado=form.save(commit=False) #guarda todo en la variable sin pasar a la base mejor para no hacer carga doble        
        empleado.full_name=empleado.first_name + '---' + empleado.last_name
        empleado.save() #se vuelve a guardar muy chingo por que esto es desde la base de datos.
        return super(EmpleadoUpdateView, self).form_valid(form)
    
    
#Borrar el empleado

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/borrar_empleado.html"
    success_url=reverse_lazy('persona_app:lista_admin')
    
    
    

    