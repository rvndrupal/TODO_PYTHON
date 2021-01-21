from django.db import models

from django.db.models import Q

class AutorManager(models.Manager):
    #se exporta en el modelo
    # def listar_autores(self):
    #     return self.all()
    
    #busca por nombre
    def buscar_autor(self, palabra):
        
        resultado=self.filter(
            nombre__icontains=palabra
            )
        return resultado
        
    #busca por nombre y apellidos
    def buscar_autor2(self, palabra):
        
        resultado=self.filter(
            Q(nombre__icontains=palabra) | Q(apellidos__icontains=palabra)
            )
        return resultado
        