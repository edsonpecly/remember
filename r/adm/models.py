from django.db import models
from django.template.defaultfilters import slugify


class SolicitarPagamento(models.Model):
    usuario = models.CharField('Solicitante', max_length=50, null=True, blank=True)
    PLANO_CHOICES = (
        ('1', 'Ouro - R$ 119,88/ano'),
        ('2', 'Prata - R$ 35,97/trimestre'),
        ('3', 'Bronze - R$ 14,99/mês ')
    )
    plano = models.CharField(
        'Plano Escolhido', max_length=50, choices=PLANO_CHOICES, default='1', null=True, blank=True
    )
    PAGAMENTO_CHOICES = (
        ('1', 'Depósito Bancário'),
        ('2', 'Boleto')
    )
    pagamento = models.CharField(
        'Tipo de Pagamento', max_length=50, choices=PAGAMENTO_CHOICES, default='1', null=True, blank=True
    )
    STATUS_CHOICES = (
        ('1', 'Não Atendida'),
        ('2', 'Atendida')
    )
    status = models.CharField(
        'Status Solicitação', choices=STATUS_CHOICES, max_length=30, default='1', null=True, blank=True
    )
    slug = models.SlugField('URL', max_length=100, null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Solicitação de Pagamento'
        verbose_name_plural = 'Solicitações de Pagamento'

    def criaslug(self):
        return slugify(str(self.id))

    @models.permalink
    def get_absolute_url(self):
        return ('editar-solicitacao-pagamento', (), {'slug': self.slug})


class Suporte(models.Model):
    usuario = models.CharField('Solicitante', max_length=50, null=True, blank=True)
    protocolo = models.CharField('Protocolo de Atendimento', max_length=100, null=True, blank=True)
    TIPO_SOLICITACAO = (
        ('1', 'Alteração de Plano'),
        ('2', 'Regularização de conta'),
        ('3', 'Alterar de Método de Pagamento'),
        ('4', 'Dúvidas/ Críticas/ Sugestões'),
        ('5', 'Cancelar assinatura'),
        ('6', 'Outras'),
    )
    solicitacao = models.CharField(
        'Solicitação', max_length=50, choices=TIPO_SOLICITACAO, null=True, blank=True
    )
    mensagem = models.TextField('Mensagem', null=True, blank=True)
    resposta = models.TextField('Resposta',  default='', null=True, blank=True)
    email = models.CharField('E-mail', max_length=100, null=True, blank=True)
    telefone = models.CharField('Fone', max_length=100, null=True, blank=True)
    STATUS_CHOICES = (
        ('1', 'Não Atendida'),
        ('2', 'Atendida')
    )
    status = models.CharField(
        'Status Solicitação', choices=STATUS_CHOICES, max_length=30, default='1', null=True, blank=True
    )
    slug = models.SlugField('URL', max_length=100, null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Suporte'
        verbose_name_plural = 'Suportes'
        ordering = ['status', 'created_at']

    def criaslug(self):
        return slugify(str(self.id))

    @models.permalink
    def get_absolute_url(self):
        return ('protocolo_de_atendimento', (), {'slug': self.slug})


class Vendedor(models.Model):
    nome = models.CharField('Nome Completo', max_length=100)
    apelido = models.CharField('Nome de Vendas', max_length=100, null=True, blank=True)
    email = models.EmailField('E-mail')
    telefone = models.CharField('Telefone', max_length=14)
    comissao = models.PositiveIntegerField('Comissao', blank=True, null=True, default=0)
    banco = models.CharField('Banco', max_length=50, null=True, blank=True)
    agencia = models.CharField('Agencia', max_length=50, null=True, blank=True)
    TIPO_CONTA = (
        ('1', 'Conta Poupança'),
        ('2', 'Conta Corrente')
    )
    tipo_conta = models.CharField('Tipo da Conta', choices=TIPO_CONTA, max_length=50, null=True, blank=True)
    conta = models.CharField('N° da Conta', max_length=50, null=True, blank=True)
    slug = models.SlugField('URL', max_length=100, null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)

    def __str__(self):
        return str(self.apelido)

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'
        ordering = ['nome', 'comissao']

    def criaslug(self):
        return slugify(str(self.id))

    @models.permalink
    def get_absolute_url(self):
        return ('adm:vendedor', (), {'slug': self.slug})


class CadastroVendedor(models.Model):
    nome = models.CharField('Nome Completo', max_length=100)
    STATUS = (
        ('1', 'Aguardando'),
        ('2', 'Aprovado'),
        ('3', 'Reprovado'),
    )
    status = models.CharField('Status de Liberação', choices=STATUS, max_length=30, null=True, blank=True)
    email = models.EmailField('E-mail')
    telefone = models.CharField('Telefone', max_length=14)
    termos = models.BooleanField('Concordancia com os termos', default=False, blank=True)
    mensagem = models.TextField('Mensagem', null=True, blank=True)
    slug = models.SlugField('URL', max_length=100, null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name = 'Cadastro Vendedor'
        verbose_name_plural = 'Cadastros Vendedores'
        ordering = ['status', 'created_at']

    def criaslug(self):
        return slugify(str(self.id))

    @models.permalink
    def get_absolute_url(self):
        return ('adm:vendedor', (), {'slug': self.slug})


class InserirComissao(models.Model):
    vendedor = models.ForeignKey(Vendedor, verbose_name='Vendedor', blank=True, null=True)
    cliente = models.CharField('Cliente', max_length=100, null=True, blank=True)
    valor = models.DecimalField('Valor da Comissão', max_digits=10, default=0, decimal_places=2, null=True, blank=True)

    slug = models.SlugField('URL', max_length=100, null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)

    def __str__(self):
        return str(self.id or self.vendedor)

    class Meta:
        verbose_name = 'Comissão'
        verbose_name_plural = 'Comissões'
        ordering = ['vendedor', '-created_at']

    def criaslug(self):
        return slugify(str(self.id))

    @models.permalink
    def get_absolute_url(self):
        return ('adm:inserir_comissao', (), {'slug': self.slug})


class PagarComissao(models.Model):
    vendedor = models.CharField('Vendedor', max_length=100, blank=True, null=True)
    valor = models.DecimalField('Valor Pago', max_digits=10, default=0, decimal_places=2, null=True, blank=True)
    STATUS = (
        ('1', 'Aguardando'),
        ('2', 'Pago'),
    )
    status = models.CharField(
        'Status da Solicitação', max_length=20, default='1', choices=STATUS, null=True, blank=True
    )

    slug = models.SlugField('URL', max_length=100, null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)

    def __str__(self):
        return str(self.id or self.vendedor)

    class Meta:
        verbose_name = 'Silicitação de Comissão'
        verbose_name_plural = 'Solicitações de Comissões'
        ordering = ['-created_at']

    def criaslug(self):
        return slugify(str(self.id))

    @models.permalink
    def get_absolute_url(self):
        return ('adm:pagar_comissao', (), {'slug': self.slug})
