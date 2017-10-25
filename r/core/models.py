import re
from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Nome de Usuário', max_length=30, unique=True,
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                              'O nome de usuário só pode  conter letras, números ou os seguintes '
                                              'caracteres @/./+/-/_',
                                              'invalid')]
    )
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Seu Nome', max_length=20, blank=True, null=True)
    nome_empresa = models.CharField('Nome da Empresa', max_length=24, blank=True, null=True)
    VENDEDOR = (
        ('0', 'Sem Vendedor'),
        ('1', 'Edson Pecly'),
        ('2', 'Graziele Pecly'),
        ('3', 'Diego Fernando')
    )
    vendedor = models.CharField('Vendedor Responsável', default='0', choices=VENDEDOR, max_length=10, blank=True, null=True)
    permissao = models.CharField('Nivel Permissão', max_length=2, blank=True, null=True)  # 0=inativo 5=empresa 10=admin
    PLANO_CHOICES = (
        ('1', 'Ouro - R$ 95,88/ano'),
        ('2', 'Prata - R$ 29,70/trimestre'),
        ('3', 'Bronze - R$ 11,99/mês ')
    )
    plano = models.CharField('Plano', max_length=10, choices=PLANO_CHOICES, blank=True, null=True)
    inicio_ciclo = models.DateField('Inicio do Ciclo', null=True, blank=True)
    fim_ciclo = models.DateField('Final do Ciclo', null=True, blank=True)
    PAGAMENTO_CHOICES = (
        ('1', 'Depósito Bancário'),
        ('2', 'Boleto'),
        ('3', 'Cartão de Crédito')
    )
    tipo_pagamento = models.CharField(
        'Tipo de Pagamento', max_length=50, choices=PAGAMENTO_CHOICES, default=3, null=True, blank=True
    )
    endereco = models.CharField('Endereço', max_length=200, blank=True, null=True)
    cnpj = models.CharField('CNPJ', max_length=18, blank=True, null=True)
    cod_empresa = models.CharField('Cód Empresa', max_length=18, blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=14, blank=True, null=True)
    whatsapp = models.CharField('WhatsApp', max_length=11, blank=True, null=True)
    is_active = models.BooleanField('Ativo', blank=True, default=True)
    is_staff = models.BooleanField('Equipe', blank=True, default=False)
    slug = models.SlugField('URL', max_length=100, null=True, blank=True)
    date_joined = models.DateTimeField('Data de cadastro', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    def criaslug(self):
        return slugify(str(self.id))

    @models.permalink
    def get_absolute_url(self):
        return ('adm:editar_conta', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['name', 'permissao']


class PasswordReset(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='reset'
    )
    key = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    confirmed = models.BooleanField('Confirmado?', default=False, blank=True)

    def __str__(self):
        return '{0} em {1}'.format(self.user, self.created_at)

    class Meta:
        verbose_name = 'Nova Senha'
        verbose_name_plural = 'Novas Senhas'
        ordering = ['-created_at']


class DesignSystem(models.Model):
    usuario = models.CharField('Empresa', max_length=50, null=True, blank=True)
    CORES_CHOICES = (
        ('1', 'Amarelo'),
        ('2', 'Vermelho'),
        ('3', 'Roxo'),
        ('4', 'Azul')
    )
    cor_topo = models.CharField('Topo Sistema', max_length=50, choices=CORES_CHOICES, default='3', null=True, blank=True)
    cor_pn_retorno = models.CharField(
        'Painel de Retorno', max_length=50, choices=CORES_CHOICES, default='2', null=True, blank=True
    )
    cor_pn_aniversario = models.CharField(
        'Painel de Aniversário', max_length=50, choices=CORES_CHOICES, default='1', null=True, blank=True
    )
    cor_pn_produto = models.CharField(
        'Painel de Produtos', max_length=50, choices=CORES_CHOICES, default='4', null=True, blank=True
    )
    slug = models.SlugField('URL', max_length=100, null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Design Sistema'
        verbose_name_plural = 'Design Sistema'

    def criaslug(self):
        return slugify(str(self.id))

    @models.permalink
    def get_absolute_url(self):
        return ('editar-design', (), {'slug': self.slug})


class ControleCadastro(models.Model):
    STATUS_CHOICE = (
        ('1', 'Sim'),
        ('2', 'Não')
    )
    usuario = models.CharField('Empresa', max_length=20, null=True, blank=True)
    u_telefone = models.CharField('Usu - Exibir Telefone?', max_length=5, choices=STATUS_CHOICE, default='2')
    u_data_nascimento = models.CharField(
        'Usu - Exibir Data de Nascimento?', max_length=5, choices=STATUS_CHOICE, default='1'
    )
    u_endereco = models.CharField('Usu - Exibir Endereço?', max_length=5, choices=STATUS_CHOICE, default='2')
    u_observacao = models.CharField('Usu - Exibir Observação?', max_length=5, choices=STATUS_CHOICE, default='2')
    p_celular = models.CharField('Prof - Exibir Celular?', max_length=5, choices=STATUS_CHOICE, default='2')
    p_data_nascimento = models.CharField(
        'Prof - Exibir Data de Nascimento?', max_length=5, choices=STATUS_CHOICE, default='2'
    )
    p_endereco = models.CharField('Prof - Exibir Endereço?', max_length=5, choices=STATUS_CHOICE, default='2')
    p_observacao = models.CharField('Prof - Exibir Observação?', max_length=5, choices=STATUS_CHOICE, default='2')
    s_valor = models.CharField('Ser - Exibir Valor?', max_length=5, choices=STATUS_CHOICE, default='1')
    s_observacao = models.CharField('Ser - Exibir Observação?', max_length=5, choices=STATUS_CHOICE, default='2')
    pr_custo = models.CharField('Prod - Exibir Custo?', max_length=5, choices=STATUS_CHOICE, default='2')
    pr_valor = models.CharField('Prod - Exibir Valor?', max_length=5, choices=STATUS_CHOICE, default='1')
    pr_observacao = models.CharField('Prod - Exibir Observação?', max_length=5, choices=STATUS_CHOICE, default='2')
    slug = models.SlugField('URL', max_length=100, null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Controle Cadastro'
        verbose_name_plural = 'Controle Cadastro'

    def criaslug(self):
        return slugify(str(self.id))

    @models.permalink
    def get_absolute_url(self):
        return ('editar-controle-cadastro', (), {'slug': self.slug})


class ConfigsSistema(models.Model):
    STATUS = (
        ('1', 'Sim'),
        ('2', 'Não')
    )
    CONTROLE = (
        ('1', 'Cadastro'),
        ('2', 'Utilização')
    )
    usuario = models.CharField('Empresa', max_length=20, null=True, blank=True)
    aviso_retorno = models.PositiveIntegerField('Retorno - avisar em', null=True, blank=True)
    aviso_produto = models.PositiveIntegerField('Produto - avisar em', null=True, blank=True)
    c_profissional = models.CharField(
        'Utilizar Cad Profissional?', max_length=5, choices=STATUS, default='1', null=True, blank=True
    )
    c_produto = models.CharField(
        'Utilizar Cad Produto?', max_length=5, choices=STATUS, default='1', null=True, blank=True
    )
    ctrl_servicos = models.CharField(
        'Periodicidade Serviços', max_length=5, choices=CONTROLE, default='1', null=True, blank=True
    )
    ctrl_produto = models.CharField(
        'Periodicidade Produtos', max_length=5, choices=CONTROLE, default='2', null=True, blank=True
    )
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Configuração do Sistema'
        verbose_name_plural = 'Configurações do Sistema'
