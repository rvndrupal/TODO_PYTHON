from django import forms


#Creamos el formulario que va a tener dos tipos de modelos diferentes

#hereda de form por que es simple no es modemform no hereda de un formulario
#fc
class NewdepartamentoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50, required=True)
    apellidos = forms.CharField(label='Apellidos', max_length=50, required=True)
    departamento = forms.CharField(label='Departamento', max_length=70, required=True)
    shorname = forms.CharField(label='ShortName', max_length=50, required=True)
    