from django.db import models
from r.registration.models import Cliente, Servico, Profissional, Produto
from django.template.defaultfilters import slugify


class VendaServico(models.Model):
    empresa = models.CharField('Empresa Criadora', max_length=30, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', related_name='cliente')
    profissional = models.ForeignKey(
        Profissional, verbose_name='Profissional', related_name='profissional', blank=True, null=True
    )
    servico = models.ForeignKey(Servico, verbose_name='Serviço', related_name='servico')
    data = models.DateField('Data de Realização', auto_now_add=True)
    valor = models.DecimalField('Valor', max_digits=10, default=0, decimal_places=2, null=True, blank=True)
    qtd = models.PositiveIntegerField('Quantidade', default=1, null=True, blank=True)
    periodicidade = models.PositiveIntegerField('Periodicidade', null=True, blank=True)
    retorno = models.DateField('Data de Retorno', null=True, blank=True)
    STATUS_CHOICE = (
        ('1', 'Mensagem Enviada'),
        ('2', 'Mensagem não enviada')
    )
    status = models.CharField('Status de Aviso', max_length=3, choices=STATUS_CHOICE, default=2, blank=False, null=True)
    slug = models.SlugField('ID url', null=True)
    observacao = models.TextField('Observações', null=True, blank=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Venda de Serviço'
        verbose_name_plural = 'Vendas de Serviços'
        ordering = ['-status', 'retorno']

    def __str__(self):
        return str(self.servico)

    def criaslug(self):
        return slugify(str(self.id))

    @models.permalink
    def get_absolute_url(self):
        return ('sale:detalhe_venda_servico', (), {'slug': self.slug})


class VendaProduto(models.Model):
    empresa = models.CharField('Empresa Criadora', max_length=30, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', related_name='cliente2')
    profissional = models.ForeignKey(
        Profissional, verbose_name='Profissional', related_name='profissional2', blank=True, null=True
    )
    produto = models.ForeignKey(Produto, verbose_name='Produto', related_name='produto')
    qtd = models.PositiveIntegerField('Quantidade', default=1, null=True, blank=True)
    valor = models.DecimalField('Valor', max_digits=10, default=0, decimal_places=2, null=True, blank=True)
    data = models.DateField('Data de Realização', auto_now_add=True)
    periodicidade = models.PositiveIntegerField('Periodicidade', null=True, blank=True)
    retorno = models.DateField('retorno', null=True, blank=True)
    nova_compra = models.DateField('Nova Compra', null=True, blank=True)
    STATUS_CHOICE = (
        ('1', 'Mensagem Enviada'),
        ('2', 'Mensagem não enviada')
    )
    status = models.CharField('Status de Aviso', max_length=3, choices=STATUS_CHOICE, default=2, blank=False, null=True)
    slug = models.SlugField('ID url', null=True)
    observacao = models.TextField('Observações', null=True, blank=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Venda de Produto'
        verbose_name_plural = 'Vendas de Produtos'
        ordering = ['-status', 'nova_compra']

    def __str__(self):
        return str(self.produto)

    def criaslug(self):
        return slugify(str(self.id))

    @models.permalink
    def get_absolute_url(self):
        return ('sale:detalhe_venda_produto', (), {'slug': self.slug})
