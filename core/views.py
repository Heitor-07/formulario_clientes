from django.views.generic import TemplateView, FormView
from .forms import ClienteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.


class IndexView(TemplateView):
    template_name = 'home.html'


class CadastroView(LoginRequiredMixin, FormView):
    success_url = reverse_lazy('login')
    template_name = 'cadastro.html'
    form_class = ClienteForm


    def form_valid(self, form):
        return super(CadastroView, self).form_valid()

