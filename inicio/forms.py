from django import forms

class CrearCelularFormulario (forms.Form):    
    marca = forms.CharField (max_length=20)
    modelo = forms.CharField (max_length=20)