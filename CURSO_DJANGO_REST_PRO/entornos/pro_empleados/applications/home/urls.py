from django.contrib import admin
from django.urls import path

from . import views



urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
    path('prueba2/', views.PruebaListView.as_view()),
    path('lista_prueba3/', views.ListaPrueba3.as_view()),
    path('add/', views.Prueba3CreateView.as_view(), name="add"),
]
