from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa, Veiculo, MovRotative


def home(request):
    context = {'mensagem': 'Ola Mundo...'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})


def lista_movrotativo(request):
    mov_rot = MovRotative.objects.all()
    return render(request, 'core/mov_rotativo.html',  {'mov_rot': mov_rot})

