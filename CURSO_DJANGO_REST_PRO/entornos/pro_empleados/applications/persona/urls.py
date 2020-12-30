from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"  #nombre del paquete de todos las urls muy importante para las rutas

urlpatterns = [
    path('listar-todos-empleados/', views.ListAllEmpleados.as_view()),
    #path('listar-departamento/', views.ListporArea.as_view()),  
    path('listar-departamento/<dep>', views.ListporArea.as_view()),  
    path('listar-empleado-caja/', views.ListporCaja.as_view()),  
    path('listar-habilidad/', views.ListaHabilidades.as_view()),  
    path('empleado-detalle/<pk>', views.Empleado_DetailView.as_view()),   #<pk> es el id de la persona
    path('add-empleado/', views.EmpleadosCreateView.as_view()),
    path('success/', views.SuccessView.as_view(), name="add_empleado"),
    
    
]
