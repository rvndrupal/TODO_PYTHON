from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, unique=True) #el campo sea unico
    #short_name = models.CharField('Nombre corto', max_length=50, blank=True, editable=False) #Que el campo no es Requerido, no se ve por el editable
    short_name = models.CharField('Nombre corto', max_length=50, blank=True, editable=True) #Que el campo no es Requerido
    anulate = models.BooleanField('Anulado', default=False)
    
    class Meta:
        verbose_name="Mi departamento"
        verbose_name_plural="Areas de la empresa"
        ordering = ['name'] #Orden los elementos si le pones ["-name"] es la inversa
        unique_together=('name','short_name') #no permite que se registren elementos convinados del nombre y nombre corto
       
    
    def __str__(self):
        return self.name +'-'+ self.short_name
    