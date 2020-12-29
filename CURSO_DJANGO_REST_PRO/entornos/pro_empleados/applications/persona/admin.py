from django.contrib import admin

from .models import *
# Register your models here.


admin.site.register(Habilidades)


class EmpleadosAdmin(admin.ModelAdmin):
    list_display =(
        'first_name',
        'last_name',
        'departamento',
        'job', 
        'full_name', #No existe se crea.  
        'hoja_vida'
    )
    
    def full_name(self,obj): #el object trae todos los datos del modelo. super chingon
        return str(obj.id) +'->' +obj.first_name + '-' + obj.last_name  #se tare la combinacion de los campos esta super chingon
    
    search_fields = ('first_name',)
    list_filter = ('departamento','job','departamento')
    filter_horizontal=('habilidades',)  #filtro para el campo muchos a muchos
    
admin.site.register(Empleado, EmpleadosAdmin)  #se carga aqui