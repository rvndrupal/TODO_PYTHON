from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('autores/', views.ListAutores2.as_view(),name="autores"),
]
