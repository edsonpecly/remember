from django import forms
from .models import SolicitarPagamento, Suporte, Vendedor, CadastroVendedor, InserirComissao, PagarComissao


class SolicitarPagamentoForm(forms.ModelForm):
    class Meta:
        model = SolicitarPagamento
        fields = ['plano', 'pagamento']


class SuporteForm(forms.ModelForm):
    class Meta:
        model = Suporte
        fields = ['solicitacao', 'mensagem']


class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nome', 'apelido', 'telefone', 'email', 'comissao']


class CadastroVendedorForm(forms.ModelForm):
    class Meta:
        model = CadastroVendedor
        fields = ['nome', 'status', 'telefone', 'email', 'termos']


class InserirComissaoForm(forms.ModelForm):
    class Meta:
        model = InserirComissao
        fields = ['vendedor', 'cliente', 'valor']


class PagarComissaoForm(forms.ModelForm):
    class Meta:
        model = PagarComissao
        fields = ['vendedor', 'valor', 'status']
