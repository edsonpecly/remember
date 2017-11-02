from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib import messages
from r.core.models import User
from r.core.forms import EditAccountForm
from .models import SolicitarPagamento, Suporte, CadastroVendedor
from .forms import CadastroVendedorForm
from datetime import datetime


@login_required
def home_adm(request):
    template_name = 'adm/home-adm.html'
    home_adm = 'active'
    clientes_boleto = User.objects.exclude(tipo_pagamento='3').exclude(permissao='0').exclude(permissao=10).count()
    c_aprovacao = User.objects.filter(permissao='0').filter(tipo_pagamento='3').count()
    c_sol_pagamento = SolicitarPagamento.objects.filter(status='1').count()
    c_suporte_1 = Suporte.objects.filter(status='1').filter(solicitacao='1').count()
    c_suporte_2 = Suporte.objects.filter(status='1').filter(solicitacao='2').count()
    c_suporte_3 = Suporte.objects.filter(status='1').filter(solicitacao='3').count()
    c_suporte_4 = Suporte.objects.filter(status='1').filter(solicitacao='4').count()
    c_suporte_5 = Suporte.objects.filter(status='1').filter(solicitacao='5').count()
    c_suporte_6 = Suporte.objects.filter(status='1').filter(solicitacao='6').count()
    dia = f"{datetime.now():%d}"
    mes = f"{datetime.now():%m}"
    ano = f"{datetime.now():%Y}"
    limite_10 = int(dia) - 10
    a_vencer = int(dia) + 2
    contagem_venc = User.objects.filter(fim_ciclo__day__gte=limite_10).filter(fim_ciclo__day__lte=a_vencer).filter(
        fim_ciclo__month=mes).filter(fim_ciclo__year=ano).count()
    contagem_venc_boleto = User.objects.filter(fim_ciclo__day__gte=limite_10).filter(fim_ciclo__day__lte=a_vencer).filter(
        fim_ciclo__month=mes).filter(fim_ciclo__year=ano).exclude(tipo_pagamento='3').count()
    context = {
        'home_adm': home_adm,
        'c_aprovacao': c_aprovacao,
        'c_sol_pagamento': c_sol_pagamento,
        'c_suporte_1': c_suporte_1,
        'c_suporte_2': c_suporte_2,
        'c_suporte_3': c_suporte_3,
        'c_suporte_4': c_suporte_4,
        'c_suporte_5': c_suporte_5,
        'c_suporte_6': c_suporte_6,
        'contagem_venc': contagem_venc,
        'clientes_boleto': clientes_boleto,
        'contagem_venc_boleto': contagem_venc_boleto,
    }
    return render(request, template_name, context)


def cadastro_vendedor(request):
    template_name = 'cadastro-vendedor.html'
    if request.method == 'POST':
        form = CadastroVendedorForm(request.POST)
        if form.is_valid():
            CadastroVendedor = form.save(commit=False)
            if CadastroVendedor.termos == False:
                messages.info(request, ' Você precisa concordar com os Termos do Sistema de Revendedor')
                form = CadastroVendedorForm(request.POST)
            else:
                form.save()
                CadastroVendedor.slug = (CadastroVendedor.criaslug())
                CadastroVendedor.status = '1'
                form.save()
                messages.info(request, 'Cadastro realizado com sucesso!')
                return redirect('index')
        else:
            messages.info(request, 'Deu Errado')
    else:
        form = CadastroVendedorForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context)

def sistema_revendedores(request):
    template_name = 'sistema-revendedores.html'
    return render(request, template_name)


@login_required
def venc_planos(request):
    template_name = 'adm/venc-planos.html'
    venc_planos2 = 'active'
    dia = f"{datetime.now():%d}"
    mes = f"{datetime.now():%m}"
    ano = f"{datetime.now():%Y}"
    limite_10 = int(dia) - 20
    limite_7 = int(dia) - 7
    limite_5 = int(dia) - 5
    limite_3 = int(dia) - 3
    a_vencer = int(dia) + 2
    venc_limite_10 = User.objects.filter(fim_ciclo__day__gte=limite_10).filter(fim_ciclo__day__lt=limite_7).filter(
        fim_ciclo__month=mes).filter(fim_ciclo__year=ano).order_by('fim_ciclo')
    venc_limite_7 = User.objects.filter(fim_ciclo__day__gte=limite_7).filter(fim_ciclo__day__lt=limite_5).filter(
        fim_ciclo__month=mes).filter(fim_ciclo__year=ano).order_by('fim_ciclo')
    venc_limite_5 = User.objects.filter(fim_ciclo__day__gte=limite_5).filter(fim_ciclo__day__lt=limite_3).filter(
        fim_ciclo__month=mes).filter(fim_ciclo__year=ano).order_by('fim_ciclo')
    venc_limite_3 = User.objects.filter(fim_ciclo__day__gte=limite_3).filter(fim_ciclo__day__lte=dia).filter(
        fim_ciclo__month=mes).filter(fim_ciclo__year=ano).order_by('fim_ciclo')
    venc_futuro = User.objects.filter(fim_ciclo__day__gt=dia).filter(fim_ciclo__day__lte=a_vencer).filter(
        fim_ciclo__month=mes).filter(fim_ciclo__year=ano).order_by('fim_ciclo')
    contagem_venc = User.objects.filter(fim_ciclo__day__gte=limite_10).filter(fim_ciclo__day__lte=a_vencer).filter(
        fim_ciclo__month=mes).filter(fim_ciclo__year=ano).count()
    context = {
        'venc_planos': venc_planos,
        'venc_planos2': venc_planos2,
        'venc_limite_10': venc_limite_10,
        'venc_limite_7': venc_limite_7,
        'venc_limite_5': venc_limite_5,
        'venc_limite_3': venc_limite_3,
        'venc_futuro': venc_futuro,
        'a_vencer': a_vencer,
        'limite_10': limite_10,
        'limite_7': limite_7,
        'limite_5': limite_5,
        'limite_3': limite_3,
        'contagem_venc': contagem_venc,
    }
    return render(request, template_name, context)


@login_required
def venc_planos_boleto(request):
    template_name = 'adm/venc-planos-boleto.html'
    venc_planos_boleto = 'active'
    dia = f"{datetime.now():%d}"
    mes = f"{datetime.now():%m}"
    ano = f"{datetime.now():%Y}"
    limite_10 = int(dia) - 20
    limite_7 = int(dia) - 7
    limite_5 = int(dia) - 5
    limite_3 = int(dia) - 3
    a_vencer = int(dia) + 2
    venc_limite_10 = User.objects.filter(fim_ciclo__day__gte=limite_10).filter(fim_ciclo__day__lt=limite_7).filter(
        fim_ciclo__month=mes).filter(fim_ciclo__year=ano).exclude(tipo_pagamento='3').order_by('fim_ciclo')
    venc_limite_7 = User.objects.filter(fim_ciclo__day__gte=limite_7).filter(fim_ciclo__day__lt=limite_5).filter(
        fim_ciclo__month=mes).filter(fim_ciclo__year=ano).exclude(tipo_pagamento='3').order_by('fim_ciclo')
    venc_limite_5 = User.objects.filter(fim_ciclo__day__gte=limite_5).filter(fim_ciclo__day__lt=limite_3).filter(
        fim_ciclo__month=mes).filter(fim_ciclo__year=ano).exclude(tipo_pagamento='3').order_by('fim_ciclo')
    venc_limite_3 = User.objects.filter(fim_ciclo__day__gte=limite_3).filter(fim_ciclo__day__lte=dia).filter(
        fim_ciclo__month=mes).filter(fim_ciclo__year=ano).exclude(tipo_pagamento='3').order_by('fim_ciclo')
    venc_futuro = User.objects.filter(fim_ciclo__day__gt=dia).filter(fim_ciclo__day__lte=a_vencer).filter(
        fim_ciclo__month=mes).filter(fim_ciclo__year=ano).exclude(tipo_pagamento='3').order_by('fim_ciclo')
    contagem_venc = User.objects.filter(fim_ciclo__day__gte=limite_10).filter(fim_ciclo__day__lte=a_vencer).filter(
        fim_ciclo__month=mes).filter(fim_ciclo__year=ano).exclude(tipo_pagamento='3').count()
    context = {
        'venc_planos': venc_planos,
        'venc_planos_boleto': venc_planos_boleto,
        'venc_limite_10': venc_limite_10,
        'venc_limite_7': venc_limite_7,
        'venc_limite_5': venc_limite_5,
        'venc_limite_3': venc_limite_3,
        'venc_futuro': venc_futuro,
        'a_vencer': a_vencer,
        'limite_10': limite_10,
        'limite_7': limite_7,
        'limite_5': limite_5,
        'limite_3': limite_3,
        'contagem_venc': contagem_venc,
    }
    return render(request, template_name, context)


@login_required
def solicitacao_acesso(request):
    template_name = 'adm/solicitacao-acesso.html'
    aprovacao = User.objects.filter(permissao='0').filter(tipo_pagamento='3')
    c_aprovacao = User.objects.filter(permissao='0').filter(tipo_pagamento='3').count()
    solicitacao_acesso = 'active'
    context = {
        'solicitacao_acesso': solicitacao_acesso,
        'aprovacao': aprovacao,
        'c_aprovacao': c_aprovacao
    }
    return render(request, template_name, context)


@login_required
def solicitacao_acesso_boleto(request):
    template_name = 'adm/solicitacao-acesso-boleto.html'
    aprovacao = User.objects.filter(permissao='0').exclude(tipo_pagamento='3')
    c_aprovacao = User.objects.filter(permissao='0').exclude(tipo_pagamento='3').count()
    solicitacao_acesso_boleto = 'active'
    context = {
        'solicitacao_acesso_boleto': solicitacao_acesso_boleto,
        'aprovacao': aprovacao,
        'c_aprovacao': c_aprovacao
    }
    return render(request, template_name, context)


@login_required
def editar_conta(request, slug):
    template_name = 'adm/editar-conta.html'
    editar_conta = get_object_or_404(User, slug=slug)
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=editar_conta)
        if form.is_valid():
            form.save()
            messages.info(request, 'Alterações realizadas com sucesso')
            form = EditAccountForm(request.POST, instance=editar_conta)
    else:
        form = EditAccountForm(instance=editar_conta)
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def adm_clientes(request):
    template_name = 'adm/clientes.html'
    adm_clientes = 'active'
    adm_clientes_all = User.objects.filter(permissao__lt=10).exclude(permissao=0).order_by('plano')
    paginator = Paginator(adm_clientes_all, 15)
    query = request.GET.get('q')
    results = ''
    try:
        query = str(query)
    except ValueError:
        query = None
        results = None
    if query:
        try:
            results = User.objects.filter(name__icontains=query).filter(permissao__lt=10).exclude(permissao=0)
        except User.DoesNotExist:
            results = None
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        adm_clientes_all = paginator.page(page)
    except (EmptyPage, InvalidPage):
        adm_clientes_all = paginator.page(paginator.num_pages)
    context = {
        'adm_clientes': adm_clientes,
        'adm_clientes_all': adm_clientes_all,
        'results': results
    }
    return render(request, template_name, context)


@login_required
def adm_clientes_ouro(request):
    template_name = 'adm/clientes-ouro.html'
    adm_clientes = 'active'
    adm_clientes_all = User.objects.filter(plano__contains='1')
    paginator = Paginator(adm_clientes_all, 15)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        adm_clientes_all = paginator.page(page)
    except (EmptyPage, InvalidPage):
        adm_clientes_all = paginator.page(paginator.num_pages)
    context = {
        'adm_clientes': adm_clientes,
        'adm_clientes_all': adm_clientes_all,
    }
    return render(request, template_name, context)


@login_required
def adm_clientes_prata(request):
    template_name = 'adm/clientes-prata.html'
    adm_clientes = 'active'
    adm_clientes_all = User.objects.filter(plano__contains='2')
    paginator = Paginator(adm_clientes_all, 15)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        adm_clientes_all = paginator.page(page)
    except (EmptyPage, InvalidPage):
        adm_clientes_all = paginator.page(paginator.num_pages)
    context = {
        'adm_clientes': adm_clientes,
        'adm_clientes_all': adm_clientes_all,
    }
    return render(request, template_name, context)


@login_required
def adm_clientes_bronze(request):
    template_name = 'adm/clientes-bronze.html'
    adm_clientes = 'active'
    adm_clientes_all = User.objects.filter(plano=3).exclude(permissao=0)
    paginator = Paginator(adm_clientes_all, 15)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        adm_clientes_all = paginator.page(page)
    except (EmptyPage, InvalidPage):
        adm_clientes_all = paginator.page(paginator.num_pages)
    context = {
        'adm_clientes': adm_clientes,
        'adm_clientes_all': adm_clientes_all,
    }
    return render(request, template_name, context)


@login_required
def adm_clientes_boleto(request):
    template_name = 'adm/clientes-deb-bol.html'
    adm_clientes = 'active'
    clientes_boleto = User.objects.exclude(tipo_pagamento='3').exclude(
        permissao=0).exclude(permissao=10).order_by('plano')
    paginator = Paginator(clientes_boleto, 15)
    query = request.GET.get('q')
    results = ''
    try:
        query = str(query)
    except ValueError:
        query = None
        results = None
    if query:
        try:
            results = User.objects.filter(name__icontains=query).exclude(tipo_pagamento='3').exclude(
                permissao=0).exclude(permissao=10)
        except User.DoesNotExist:
            results = None
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        clientes_boleto = paginator.page(page)
    except (EmptyPage, InvalidPage):
        clientes_boleto = paginator.page(paginator.num_pages)
    context = {
        'adm_clientes': adm_clientes,
        'clientes_boleto': clientes_boleto,
        'results': results
    }
    return render(request, template_name, context)
