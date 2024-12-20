from django.shortcuts import render, redirect
from .models import Pessoa, Veiculo, MovRotative, MovMensalista, Mensalista
from .forms import PessoaForm, VeiculoForm, MovRotativeForm, MovMensalistaForm, MensalistaForm


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


def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': pessoa})


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


def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/veiculo_update.html', data)


def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': veiculo})


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


def mov_rot_update(request, id):
    data = {}
    mov_rot = MovRotative.objects.get(id=id)
    form = MovRotativeForm(request.POST or None, instance=mov_rot)
    data['mov_rot'] = mov_rot
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativo')
    else:
        return render(request, 'core/mov_rot_update.html', data)


def mov_rot_delete(request, id):
    mov_rot_delete = MovRotative.objects.get(id=id)
    if request.method == 'POST':
        mov_rot_delete.delete()
        return redirect('core_lista_movrotativo')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mov_rot_delete})


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


def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/mensalista_update.html', data)


def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mensalista})


def movmensalista(request):
    mov_mensalistas = MovMensalista.objects.all()
    form = MensalistaForm()
    data = {'mov_mensalistas': mov_mensalistas, 'form': form}
    return render(request, 'core/movmensalista.html', data)


def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalista')


def movmensalista_update(request, id):
    data = {}
    mov_mensalista = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=mov_mensalista)
    data['mov_mensalista'] = mov_mensalista
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalista')
    else:
        return render(request, 'core/movmensalista_update.html', data)