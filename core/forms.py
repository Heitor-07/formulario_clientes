import datetime

from django.forms import ModelForm

from .models import Cliente
from django import forms


class ClienteForm(forms.ModelForm):

    nome = forms.CharField(max_length=50)
    sexo = forms.CharField(max_length=15)
    cpf = forms.CharField(max_length=11)
    nasc = forms.DateField(widget=forms.SelectDateWidget)
    telefone = forms.CharField(max_length=10)
    celular = forms.CharField(max_length=11)
    email = forms.EmailField()

    class Meta:

        model = Cliente
        fields = ['nome', 'sexo', 'cpf', 'nasc', 'telefone', 'celular', 'email']


