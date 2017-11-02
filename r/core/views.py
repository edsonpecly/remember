from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from r.adm.forms import SolicitarPagamentoForm, SuporteForm
from r.adm.models import SolicitarPagamento, Suporte
from r.sale.models import VendaServico, VendaProduto
from r.registration.models import Servico, Cliente
from .forms import (
    EditAccountForm, DesignSystemForm, RegisterForm, ControleCadastroForm, ConfigsSistemaForm, PasswordResetForm
)
from .models import User, DesignSystem, ControleCadastro, ConfigsSistema, PasswordReset
from django.contrib import messages
from datetime import date, datetime


def index(request):
    template_name = 'index.html'
    return render(request, template_name)


@login_required
def home(request):
    template_name = 'home.html'
    home = 'active'
    request.session.clear_expired()
    servicos_realizados = VendaServico.objects.filter(empresa=str(request.user.id)).count()
    valores = VendaServico.objects.filter(empresa=str(request.user.id))
    contagem = 0
    soma = 0
    while contagem < servicos_realizados:
        for v in valores:
            valor1 = v.valor
            valor1 = soma + valor1
            soma = valor1
            contagem = contagem + 1
    produtos_vendidos = VendaProduto.objects.filter(empresa=str(request.user.id)).count()
    p_valores = VendaProduto.objects.filter(empresa=str(request.user.id))
    p_contagem = 0
    p_soma = 0
    p_qtd = 0
    while p_contagem < produtos_vendidos:
        for vp in p_valores:
            p_valor1 = vp.valor
            p_valor1 = p_soma + p_valor1
            qtd_vp = vp.qtd
            qtd_vp = p_qtd + qtd_vp
            p_qtd = qtd_vp
            p_soma = p_valor1
            p_contagem = p_contagem + 1
    total_vendas = soma + p_soma
    total_vp = p_qtd
    dia = f"{datetime.now():%d}"
    mes = f"{datetime.now():%m}"
    ano = f"{datetime.now():%Y}"
    aniversario = Cliente.objects.filter(empresa=str(request.user.id)).filter(
        data_nascimento__day=dia).filter(data_nascimento__month=mes).count()
    limite_10 = int(dia) - 10
    limite_7 = int(dia) - 7
    limite_5 = int(dia) - 5
    limite_3 = int(dia) - 3
    venc_limite_10 = User.objects.filter(id=request.user.id).filter(fim_ciclo__day__gte=limite_10).filter(
            fim_ciclo__day__lt=limite_7).filter(fim_ciclo__month=mes).filter(fim_ciclo__year=ano).count()
    venc_limite_7 = User.objects.filter(id=request.user.id).filter(fim_ciclo__day__gte=limite_7).filter(
        fim_ciclo__day__lt=limite_5).filter(fim_ciclo__month=mes).filter(fim_ciclo__year=ano).count()
    venc_limite_5 = User.objects.filter(id=request.user.id).filter(fim_ciclo__day__gte=limite_5).filter(
        fim_ciclo__day__lt=limite_3).filter(fim_ciclo__month=mes).filter(fim_ciclo__year=ano).count()
    if venc_limite_10 == 1:
        User.objects.filter(id=request.user.id).update(permissao=3)
        return redirect('acesso_negado')
    elif venc_limite_7 == 1:
        User.objects.filter(id=request.user.id).update(permissao=2)
    elif venc_limite_5 == 1:
        User.objects.filter(id=request.user.id).update(permissao=1)
    context = {
        'home': home,
        'servicos_realizados': servicos_realizados,
        'total_vendas': total_vendas,
        'produtos_vendidos': total_vp,
        'aniversario': aniversario
    }
    if request.user.whatsapp is None:
        messages.info(request, 'Por favor, complete seu cadastro para continuar')
        return redirect('editar_informacoes')
    else:
        return render(request, template_name, context)


def cadastro_usuario(request):
    template_name = 'cadastro-usuario.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        form2 = DesignSystemForm(request.POST)
        if form.is_valid():
            User = form.save(commit=False)
            User.permissao = '0'
            form.save()
            User.cod_empresa = User.id
            User.slug = (User.criaslug())
            form.save()
            User = authenticate(
                username=User.username, password=form.cleaned_data['password1']
            )
            login(request, User)
            DesignSystem = form2.save(commit=False)
            form2.save()
            DesignSystem.usuario = User.id
            DesignSystem.slug = (DesignSystem.criaslug())
            form2.save()
            form3 = ControleCadastro(
                usuario=User.id, u_telefone='2', u_data_nascimento='2', u_endereco='2', u_observacao='2', p_celular='2',
                p_data_nascimento='2', p_endereco='2', p_observacao='2', s_valor='1', s_observacao='2', pr_custo='2',
                pr_valor='1', pr_observacao='2'
            )
            form3.save()
            form3.slug = form3.id
            form3.save()
            form4 = ConfigsSistema(
                usuario=User.id, aviso_retorno=5, aviso_produto=5, c_profissional='1', c_produto='1',
                ctrl_servicos='1', ctrl_produto='2'
            )
            form4.save()
            messages.info(request, 'Falta Pouco, escolha um plano de assinatura')
            return redirect('planos_assinatura')
    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context)


def resetar_senha(request):
    template_name = 'resetar-senha.html'
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.info(request, 'Solicitação realizada com sucesso')
    context = {
        'form': form
    }
    return render(request, template_name, context)


def password_reset_confirm(request, key):
    template_name = 'confirmacao-senha.html'
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        messages.info(request, 'Senha alterada com sucesso!')
        return redirect('login')
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def planos_assinatura(request):
    template_name = 'planos-assinatura.html'
    return render(request, template_name)


@login_required
def deposito_boleto(request):
    template_name = 'deposito-boleto.html'
    if request.method == 'POST':
        form = SolicitarPagamentoForm(request.POST)
        if form.is_valid():
            SolicitarPagamento = form.save(commit=False)
            SolicitarPagamento.usuario = request.user.id
            form.save()
            User.objects.filter(id=request.user.id).update(tipo_pagamento=SolicitarPagamento.pagamento)
            SolicitarPagamento.slug = (SolicitarPagamento.criaslug())
            form.save()
            messages.info(request, 'Sua solicitação será respondida em breve')
            return redirect('cadastro_realizado')
        else:
            messages.info(request, 'Deu Errado')
    else:
        form = SolicitarPagamentoForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def cadastro_realizado(request):
    template_name = 'cadastro-realizado.html'
    return render(request, template_name)


@login_required
def plano_ouro(request):
    template_name = 'plano-ouro.html'
    if request.user.plano == '1' or request.user.plano is None:
        User.objects.filter(id=request.user.id).update(plano='1')
    else:
        return redirect('aguarde_aprovacao')
    return render(request, template_name)


@login_required
def plano_prata(request):
    template_name = 'plano-prata.html'
    if request.user.plano == '2' or request.user.plano is None:
        User.objects.filter(id=request.user.id).update(plano='2')
    else:
        return redirect('aguarde_aprovacao')
    return render(request, template_name)


@login_required
def plano_bronze(request):
    template_name = 'plano-bronze.html'
    if request.user.plano == '3' or request.user.plano is None:
        User.objects.filter(id=request.user.id).update(plano='3')
    else:
        return redirect('aguarde_aprovacao')
    return render(request, template_name)


@login_required
def aguarde_aprovacao(request):
    template_name = 'aguarde-aprovacao.html'
    return render(request, template_name)


@login_required
def acesso_negado(request):
    template_name = 'acesso-negado.html'
    return render(request, template_name)


@login_required
def aviso_retorno(request):
    template_name = 'aviso-retorno.html'
    aviso_retorno = 'active'
    servicos_realizados = VendaServico.objects.filter(empresa=str(request.user.id)).count()
    context = {
        'aviso_retorno': aviso_retorno,
        'servicos_realizados': servicos_realizados
    }
    return render(request, template_name, context)


@login_required
def aviso_produto(request):
    template_name = 'aviso-produto.html'
    aviso_produto = 'active'
    produtos_vendidos = VendaProduto.objects.filter(empresa=str(request.user.id)).count()
    context = {
        'aviso_produto': aviso_produto,
        'produtos_vendidos': produtos_vendidos
    }
    return render(request, template_name, context)


@login_required
def aviso_aniversario(request):
    template_name = 'aviso-aniversario.html'
    aviso_aniversario = 'active'
    data = f"{datetime.now():%d/%m}"
    aniversario = Cliente.objects.filter(empresa=str(request.user.id))
    context = {
        'aviso_aniversario': aviso_aniversario,
        'data': data,
        'aniversario': aniversario
    }
    return render(request, template_name, context)


@login_required
def info_gerais(request):
    template_name = 'info-gerais.html'
    info_gerais = 'active'
    if len(str(request.user.id)) < 3:
        format_campo = '00'
    context = {
        'info_gerais': info_gerais,
        'format_campo': format_campo
    }
    return render(request, template_name, context)


@login_required
def editar_informacoes(request):
    template_name = 'editar-informacoes.html'
    editar_informacoes = 'active'
    permissao = request.user.permissao
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            User = form.save(commit=False)
            User.permissao = permissao
            form.save()
            form = EditAccountForm(instance=request.user)
            messages.success(request, 'As alterações foram gravadas com sucesso!')
    else:
        form = EditAccountForm(instance=request.user)
    context = {
        'form': form,
        'editar_informacoes': editar_informacoes
    }
    return render(request, template_name, context)


@login_required
def editar_senha(request):
    template_name = 'editar-senha.html'
    editar_senha = 'active'
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            user = form.save()
            user = authenticate(
                username=user.username, password=PasswordChangeForm(data=request.POST, user=request.user)
            )
            login(request, user)
            messages.info(request, 'A senha foi alterada com sucesso')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {
        'form': form,
        'editar_senha': editar_senha,
    }
    return render(request, template_name, context)


@login_required
def design(request):
    template_name = 'design.html'
    design = 'active'
    context = {
        'design': design
    }
    return render(request, template_name, context)


@login_required
def editar_design(request):
    template_name = 'editar-design.html'
    design = 'active'
    condicao = DesignSystem.objects.all()
    condicao2 = condicao.count()
    if condicao2 > 0:
        design_system = DesignSystem.objects.get(usuario=str(request.user.id))
        context = {}
        if request.method == 'POST':
            form = DesignSystemForm(request.POST, instance=design_system)
            if form.is_valid():
                form.save()
                form = DesignSystemForm(instance=design_system)
                messages.success(request, 'Alterações gravadas com sucesso')
                return redirect('design')
        else:
            form = DesignSystemForm(instance=design_system)
    else:
        messages.info(request, 'Você ainda não pode alterar o design do sistema')
        return redirect('home')
    context = {
        'design': design,
        'form': form
    }
    return render(request, template_name, context)


@login_required
def ctrl_cadastro(request):
    template_name = 'ctrl-cadastro.html'
    ctrl_cadastro = 'active'
    context = {
        'ctrl_cadastro': ctrl_cadastro
    }
    return render(request, template_name, context)


@login_required
def editar_ctrl_cadastro(request):
    template_name = 'editar-ctrl-cadastro.html'
    ctrl_cadastro = 'active'
    condicao = ControleCadastro.objects.all().count()
    if condicao > 0:
        ctrl_cadastro = ControleCadastro.objects.get(usuario=str(request.user.id))
        context = {}
        if request.method == 'POST':
            form = ControleCadastroForm(request.POST, instance=ctrl_cadastro)
            if form.is_valid():
                form.save()
                form = ControleCadastroForm(instance=ctrl_cadastro)
                messages.success(request, 'Alterações gravadas com sucesso')
                return redirect('ctrl_cadastro')
        else:
            form = ControleCadastroForm(instance=ctrl_cadastro)
    else:
        messages.info(request, 'Você ainda não pode alterar o design do sistema')
        return redirect('home')
    context = {
        'ctrl_cadastro': ctrl_cadastro,
        'form': form
    }
    return render(request, template_name, context)


@login_required
def config_gerais(request):
    template_name = 'config-gerais.html'
    config_gerais = 'active'
    context = {
        'config_gerais': config_gerais
    }
    return render(request, template_name, context)


@login_required
def editar_config_gerais(request):
    template_name = 'editar-config-gerais.html'
    config_gerais = 'active'
    condicao = ConfigsSistema.objects.all().count()
    if condicao > 0:
        config_gerais = ConfigsSistema.objects.get(usuario=str(request.user.id))
        context = {}
        if request.method == 'POST':
            form = ConfigsSistemaForm(request.POST, instance=config_gerais)
            if form.is_valid():
                form.save()
                form = ConfigsSistemaForm(instance=config_gerais)
                messages.success(request, 'Alterações gravadas com sucesso')
                return redirect('config_gerais')
        else:
            form = ConfigsSistemaForm(instance=config_gerais)
    else:
        messages.info(request, 'Você ainda não pode alterar as configurações do sistema')
        return redirect('home')
    context = {
        'config_gerais': config_gerais,
        'form': form
    }
    return render(request, template_name, context)


@login_required
def suporte(request):
    template_name = 'suporte.html'
    suporte = 'active'
    consulta_protocolo = Suporte.objects.filter(usuario=request.user.cod_empresa)
    paginator = Paginator(consulta_protocolo, 15)
    query = request.GET.get('q')
    results = ''
    try:
        query = str(query)
    except ValueError:
        query = None
        results = None
    if query:
        try:
            results = Suporte.objects.filter(
                usuario=request.user.cod_empresa).filter(protocolo__icontains=query)
        except Suporte.DoesNotExist:
            results = None
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        consulta_protocolo = paginator.page(page)
    except (EmptyPage, InvalidPage):
        consulta_protocolo = paginator.page(paginator.num_pages)
    context = {
        'suporte': suporte,
        'consulta_protocolo': consulta_protocolo,
        'results': results
    }
    return render(request, template_name, context)


@login_required
def novo_atendimento(request):
    template_name = 'novo-atendimento.html'
    novo_atendimento = 'active'
    data = date.today()
    if request.method == 'POST':
        form = SuporteForm(request.POST)
        if form.is_valid():
            Suporte = form.save(commit=False)
            Suporte.save()
            Suporte.usuario = request.user.cod_empresa
            Suporte.email = request.user.email
            Suporte.telefone = request.user.telefone
            Suporte.protocolo = str(request.user.id) + str(Suporte.id) + str(data.year) + \
                                str(data.month) + str(data.day)
            Suporte.slug = (Suporte.criaslug())
            form.save()
            messages.info(request, 'Atendimento inserido com sucesso!')
            return redirect('suporte')
    else:
        form = SuporteForm()
    context = {
        'form': form,
        'novo_atendimento': novo_atendimento
    }
    return render(request, template_name, context)


@login_required
def protocolo_atendimento(request, slug):
    template_name = 'protocolo-de-atendimento.html'
    protocolo_atendimento = 'active'
    protocolo_de_atendimento = get_object_or_404(Suporte, slug=slug)
    context = {
        'protocolo_atendimento': protocolo_atendimento,
        'protocolo_de_atendimento': protocolo_de_atendimento
    }
    return render(request, template_name, context)


@login_required
def contato(request):
    template_name = 'contato.html'
    data = date.today()
    if request.method == 'POST':
        form = SuporteForm(request.POST)
        if form.is_valid():
            Suporte = form.save(commit=False)
            Suporte.save()
            Suporte.usuario = request.user.cod_empresa
            Suporte.email = request.user.email
            Suporte.telefone = request.user.telefone
            Suporte.protocolo = str(request.user.id) + str(Suporte.id) + str(data.year) + \
                                str(data.month) + str(data.day)
            Suporte.slug = (Suporte.criaslug())
            form.save()
            messages.info(request, 'Mensagem enviada com sucesso!')
            return redirect('index')
    else:
        form = SuporteForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context)


def blank(request):
    template_name = 'blank.html'
    blank = 'active'
    context = {
        'blank': blank
    }
    return render(request, template_name, context)
