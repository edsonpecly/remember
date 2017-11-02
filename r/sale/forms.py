from django import forms
from .models import VendaServico, VendaProduto
from r.registration.models import Cliente, Profissional, Servico, Produto


class VendaServicoForm(forms.ModelForm):
    class Meta:
        model = VendaServico
        fields = ['cliente', 'servico', 'profissional', 'observacao', 'qtd']
        list_filter = ['cliente']

    def __init__(self, user, *args, **kwargs):
        super(VendaServicoForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.filter(empresa=user)
        self.fields['profissional'].queryset = Profissional.objects.filter(empresa=user)
        self.fields['servico'].queryset = Servico.objects.filter(empresa=user)


class EditarVendaServicoForm(forms.ModelForm):
    class Meta:
        model = VendaServico
        fields = ['status']
        list_filter = ['cliente']


class VendaProdutoForm(forms.ModelForm):
    class Meta:
        model = VendaProduto
        fields = ['cliente', 'produto', 'profissional', 'observacao', 'qtd']
        list_filter = ['cliente']

    def __init__(self, user, *args, **kwargs):
        super(VendaProdutoForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.filter(empresa=user)
        self.fields['profissional'].queryset = Profissional.objects.filter(empresa=user)
        self.fields['produto'].queryset = Produto.objects.filter(empresa=user)


class EditarVendaProdutoForm(forms.ModelForm):
    class Meta:
        model = VendaProduto
        fields = ['status']
        list_filter = ['cliente']
