from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sexo', 'cpf', 'nasc', 'telefone', 'celular', 'email']


