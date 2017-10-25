from django import forms
from .models import SolicitarPagamento, Suporte


class SolicitarPagamentoForm(forms.ModelForm):
    class Meta:
        model = SolicitarPagamento
        fields =['plano', 'pagamento']


class SuporteForm(forms.ModelForm):
    class Meta:
        model = Suporte
        fields =['solicitacao', 'mensagem']
