from django.views.generic import TemplateView, CreateView
from .models import Cliente
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.


class IndexView(TemplateView):
    template_name = 'home.html'


class CadastroView(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = 'cadastro.html'
    fields = ['nome', 'sexo', 'cpf', 'nasc', 'telefone', 'celular', 'email']
    success_url = reverse_lazy('cadastro')


