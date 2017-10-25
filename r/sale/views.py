from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import date
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from r.registration.models import Cliente
from .forms import VendaServicoForm, EditarVendaServicoForm, VendaProdutoForm, EditarVendaProdutoForm
from .models import VendaServico, VendaProduto


@login_required
def venda_servico(request):
    template_name = 'sale/venda-servico.html'
    venda_servico = 'active'
    user = request.user.id
    if request.method == 'POST':
        form = VendaServicoForm(user, request.POST)
        if form.is_valid():
            VendaServico = form.save(commit=False)
            VendaServico.empresa = request.user.cod_empresa
            VendaServico.save()
            VendaServico.slug = (VendaServico.criaslug())
            VendaServico.periodicidade = VendaServico.servico.periodicidade
            VendaServico.retorno = date.fromordinal(VendaServico.data.toordinal() + int(VendaServico.periodicidade))
            form.save()
            messages.info(request, 'Venda realizada com sucesso!')
            return redirect('sale:rel_venda_servico')
    else:
        form = VendaServicoForm(user)
    context = {
        'venda_servico': venda_servico,
        'form': form
    }
    return render(request, template_name, context)


@login_required
def rel_venda_servico(request):
    template_name = 'sale/rel-venda-servico.html'
    rel_venda_servico = 'active'
    contagem_venda_servico = VendaServico.objects.all().count()
    consulta_venda_servico = VendaServico.objects.filter(empresa=request.user.cod_empresa)
    paginator = Paginator(consulta_venda_servico, 15)
    query = request.GET.get('q')
    results = ''
    try:
        query = str(query)
    except ValueError:
        query = None
        results = None
    if query:
        try:
            results = VendaServico.objects.filter(empresa=request.user.cod_empresa).filter(cliente__nome__icontains=query)
        except VendaServico.DoesNotExist:
            results = None
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        consulta_venda_servico = paginator.page(page)
    except (EmptyPage, InvalidPage):
        consulta_venda_servico = paginator.page(paginator.num_pages)
    context = {
        'rel_venda_servico': rel_venda_servico,
        'contagem_venda_servico': contagem_venda_servico,
        'consulta_venda_servico': consulta_venda_servico,
        'results': results
    }
    return render(request, template_name, context)


@login_required
def detalhe_venda_servico(request, slug):
    template_name = 'sale/detalhe-venda-servico.html'
    var_detalhe_venda_servico = 'active'
    detalhe_venda_servico = get_object_or_404(VendaServico, slug=slug)
    cache_detalhe_venda_servico = detalhe_venda_servico.id
    request.session['cache_detalhe_venda_servico'] = cache_detalhe_venda_servico
    if len(str(detalhe_venda_servico.id)) < 3:
        format_campo = '00'
    context = {
        'detalhe_venda_servico': detalhe_venda_servico,
        'var_detalhe_venda_servico': var_detalhe_venda_servico,
        'format_campo': format_campo
    }
    return render(request, template_name, context)


@login_required
def editar_venda_servico(request):
    template_name = 'sale/editar-venda-servico.html'
    slug = request.session['cache_detalhe_venda_servico']
    detalhe_venda_servico = VendaServico.objects.get(id=slug)
    if request.method == 'POST':
        form = EditarVendaServicoForm(request.POST, instance=detalhe_venda_servico)
        if form.is_valid():
            form.save()
            messages.info(request, 'Alterações gravadas com sucesso')
            return redirect('sale:rel_venda_servico')
    else:
        form = EditarVendaServicoForm(instance=detalhe_venda_servico)
    context = {
        'form': form,
        'detalhe_venda_servico': detalhe_venda_servico
    }
    return render(request, template_name, context)


@login_required
def confirm_del_vservico(request):
    template_name = 'sale/confirm-del-vservico.html'
    slug = request.session['cache_detalhe_venda_servico']
    delete_vservico = VendaServico.objects.get(id=slug)
    context = {
        'delete_vservico': delete_vservico
    }
    return render(request, template_name, context)


@login_required
def delete_vservico(request):
    template_name = 'sale/delete-vservico.html'
    slug = request.session['cache_detalhe_venda_servico']
    delete_vservico = VendaServico.objects.get(id=slug)
    delete_vservico.delete()
    messages.info(request, 'Venda excluída com Sucesso!')
    return render(request, template_name)


@login_required
def venda_produto(request):
    template_name = 'sale/venda-produto.html'
    venda_produto = 'active'
    user = request.user.id
    if request.method == 'POST':
        form = VendaProdutoForm(user, request.POST)
        if form.is_valid():
            VendaProduto = form.save(commit=False)
            VendaProduto.empresa = request.user.cod_empresa
            VendaProduto.save()
            VendaProduto.slug = (VendaProduto.criaslug())
            VendaProduto.periodicidade = VendaProduto.produto.periodicidade
            VendaProduto.nova_compra = date.fromordinal(VendaProduto.data.toordinal() + int(VendaProduto.periodicidade))
            form.save()
            messages.info(request, 'Venda realizada com sucesso!')
            return redirect('sale:rel_venda_produto')
    else:
        form = VendaProdutoForm(user)
    context = {
        'venda_produto': venda_produto,
        'form': form
    }
    return render(request, template_name, context)


@login_required
def rel_venda_produto(request):
    template_name = 'sale/rel-venda-produto.html'
    rel_venda_produto = 'active'
    contagem_venda_produto = VendaProduto.objects.all().count()
    consulta_venda_produto = VendaProduto.objects.filter(empresa=request.user.cod_empresa)
    paginator = Paginator(consulta_venda_produto, 15)
    query = request.GET.get('q')
    results = ''
    try:
        query = str(query)
    except ValueError:
        query = None
        results = None
    if query:
        try:
            results = VendaProduto.objects.filter(
                empresa=request.user.cod_empresa).filter(cliente__nome__icontains=query)
        except VendaProduto.DoesNotExist:
            results = None
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        consulta_venda_produto = paginator.page(page)
    except (EmptyPage, InvalidPage):
        consulta_venda_produto = paginator.page(paginator.num_pages)
    context = {
        'rel_venda_produto': rel_venda_produto,
        'contagem_venda_produto': contagem_venda_produto,
        'consulta_venda_produto': consulta_venda_produto,
        'results': results
    }
    return render(request, template_name, context)


@login_required
def detalhe_venda_produto(request, slug):
    template_name = 'sale/detalhe-venda-produto.html'
    var_detalhe_venda_produto = 'active'
    detalhe_venda_produto = get_object_or_404(VendaProduto, slug=slug)
    cache_detalhe_venda_produto = detalhe_venda_produto.id
    request.session['cache_detalhe_venda_produto'] = cache_detalhe_venda_produto
    if len(str(detalhe_venda_produto.id)) < 3:
        format_campo = '00'
    context = {
        'detalhe_venda_produto': detalhe_venda_produto,
        'var_detalhe_venda_produto': var_detalhe_venda_produto,
        'format_campo': format_campo
    }
    return render(request, template_name, context)


@login_required
def editar_venda_produto(request):
    template_name = 'sale/editar-venda-produto.html'
    slug = request.session['cache_detalhe_venda_produto']
    detalhe_venda_produto = VendaProduto.objects.get(id=slug)
    if request.method == 'POST':
        form = EditarVendaProdutoForm(request.POST, instance=detalhe_venda_produto)
        if form.is_valid():
            form.save()
            messages.info(request, 'Alterações gravadas com sucesso')
            return redirect('sale:rel_venda_produto')
    else:
        form = EditarVendaProdutoForm(instance=detalhe_venda_produto)
    context = {
        'form': form,
        'detalhe_venda_produto': detalhe_venda_produto
    }
    return render(request, template_name, context)


@login_required
def confirm_del_vproduto(request):
    template_name = 'sale/confirm-del-vproduto.html'
    slug = request.session['cache_detalhe_venda_produto']
    delete_vproduto = VendaProduto.objects.get(id=slug)
    context = {
        'delete_vproduto': delete_vproduto
    }
    return render(request, template_name, context)


@login_required
def delete_vproduto(request):
    template_name = 'sale/delete-vproduto.html'
    slug = request.session['cache_detalhe_venda_produto']
    delete_vproduto = VendaProduto.objects.get(id=slug)
    delete_vproduto.delete()
    messages.info(request, 'Venda excluída com Sucesso!')
    return render(request, template_name)
