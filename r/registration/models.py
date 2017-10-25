from django.db import models
from django.template.defaultfilters import slugify


class Cliente(models.Model):
    empresa = models.CharField('Empresa Criadora', max_length=30, null=True, blank=True)
    nome = models.CharField('Nome Completo', max_length=23, null=False, blank=False)
    email = models.EmailField('Email', unique=True)
    data_nascimento = models.DateField('Data de Nascimento', null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=14, null=True, blank=True)
    whatsapp = models.CharField('WhatsApp', max_length=11, unique=True)
    cep = models.CharField('CEP', max_length=10, null=True, blank=True)
    endereco = models.CharField('Endereço', max_length=150, null=True, blank=True)
    compl = models.CharField('Compl.', max_length=20, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=100, null=True, blank=True)
    cidade = models.CharField('Cidade', max_length=100, null=True, blank=True)
    ESTADOS_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RR', 'Roraima'),
        ('RO', 'Rondônia'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    estado = models.CharField('Estado', max_length=20, choices=ESTADOS_CHOICES, blank=True, null=True)
    observacao = models.TextField('Observações', null=True, blank=True)
    slug = models.SlugField('Id url', null=True)
    created_at = models.DateTimeField('Cadastrado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.nome

    def criaslug(self):
        return slugify(str(self.id))

    @models.permalink
    def get_absolute_url(self):
        return ('registration:detalhe_cliente', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']


class Profissional(models.Model):
    empresa = models.CharField('Empresa Criadora', max_length=30, null=True, blank=True)
    nome = models.CharField('Nome Completo', max_length=23, null=False, blank=False)
    email = models.EmailField('Email', unique=True)
    data_nascimento = models.DateField('Data de Nascimento', null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=14, null=True, blank=True)
    celular = models.CharField('Celular', max_length=11, unique=True, null=True, blank=True)
    cep = models.CharField('CEP', max_length=10, null=True, blank=True)
    endereco = models.CharField('Endereço', max_length=150, null=True, blank=True)
    compl = models.CharField('Compl.', max_length=20, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=100, null=True, blank=True)
    cidade = models.CharField('Cidade', max_length=100, null=True, blank=True)
    ESTADOS_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RR', 'Roraima'),
        ('RO', 'Rondônia'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    estado = models.CharField('Estado', max_length=20, choices=ESTADOS_CHOICES, blank=True, null=True)
    observacao = models.TextField('Observações', null=True, blank=True)
    serviços = models.CharField('Habilidades do Profissional', max_length=30, null=True, blank=True)
    horarios = models.CharField('Horários de Trabalho', max_length=30, null=True, blank=True)
    slug = models.SlugField('Id url', null=True)
    created_at = models.DateTimeField('Cadastrado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.nome

    def criaslug(self):
        return slugify(str(self.id))

    @models.permalink
    def get_absolute_url(self):
        return ('registration:detalhe_profissional', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'
        ordering = ['nome']


class Servico(models.Model):
    empresa = models.CharField('Empresa Criadora', max_length=100, null=True, blank=True)
    nome = models.CharField('Nome', max_length=100)
    periodicidade = models.PositiveIntegerField('Periodicidade')
    valor = models.DecimalField('Valor', max_digits=10, default=0, decimal_places=2, null=True, blank=True)
    observacao = models.TextField('Observação', null=True, blank=True)
    slug = models.SlugField('Id url', null=True, blank=True)
    created_at = models.DateTimeField('Cadastrado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.nome

    def criaslug(self):
        return slugify(str(self.id))

    @models.permalink
    def get_absolute_url(self):
        return ('registration:detalhe_servico', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'


class Produto(models.Model):
    empresa = models.CharField('Empresa Criadora', max_length=100, null=True, blank=True)
    nome = models.CharField('Nome', max_length=100)
    periodicidade = models.PositiveIntegerField('Periodicidade')
    custo = models.DecimalField('Valor de Custo', max_digits=10, decimal_places=2, null=True, blank=True)
    valor = models.DecimalField('Valor', max_digits=10, default=0, decimal_places=2, null=True, blank=True)
    observacao = models.TextField('Observação', null=True, blank=True)
    slug = models.SlugField('Id url', null=True, blank=True)
    created_at = models.DateTimeField('Cadastrado em', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.nome

    def criaslug(self):
        return slugify(str(self.id))

    @models.permalink
    def get_absolute_url(self):
        return ('registration:detalhe_produto', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'