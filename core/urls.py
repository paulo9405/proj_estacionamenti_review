from django.urls import path
from core import views

urlpatterns = [
    path('index/', views.home, name='core_home'),
    path('pessoas/', views.lista_pessoas, name='core_lista_pessoas'),
    path('pessoas-novo/', views.pessoa_novo, name='core_pessoa_novo'),
    path('pessoa-update/<int:id>/', views.pessoa_update, name='core_pessoa_update'),
    path('pessoa-delete/<int:id>/', views.pessoa_delete, name='core_pessoa_delete'),

    path('veiculos/', views.lista_veiculos, name='core_lista_veiculos'),
    path('veiculos-novo/', views.veiculo_novo, name='core_veiculo_novo'),
    path('veiculo-update/<int:id>/', views.veiculo_update, name='core_veiculo_update'),

    path('mov_rotativo/', views.lista_movrotativo, name='core_lista_movrotativo'),
    path('mov_rotativo-novo/', views.mov_rot_novo, name='core_movrotativo_novo'),
    path('mov_rot_update/<int:id>/', views.mov_rot_update, name='core_mov_rot_update'),

    path('mensalista/', views.lista_mensalista, name='core_lista_mensalista'),
    path('mensalista-novo/', views.mensalista_novo, name='core_mensalista_novo'),
    path('mensalista-update/<int:id>/', views.mensalista_update, name='core_mensalista_update'),

]
