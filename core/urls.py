from django.urls import path
from .views import (
        home,
        lista_pessoas,
        lista_veiculos,
        lista_movrotativo,
        pessoa_novo
)

urlpatterns = [
        path('index/', home, name='core_home'),
        path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
        path('pessoas-novo/', pessoa_novo, name='core_pessoa_novo'),
        path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
        path('mov_rotativo/', lista_movrotativo, name='core_lista_movrotativo'),
]
