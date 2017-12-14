'''
Created on 3 dic. 2017

@author: franklin
'''

from django.forms import ModelForm
#from django import forms
#from django.contrib.auth.forms import AuthenticationForm
#from django.utils.translation import ugettext_lazy as _
from voluntarios.models import Voluntario, Referencia
#from django.forms.widgets import Select, NumberInput, TextInput, DateInput
#from django.forms.fields import CharField#


class VoluntarioForm(ModelForm):
    class Meta:
        model = Voluntario
        fields = '__all__'
        #fields = ['cedula','nombres','apellido_paterno','apellido_materno','sexo','fecha_nacimiento','telefono','estado','referencia']


class ReferenciaForm(ModelForm):
    class Meta:
        model = Referencia
        fields = '__all__'        