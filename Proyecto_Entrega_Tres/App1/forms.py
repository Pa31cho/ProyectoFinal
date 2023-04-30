from django import forms
 
class ProductoFormu(forms.Form):
    id= forms.IntegerField()
    nombre = forms.CharField()
    cantidad = forms.IntegerField()

class ClienteFormu(forms.Form):
    id= forms.IntegerField()   
    nombre = forms.CharField()
    apellido = forms.CharField()
    email= forms.CharField()

class ProveedorFormu(forms.Form):
    id= forms.IntegerField()   
    nombre = forms.CharField()
    apellido = forms.CharField()
    email= forms.CharField()
    cuil= forms.IntegerField()   

