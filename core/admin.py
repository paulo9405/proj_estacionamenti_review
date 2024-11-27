from django.contrib import admin
from core.models import *


class PessoaAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'endereco',
        'telefone'
    )


class ParametroAdmin(admin.ModelAdmin):
    list_display = (
        'valor_hora',
        'valor_mes'
    )


class MarcaAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
    )


class MensalistaAdmin(admin.ModelAdmin):
    list_display = (
        'veiculo',
        'inicio',
        'valor_mes'
    )


class MovMenssalistaAdmin(admin.ModelAdmin):
    list_display = (
        'mensalista',
        'data_pagamento',
        'total'
    )


class VeiculoAdmin(admin.ModelAdmin):
    list_display = (
        'marca',
        'placa',
        'proprietario',
        'cor',
        'observacoes'
    )


class MovRotativoAdmin(admin.ModelAdmin):
    list_display = (
        'checkin', 'checkout', 'valor_hora', 'veiculo',
        'pago')


admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Parametros, ParametroAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Veiculo, VeiculoAdmin)
admin.site.register(MovRotative, MovRotativoAdmin)
admin.site.register(Mensalista, MensalistaAdmin)
admin.site.register(MovMensalista, MovMenssalistaAdmin)
