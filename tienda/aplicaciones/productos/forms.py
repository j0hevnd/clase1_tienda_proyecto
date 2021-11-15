from django import forms
from django.forms.widgets import Textarea

from .models import Producto

# class FormularioProductos(forms.Form):

#     nombre = forms.CharField(max_length=70)
#     descripcion = forms.CharField(widget=Textarea)
#     precio = forms.FloatField()
#     stock = forms.IntegerField()
#     imagen = forms.ImageField()

class FormularioProductos(forms.ModelForm):
    class Meta:
        model=Producto
        fields = ('__all__')