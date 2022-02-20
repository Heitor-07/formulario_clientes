from django.urls import path
from .views import IndexView, CadastroView, Lista, HomeView, AtualizaView, DeletaView

urlpatterns = [
    path('', IndexView.as_view(), name='logar'),
    path('home', HomeView.as_view(), name='home'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('lista', Lista.as_view(), name='lista'),
    path('<int:pk>/cliente', AtualizaView.as_view(), name='cliente'),
    path('<int:pk>/deleta', DeletaView.as_view(), name='deleta')
]

