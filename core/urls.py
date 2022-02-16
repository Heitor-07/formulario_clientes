from django.urls import path
from .views import IndexView, CadastroView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
]

