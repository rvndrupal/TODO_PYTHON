from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"  #nombre del paquete de todos las urls muy importante para las rutas

urlpatterns = [
    #inicio del proyecto uno
    path('', views.InicioView.as_view(), name="inicio"),
    #del proyecto uno
    path('listar-todos-empleados/', views.ListAllEmpleados.as_view(),name="lista_empleados"),
    #path('listar-departamento/', views.ListporArea.as_view()),  
    path('listar-departamento/<dep>', views.ListporArea.as_view(),name="persona_departamento"),  
    path('listar-empleado-caja/', views.ListporCaja.as_view()),  
    path('listar-habilidad/', views.ListaHabilidades.as_view()),  
    path('empleado-detalle/<pk>', views.Empleado_DetailView.as_view(),name="detalle_empleado"),   #<pk> es el id de la persona
    path('add-empleado/', views.EmpleadosCreateView.as_view(), name="agregar_empleado"),
    path('success/', views.SuccessView.as_view(), name="add_empleado"),
    path('update-empleado/<pk>', views.EmpleadoUpdateView.as_view(), name="update_empleado"),
    path('borrar-empleado/<pk>', views.EmpleadoDeleteView.as_view(), name="borrar_empleado"),
    path('lista_admin',views.ListAllEmpleadosAdmin.as_view(),name="lista_admin")
    
    
]
