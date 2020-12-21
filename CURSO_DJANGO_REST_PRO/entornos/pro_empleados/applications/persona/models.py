from django.db import models

from applications.departamento.models import *

# Create your models here.

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
    
    def __str__(self):
        return str(self.id)+'--'+ self.first_name + '--' + self.last_name
    