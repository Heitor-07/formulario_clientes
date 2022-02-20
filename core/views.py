from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .models import Cliente
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.


class IndexView(TemplateView):
    template_name = 'logar.html'


class HomeView(LoginRequiredMixin ,TemplateView):
    template_name = 'home.html'


class CadastroView(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = 'cadastro.html'
    fields = ['nome', 'sexo', 'cpf', 'nasc', 'telefone', 'celular', 'email']
    success_url = reverse_lazy('cadastro')


class Lista(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'lista.html'
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'


class AtualizaView(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = 'cliente.html'
    fields = ['nome', 'sexo', 'cpf', 'nasc', 'telefone', 'celular', 'email']
    success_url = reverse_lazy('lista')


class DeletaView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'deletar.html'
    success_url = reverse_lazy('lista')
