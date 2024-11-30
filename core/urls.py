from django.urls import path
from .views import (
    home,
    lista_pessoas,
    lista_veiculos,
    lista_movrotativo,
    pessoa_novo,
    veiculo_novo,
    mov_rot_novo,
    lista_mensalista,
    mensalista_novo,
    pessoa_update,
    veiculo_update,
)

urlpatterns = [
    path('index/', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoas-novo/', pessoa_novo, name='core_pessoa_novo'),
    path('pessoa-update/<int:id>/', pessoa_update, name='core_pessoa_update'),

    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('veiculos-novo/', veiculo_novo, name='core_veiculo_novo'),
    path('veiculo-update/<int:id>/', veiculo_update, name='core_veiculo_update'),

    path('mov_rotativo/', lista_movrotativo, name='core_lista_movrotativo'),
    path('mov_rotativo-novo/', mov_rot_novo, name='core_movrotativo_novo'),

    path('mensalista/', lista_mensalista, name='core_lista_mensalista'),
    path('mensalista-novo/', mensalista_novo, name='core_mensalista_novo'),

]
