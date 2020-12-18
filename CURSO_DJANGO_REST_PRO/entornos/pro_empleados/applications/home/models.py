from django.db import models

# Create your models here.

class Prueba3(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return self.titulo
    

class Prueba4(models.Model):
    nombre = models.CharField(max_length=50)
    ap = models.CharField(max_length=50)
    am = models.CharField(max_length=50)
    edad = models.IntegerField()
    
    def __str__(self):
        return self.nombre +'--'+ self.ap
    

    