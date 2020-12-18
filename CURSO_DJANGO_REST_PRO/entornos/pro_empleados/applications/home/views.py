from django.shortcuts import render

from django.views.generic import TemplateView, ListView 



class PruebaView(TemplateView):
    template_name= "home/prueba.html"
    

class  PruebaListView(ListView):
    template_name = "home/prueba2.html"
    context_object_name='numeros'
    queryset= ['0','10','20','30']
    

