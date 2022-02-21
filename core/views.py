from django.views.generic import TemplateView, ListView, UpdateView, DeleteView
from .models import Cliente
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from .forms import ClienteForm

# Create your views here.


class IndexView(TemplateView):
    template_name = 'logar.html'


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


def cadastro(request):
    template_name = 'cadastro.html'
    form = ClienteForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista')
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, template_name, context)


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


def erro404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset-utf8', status=404)

