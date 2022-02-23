from django.urls import path
from .views import IndexView, cadastro, Lista, HomeView, up_date, DeletaView

urlpatterns = [
    path('', IndexView.as_view(), name='logar'),
    path('home', HomeView.as_view(), name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('lista', Lista.as_view(), name='lista'),
    path('cliente/<int:pk>', up_date, name='cliente'),
    path('<int:pk>/deleta', DeletaView.as_view(), name='deleta'),
]

