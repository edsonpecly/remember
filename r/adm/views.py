from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib import messages
from r.core.models import User
from r.core.forms import EditAccountForm


@login_required
def venc_planos(request):
    template_name = 'adm/venc-planos.html'
    venc_planos = User.objects.filter(permissao='0')
    venc_planos2 = 'active'
    context = {
        'venc_planos': venc_planos,
        'venc_planos2': venc_planos2
    }
    return render(request, template_name, context)


@login_required
def solicitacao_acesso(request):
    template_name = 'adm/solicitacao-acesso.html'
    aprovacao = User.objects.filter(permissao='0')
    solicitacao_acesso = 'active'
    context = {
        'solicitacao_acesso': solicitacao_acesso,
        'aprovacao': aprovacao
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
            return redirect('adm:venc_planos')
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
    adm_clientes_all = User.objects.filter(permissao__gte='0').exclude(permissao='10')
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
            results = User.objects.filter(name__icontains=query).exclude(permissao='10').filter(permissao__gte='0')
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
    adm_clientes_all = User.objects.filter(plano__contains='3')
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
