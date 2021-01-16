from django.contrib import admin
from django.urls import path

from . import views

def Departamento(self):
    print("#######Demo del Departamento##############")

app_name = "departamento_app" 

urlpatterns = [
    path('departamento/', Departamento),
    path('listar-departamentos/', views.DepartamentoListView.as_view(),name="lista_departamentos"),
    path('departamento-detalle/<pk>', views.DepartamentoDetailView.as_view(),name="departamento-detalle"),   #<pk> es el id de la persona
    path('success_departamento/', views.SuccessView.as_view(), name="succes_departamento"),
    path('new_departamento/', views.NewDepartamentoView.as_view(), name="Nuevo_departamento"),
    
]
