from django.contrib import admin
from django.urls import path

from . import views



urlpatterns = [
    path('listar-todos-empleados/', views.ListAllEmpleados.as_view()),
    #path('listar-departamento/', views.ListporArea.as_view()),  
    path('listar-departamento/<dep>', views.ListporArea.as_view()),  
    path('listar-empleado-caja/', views.ListporCaja.as_view()),  
]
