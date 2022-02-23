from django.views.generic import TemplateView, ListView, DeleteView
from .models import Cliente
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required

# Create your views here.


class IndexView(TemplateView):
    template_name = 'logar.html'


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


@login_required()
def cadastro(request):
    template_name = 'cadastro.html'
    form = ClienteForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista')

    context = {'form': form}
    return render(request, template_name, context)


class Lista(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'lista.html'
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'


@login_required()
def up_date(request, pk):
    upd = get_object_or_404(Cliente, id=pk)
    forms = ClienteForm(request.POST or None, instance=upd)
    if forms.is_valid():
        forms.save()
        return redirect('lista')
    context = {
        'forms': forms
    }
    return render(request, 'cliente.html', context)


class DeletaView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'deletar.html'
    success_url = reverse_lazy('lista')


def erro404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset-utf8', status=404)

