from .models import DesignSystem, ControleCadastro, ConfigsSistema
from r.sale.models import VendaServico, VendaProduto
from datetime import date, datetime


def design_system(request):
    if request.user.is_authenticated:
        condicao_design = DesignSystem.objects.all()
        condicao_design2 = condicao_design.count()
        if condicao_design2 > 0:
            cores = DesignSystem.objects.get(usuario=str(request.user.id))
        else:
            cores = {}
    else:
        cores = {}
    return {
        'cores': cores
    }


def controle_cadastro(request):
    if request.user.is_authenticated:
        condicao_cadastro = ControleCadastro.objects.all().count()
        if condicao_cadastro > 0:
            try:
                exibir_campo = ControleCadastro.objects.get(usuario=str(request.user.id))
            except ControleCadastro.DoesNotExist:
                exibir_campo = None
        else:
            exibir_campo = {}
    else:
        exibir_campo = {}
    return {
        'exibir_campo': exibir_campo
    }


def configs_sistema(request):
    if request.user.is_authenticated:
        condicao_sistema = ConfigsSistema.objects.all().count()
        if condicao_sistema > 0:
            try:
                configs_sistema = ConfigsSistema.objects.get(usuario=str(request.user.id))
            except ConfigsSistema.DoesNotExist:
                configs_sistema = None
        else:
            configs_sistema = {}
    else:
        configs_sistema = {}
    return {
        'configs_sistema': configs_sistema
    }


def painel_retorno(request):
    if request.user.is_authenticated:
        data = datetime.today()
        condicao_painel_aviso = ConfigsSistema.objects.all().count()
        if condicao_painel_aviso > 0:
            try:
                filtro_retorno = ConfigsSistema.objects.get(usuario=str(request.user.id))
                dias_aviso = filtro_retorno.aviso_retorno
                retorno = date.fromordinal(data.toordinal() + int(dias_aviso))
                aviso = VendaServico.objects.filter(
                    empresa=str(request.user.id)).exclude(retorno__gt=retorno).exclude(status='1').exclude(
                    retorno__lt=data)
                contagem_painel_aviso = aviso.count()
            except ConfigsSistema.DoesNotExist:
                dias_aviso = None
                retorno = None
                aviso = None
                contagem_painel_aviso = None
        else:
            dias_aviso = {}
            retorno = {}
            aviso = {}
            contagem_painel_aviso = {}
    else:
        data = {}
        dias_aviso = {}
        retorno = {}
        aviso = {}
        contagem_painel_aviso = {}
    return {
        'data': data,
        'dias_aviso': dias_aviso,
        'retorno': retorno,
        'aviso': aviso,
        'contagem_painel_aviso': contagem_painel_aviso
    }


def painel_produto(request):
    if request.user.is_authenticated:
        p_data = datetime.today()
        condicao_painel_produto = ConfigsSistema.objects.all().count()
        if condicao_painel_produto > 0:
            try:
                filtro_produto = ConfigsSistema.objects.get(usuario=str(request.user.id))
                p_dias_aviso = filtro_produto.aviso_produto
                p_retorno = date.fromordinal(p_data.toordinal() + int(p_dias_aviso))
                p_aviso = VendaProduto.objects.filter(
                    empresa=str(request.user.id)).exclude(nova_compra__gt=p_retorno).exclude(status='1').exclude(
                    nova_compra__lt=p_data)
                contagem_painel_produto = p_aviso.count()
            except ConfigsSistema.DoesNotExist:
                p_dias_aviso = None
                p_retorno = None
                p_aviso = None
                contagem_painel_produto = None
        else:
            p_dias_aviso = {}
            p_retorno = {}
            p_aviso = {}
            contagem_painel_produto = {}
    else:
        p_data = {}
        p_dias_aviso = {}
        p_retorno = {}
        p_aviso = {}
        contagem_painel_produto = {}
    return {
        'p_data': p_data,
        'p_dias_aviso': p_dias_aviso,
        'p_retorno': p_retorno,
        'p_aviso': p_aviso,
        'contagem_painel_produto': contagem_painel_produto
    }
