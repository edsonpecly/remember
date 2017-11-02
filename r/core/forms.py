from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .utils import generate_hash_key
from .mail import send_mail_template
from .models import (User, DesignSystem, ControleCadastro, ConfigsSistema, PasswordReset, PeriodicidadeProduto,
                     PeriodicidadeServico)

User = get_user_model()


class UserAdminCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'is_active', 'is_staff']


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita a senha', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('As senhas não conferem')
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'telefone', 'name', 'nome_empresa', 'endereco', 'email', 'vendedor']


class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError('Nenhum usuário encontrado com este e-mail')

    def save(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        template_name = 'recuperacao-senha.html'
        subject = 'Criar nova senha R Sistema'
        context = {
            'reset': reset,
        }
        send_mail_template(subject, template_name, context, [user.email])


class EditAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'name', 'endereco', 'telefone', 'whatsapp', 'nome_empresa', 'cnpj', 'whatsapp',
            'permissao', 'plano', 'inicio_ciclo', 'fim_ciclo', 'tipo_pagamento', 'vendedor'
        ]


class DesignSystemForm(forms.ModelForm):
    class Meta:
        model = DesignSystem
        fields = ['cor_topo', 'cor_pn_retorno', 'cor_pn_aniversario', 'cor_pn_produto']


class ControleCadastroForm(forms.ModelForm):
    class Meta:
        model = ControleCadastro
        fields = [
            'u_telefone', 'u_data_nascimento', 'u_endereco', 'u_observacao', 'u_telefone', 'p_celular', 'p_observacao',
            'p_data_nascimento', 'p_endereco', 's_valor', 's_observacao', 'pr_custo', 'pr_valor', 'pr_observacao',
        ]


class ConfigsSistemaForm(forms.ModelForm):
    class Meta:
        model = ConfigsSistema
        fields = [
            'aviso_retorno', 'aviso_produto', 'c_profissional', 'c_produto', 'ctrl_servicos', 'ctrl_produto'
        ]


class PeriodicidadeProdutoForm(forms.ModelForm):
    class Meta:
        model = PeriodicidadeProduto
        fields = ['pc_produto']


class PeriodicidadeServicoForm(forms.ModelForm):
    class Meta:
        model = PeriodicidadeServico
        fields = ['pc_servico']
