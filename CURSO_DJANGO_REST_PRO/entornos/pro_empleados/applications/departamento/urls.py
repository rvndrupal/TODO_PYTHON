from django.contrib import admin
from django.urls import path

def Departamento(self):
    print("#######Demo del Departamento##############")


urlpatterns = [
    path('departamento/', Departamento),
]
