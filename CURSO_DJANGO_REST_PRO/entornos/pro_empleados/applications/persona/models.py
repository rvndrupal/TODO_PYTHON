from django.db import models

from applications.departamento.models import *
#ckeditor
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField("Habilidad", max_length=50)
    
    class Meta:
        verbose_name="Habilidad"
        verbose_name_plural="Habilidades de los empleados"
        
    def __str__(self):
        return str(self.id)+'--'+ self.habilidad
    
        


class Empleado(models.Model):
    
    Job=(
        ('0' , 'CONTADOR'),
        ('1' , 'ADMINISTRADOR'),
        ('2' , 'ECONOMISTA'),
        ('3' , 'OTRO'),        
    )
    
    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    job = models.CharField('Trabajo', max_length=1, choices=Job)  #Lista de Opciones el valor que se guarda en la base es el numero
    #ojo primero importar el modelo al que se va a relacionar
    #Luego s epone el model a relacionar
    #comando  fk
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #m2m
    #Relacion de muchos a muchos con la tabla habilidades de arriba
    habilidades = models.ManyToManyField(Habilidades)
    #Para el Ckeditor
    hoja_vida= RichTextField() 
    
    class Meta:
        verbose_name="Empleado"
        verbose_name_plural="Empleados de la empresa"
        ordering = ['first_name'] #Orden los elementos si le pones ["-name"] es la inversa
        unique_together=('first_name',) #no permite que se registren elementos convinados del nombre y nombre corto
    
    def __str__(self):
        return str(self.id)+'--'+ self.first_name + '--' + self.last_name
    