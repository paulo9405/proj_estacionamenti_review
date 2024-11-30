from django.shortcuts import render, redirect
from .models import Pessoa, Veiculo, MovRotative, Mensalista
from .forms import PessoaForm, VeiculoForm, MovRotativeForm, MensalistaForm


def home(request):
    context = {'mensagem': 'Ola Mundo...'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/pessoa_update.html', data)


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def lista_movrotativo(request):
    mov_rot = MovRotative.objects.all()
    form = MovRotativeForm()
    data = {'mov_rot': mov_rot, 'form': form}
    return render(request, 'core/mov_rotativo.html', data)


def mov_rot_novo(request):
    form = MovRotativeForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativo')


def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/lista_mensalista.html', data)


def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalista')
