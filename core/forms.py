from django.forms import ModelForm

from .models import Cliente


class ClienteForm(ModelForm):

    class Meta:
        model = Cliente
        fields = ['nome', 'sexo', 'cpf', 'nasc', 'telefone', 'celular', 'email']


