import datetime
from django.db import models

from django.db.models import Q

class LibrosManager(models.Manager):
    #se exporta en el modelo
    # def listar_autores(self):
    #     return self.all()
    
    #busca por nombre
    def listar_libros(self, palabra):        
        resultado=self.filter(
            titulo__icontains=palabra,
            )
        return resultado
    
    #busca por nombre y fecha
    def listar_libros2(self, palabra, f1,f2):     
        date1=datetime.datetime.strptime(f1, "%Y-%m-%d").date()
        date2=datetime.datetime.strptime(f2, "%Y-%m-%d").date()
           
        resultado=self.filter(
            titulo__icontains=palabra,
            fecha__range=(date1,date2)
            )
        return resultado