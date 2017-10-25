from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from r.sale.models import VendaServico, VendaProduto
from django.contrib import messages
from .models import Cliente, Profissional, Servico, Produto
from .forms import ClienteForm, ProfissionalForm, ServicoForm, ProdutoForm


@login_required
def cadastro_cliente(request):
    template_name = 'registration/cadastro-cliente.html'
    cadastro_cliente = 'active'
    form = ClienteForm(request.POST or None)
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            Cliente = form.save(commit=False)
            Cliente.save()
            Cliente.empresa = request.user.cod_empresa
            Cliente.slug = (Cliente.criaslug())
            form.save()
            messages.info(request, 'Cliente cadastrado com sucesso')
            return redirect('registration:consulta_cliente')
    else:
        form = ClienteForm()
    context = {
        'form': form,
        'cadastro_cliente': cadastro_cliente
    }
    return render(request, template_name, context)


@login_required
def consulta_cliente(request):
    template_name = 'registration/consulta-cliente.html'
    var_consulta_cliente = 'active'
    contagem_cliente = Cliente.objects.all().count()
    consulta_cliente = Cliente.objects.filter(empresa=request.user.cod_empresa)
    paginator = Paginator(consulta_cliente, 15)
    query = request.GET.get('q')
    results = ''
    try:
        query = str(query)
    except ValueError:
        query = None
        results = None
    if query:
        try:
            results = Cliente.objects.filter(empresa=request.user.cod_empresa).filter(nome__icontains=query)
        except Cliente.DoesNotExist:
            results = None
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        consulta_cliente = paginator.page(page)
    except (EmptyPage, InvalidPage):
        consulta_cliente = paginator.page(paginator.num_pages)
    context = {
        'var_consulta_cliente': var_consulta_cliente,
        'consulta_cliente': consulta_cliente,
        'contagem_cliente': contagem_cliente,
        'results': results
    }
    return render(request, template_name, context)


@login_required
def detalhe_cliente(request, slug):
    template_name = 'registration/detalhe-cliente.html'
    var_detalhe_cliente = 'active'
    detalhe_cliente = get_object_or_404(Cliente, slug=slug)
    cache_detalhe_cliente = detalhe_cliente.id
    request.session['cache_detalhe_cliente'] = cache_detalhe_cliente
    pag_servico = VendaServico.objects.filter(empresa=request.user.cod_empresa).filter(cliente=detalhe_cliente)
    paginator = Paginator(pag_servico, 5)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        pag_servico = paginator.page(page)
    except (EmptyPage, InvalidPage):
        pag_servico = paginator.page(paginator.num_pages)
    context = {
        'detalhe_cliente': detalhe_cliente,
        'var_detalhe_cliente': var_detalhe_cliente,
        'pag_servico': pag_servico,
    }
    return render(request, template_name, context)


@login_required
def detalhe_cliente_p(request):
    template_name = 'registration/detalhe-cliente-p.html'
    var_detalhe_cliente = 'active'
    slug = request.session['cache_detalhe_cliente']
    detalhe_cliente = Cliente.objects.get(slug=slug)
    pag_produto = VendaProduto.objects.filter(empresa=request.user.cod_empresa).filter(cliente=detalhe_cliente)
    paginator = Paginator(pag_produto, 5)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        pag_produto = paginator.page(page)
    except (EmptyPage, InvalidPage):
        pag_produto = paginator.page(paginator.num_pages)
    context = {
        'detalhe_cliente': detalhe_cliente,
        'var_detalhe_cliente': var_detalhe_cliente,
        'pag_produto': pag_produto,
    }
    return render(request, template_name, context)


@login_required
def editar_cliente(request):
    template_name = 'registration/editar-cliente.html'
    slug = request.session['cache_detalhe_cliente']
    detalhe_cliente = Cliente.objects.get(slug=slug)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=detalhe_cliente)
        if form.is_valid():
            form.save()
            messages.info(request, 'Alterações gravadas com sucesso')
            return redirect('registration:consulta_cliente')
    else:
        form = ClienteForm(instance=detalhe_cliente)
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def confirm_del_cliente(request):
    template_name = 'registration/confirm-del-cliente.html'
    slug = request.session['cache_detalhe_cliente']
    detalhe_cliente = Cliente.objects.get(id=slug)
    context = {
        'detalhe_cliente': detalhe_cliente
    }
    return render(request, template_name, context)


@login_required
def delete_cliente(request):
    template_name = 'registration/delete-cliente.html'
    slug = request.session['cache_detalhe_cliente']
    detalhe_cliente = Cliente.objects.get(id=slug)
    detalhe_cliente.delete()
    messages.info(request, 'Cliente excluído com Sucesso!')
    return render(request, template_name)


@login_required
def cadastro_profissional(request):
    template_name = 'registration/cadastro-profissional.html'
    cadastro_profissional = 'active'
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)
        if form.is_valid():
            Profissional = form.save(commit=False)
            Profissional.save()
            Profissional.empresa = request.user.cod_empresa
            Profissional.slug = (Profissional.criaslug())
            form.save()
            messages.info(request, 'Profissional cadastrado com sucesso')
            return redirect('registration:consulta_profissional')
    else:
        form = ProfissionalForm()
    context = {
        'form': form,
        'cadastro_profissional': cadastro_profissional
    }
    return render(request, template_name, context)


@login_required
def consulta_profissional(request):
    template_name = 'registration/consulta-profissional.html'
    var_consulta_profissional = 'active'
    contagem_profissional = Profissional.objects.all().count()
    consulta_profissional = Profissional.objects.filter(empresa=request.user.cod_empresa)
    paginator = Paginator(consulta_profissional, 15)
    query = request.GET.get('q')
    results = ''
    try:
        query = str(query)
    except ValueError:
        query = None
        results = None
    if query:
        try:
            results = Profissional.objects.filter(empresa=request.user.cod_empresa).filter(nome__icontains=query)
        except Profissional.DoesNotExist:
            results = None
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        consulta_profissional = paginator.page(page)
    except (EmptyPage, InvalidPage):
        consulta_profissional = paginator.page(paginator.num_pages)
    context = {
        'var_consulta_profissional': var_consulta_profissional,
        'consulta_profissional': consulta_profissional,
        'contagem_profissional': contagem_profissional,
        'results': results
    }
    return render(request, template_name, context)


@login_required
def detalhe_profissional(request, slug):
    template_name = 'registration/detalhe-profissional.html'
    var_detalhe_profissional = 'active'
    detalhe_profissional = get_object_or_404(Profissional, slug=slug)
    cache_detalhe_profissional = detalhe_profissional.id
    request.session['cache_detalhe_profissional'] = cache_detalhe_profissional
    context = {
        'detalhe_profissional': detalhe_profissional,
        'var_detalhe_profissional': var_detalhe_profissional
    }
    return render(request, template_name, context)


@login_required
def editar_profissional(request):
    template_name = 'registration/editar-profissional.html'
    slug = request.session['cache_detalhe_profissional']
    detalhe_profissional = Profissional.objects.get(id=slug)
    if request.method == 'POST':
        form = ProfissionalForm(request.POST, instance=detalhe_profissional)
        if form.is_valid():
            form.save()
            messages.info(request, 'Alterações gravadas com sucesso')
            return redirect('registration:consulta_profissional')
    else:
        form = ProfissionalForm(instance=detalhe_profissional)
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def cadastro_servico(request):
    template_name = 'registration/cadastro-servico.html'
    cadastro_servico = 'active'
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            Servico = form.save(commit=False)
            Servico.save()
            Servico.empresa = request.user.cod_empresa
            Servico.slug = (Servico.criaslug())
            form.save()
            messages.info(request, 'Serviço cadastrado com sucesso')
            return redirect('registration:consulta_servico')
    else:
        form = ServicoForm()
    context = {
        'form': form,
        'cadastro_servico': cadastro_servico
    }
    return render(request, template_name, context)


@login_required
def consulta_servico(request):
    template_name = 'registration/consulta-servico.html'
    var_consulta_servico = 'active'
    contagem_servico = Servico.objects.all().count()
    consulta_servico = Servico.objects.filter(empresa=request.user.cod_empresa)
    paginator = Paginator(consulta_servico, 15)
    query = request.GET.get('q')
    results = ''
    try:
        query = str(query)
    except ValueError:
        query = None
        results = None
    if query:
        try:
            results = Servico.objects.filter(empresa=request.user.cod_empresa).filter(nome__icontains=query)
        except Servico.DoesNotExist:
            results = None
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        consulta_servico = paginator.page(page)
    except (EmptyPage, InvalidPage):
        consulta_servico = paginator.page(paginator.num_pages)
    context = {
        'var_consulta_servico': var_consulta_servico,
        'consulta_servico': consulta_servico,
        'contagem_servico': contagem_servico,
        'results': results
    }
    return render(request, template_name, context)


@login_required
def detalhe_servico(request, slug):
    template_name = 'registration/detalhe-servico.html'
    var_detalhe_servico = 'active'
    detalhe_servico = get_object_or_404(Servico, slug=slug)
    cache_detalhe_servico = detalhe_servico.id
    request.session['cache_detalhe_servico'] = cache_detalhe_servico
    total_vendas = VendaServico.objects.filter(empresa=request.user.cod_empresa).filter(servico=detalhe_servico).count()
    context = {
        'detalhe_servico': detalhe_servico,
        'var_detalhe_servico': var_detalhe_servico,
        'total_vendas': total_vendas
    }
    return render(request, template_name, context)


@login_required
def editar_servico(request):
    template_name = 'registration/editar-servico.html'
    slug = request.session['cache_detalhe_servico']
    detalhe_servico = Servico.objects.get(id=slug)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=detalhe_servico)
        if form.is_valid():
            form.save()
            messages.info(request, 'Alterações gravadas com sucesso')
            return redirect('registration:consulta_servico')
    else:
        form = ServicoForm(instance=detalhe_servico)
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def confirm_del_servico(request):
    template_name = 'registration/confirm-del-servico.html'
    slug = request.session['cache_detalhe_servico']
    detalhe_servico = Servico.objects.get(id=slug)
    context = {
        'detalhe_servico': detalhe_servico
    }
    return render(request, template_name, context)


@login_required
def delete_servico(request):
    template_name = 'registration/delete-servico.html'
    slug = request.session['cache_detalhe_servico']
    detalhe_servico = Servico.objects.get(id=slug)
    detalhe_servico.delete()
    messages.info(request, 'Serviço excluído com Sucesso!')
    return render(request, template_name)


@login_required
def cadastro_produto(request):
    template_name = 'registration/cadastro-produto.html'
    cadastro_produto = 'active'
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            Produto = form.save(commit=False)
            Produto.save()
            Produto.empresa = request.user.cod_empresa
            Produto.slug = (Produto.criaslug())
            form.save()
            messages.info(request, 'Produto cadastrado com sucesso')
            return redirect('registration:consulta_produto')
    else:
        form = ProdutoForm()
    context = {
        'form': form,
        'cadastro_produto': cadastro_produto
    }
    return render(request, template_name, context)


@login_required
def consulta_produto(request):
    template_name = 'registration/consulta-produto.html'
    var_consulta_produto = 'active'
    contagem_produto = Produto.objects.all().count()
    consulta_produto = Produto.objects.filter(empresa=request.user.cod_empresa)
    paginator = Paginator(consulta_produto, 15)
    query = request.GET.get('q')
    results = ''
    try:
        query = str(query)
    except ValueError:
        query = None
        results = None
    if query:
        try:
            results = Produto.objects.filter(empresa=request.user.cod_empresa).filter(nome__icontains=query)
        except Produto.DoesNotExist:
            results = None
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        consulta_produto = paginator.page(page)
    except (EmptyPage, InvalidPage):
        consulta_produto = paginator.page(paginator.num_pages)
    context = {
        'var_consulta_produto': var_consulta_produto,
        'consulta_produto': consulta_produto,
        'contagem_produto': contagem_produto,
        'results': results
    }
    return render(request, template_name, context)


@login_required
def detalhe_produto(request, slug):
    template_name = 'registration/detalhe-produto.html'
    var_detalhe_produto = 'active'
    detalhe_produto = get_object_or_404(Produto, slug=slug)
    cache_detalhe_produto = detalhe_produto.id
    request.session['cache_detalhe_produto'] = cache_detalhe_produto
    context = {
        'detalhe_produto': detalhe_produto,
        'var_detalhe_produto': var_detalhe_produto
    }
    return render(request, template_name, context)


@login_required
def editar_produto(request):
    template_name = 'registration/editar-produto.html'
    slug = request.session['cache_detalhe_produto']
    detalhe_produto = Produto.objects.get(id=slug)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=detalhe_produto)
        if form.is_valid():
            form.save()
            messages.info(request, 'Alterações gravadas com sucesso')
            return redirect('registration:consulta_produto')
    else:
        form = ProdutoForm(instance=detalhe_produto)
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def confirm_del_produto(request):
    template_name = 'registration/confirm-del-produto.html'
    slug = request.session['cache_detalhe_produto']
    detalhe_produto = Produto.objects.get(id=slug)
    context = {
        'detalhe_produto': detalhe_produto
    }
    return render(request, template_name, context)


@login_required
def delete_produto(request):
    template_name = 'registration/delete-produto.html'
    slug = request.session['cache_detalhe_produto']
    detalhe_produto = Produto.objects.get(id=slug)
    detalhe_produto.delete()
    messages.info(request, 'Produto excluído com Sucesso!')
    return render(request, template_name)
