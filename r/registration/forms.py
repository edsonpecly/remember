from django import forms
from .models import Cliente, Profissional, Servico, Produto


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome', 'email', 'telefone', 'data_nascimento', 'whatsapp', 'endereco', 'compl', 'bairro', 'cidade',
            'estado', 'observacao',
        ]


class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = [
            'nome', 'email', 'telefone', 'data_nascimento', 'celular', 'endereco', 'compl', 'bairro', 'cidade',
            'estado', 'observacao',
        ]


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'periodicidade', 'valor', 'observacao']


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'periodicidade', 'custo', 'valor', 'observacao']