from django.db import models
from django.template.defaultfilters import slugify


class SolicitarPagamento(models.Model):
    usuario = models.CharField('Solicitante', max_length=50, null=True, blank=True)
    PLANO_CHOICES = (
        ('1', 'Ouro - R$ 95,88/ano'),
        ('2', 'Prata - R$ 29,70/trimestre'),
        ('3', 'Bronze - R$ 11,99/mês ')
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
        ('2', 'Alterar de Método de Pagamento'),
        ('3', 'Dúvidas/ Críticas/ Sugestões'),
        ('4', 'Cancelar assinatura'),
    )
    solicitacao = models.CharField(
        'Solicitação', max_length=50, choices=TIPO_SOLICITACAO, null=True, blank=True
    )
    mensagem = models.TextField('Mensagem',  null=True, blank=True)
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
