from django.forms import ModelForm
from .models import Pessoa, Veiculo, MovRotative, Mensalista, MovMensalista


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'


class MovRotativeForm(ModelForm):
    class Meta:
        model = MovRotative
        fields = '__all__'


class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'

class MovMensalistaForm(ModelForm):
    class Meta:
        model = MovMensalista
        fields = '__all__'