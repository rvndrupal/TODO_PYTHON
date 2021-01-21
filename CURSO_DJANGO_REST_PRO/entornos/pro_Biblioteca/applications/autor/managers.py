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
    
    #busca por nombre y apellidos con exclusion de edad
    def buscar_autor3(self, palabra):
        
        resultado=self.filter(
            Q(nombre__icontains=palabra) | Q(apellidos__icontains=palabra)
            ).exclude(
                Q(edad__icontains=23) |  Q(edad__icontains=40) 
            )
            #TAMBIEN SE PUEDE HACER CON FILTER
            # ).filter(
            #     Q(edad__icontains=23) |  Q(edad__icontains=60) 
            # )  checarlo bien por que hace doble filtro
        return resultado
        
    #busca por nombre y apellidos con exclusion de edad mayor y menor
    def buscar_autor4(self, palabra):
        
        resultado=self.filter(
            Q(nombre__icontains=palabra) | Q(apellidos__icontains=palabra)
            # ).exclude(
            #     Q(edad__gt=23) |  Q(edad__lt=40)  #gt siginifica > mayor que  y lt es menor que  con ó
            # ).order_by("id")
            ).exclude(
                edad__gt=40,
                edad__lt=50
            ).order_by("id")  #solo deja los que no esten en ese parametro
            
        return resultado
        