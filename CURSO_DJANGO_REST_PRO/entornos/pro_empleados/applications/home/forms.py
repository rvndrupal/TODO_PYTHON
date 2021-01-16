from django import forms

from .models import  *


#mf

class PruebasForm(forms.ModelForm):
    """Form definition fos Prueba."""

    class Meta:
        """Meta definition fos Pruebaform."""
        model= Prueba4
        fields = ('nombre','ap','am','edad')
        
        #atributos
        widgets ={
            'nombre': forms.TextInput(
                attrs ={
                    'placeholder': 'Ingresa tu nombre',
                    'class': 'cl_nombre',
                    'id': 'id_nombre'                    
                }
            )
        }
        
    def clean_edad(self):
        edad=self.cleaned_data['edad']  #recuperamos el valor
        if edad < 10:
            raise forms.ValidationError('Ingrese una edad mayor a 10')        
        return edad 

