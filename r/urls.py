from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from r.core import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', login, {'template_name': 'login.html'}, name='login'),
    url(r'^adm/', include('r.adm.urls', namespace='adm')),
    url(r'^cadastros/', include('r.registration.urls', namespace='registration')),
    url(r'^vendas/', include('r.sale.urls', namespace='sale')),
    url(r'^logout/', logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^cadastro-usuario/', views.cadastro_usuario, name='cadastro_usuario'),
    url(r'^resetar-senha/', views.resetar_senha, name='resetar_senha'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$', views.password_reset_confirm, name='confirmar_nova_senha'),
    url(r'^planos-assinatura/', views.planos_assinatura, name='planos_assinatura'),
    url(r'^deposito-boleto/', views.deposito_boleto, name='deposito_boleto'),
    url(r'^plano-ouro/', views.plano_ouro, name='plano_ouro'),
    url(r'^plano-prata/', views.plano_prata, name='plano_prata'),
    url(r'^plano-bronze/', views.plano_bronze, name='plano_bronze'),
    url(r'^cadastro-realizado/', views.cadastro_realizado, name='cadastro_realizado'),
    url(r'^home/', views.home, name='home'),
    url(r'^aviso-retorno/', views.aviso_retorno, name='aviso_retorno'),
    url(r'^aviso-produto/', views.aviso_produto, name='aviso_produto'),
    url(r'^aviso-aniversario/', views.aviso_aniversario, name='aviso_aniversario'),
    url(r'^info-gerais/', views.info_gerais, name='info_gerais'),
    url(r'^editar-informacoes/', views.editar_informacoes, name='editar_informacoes'),
    url(r'^editar-senha/', views.editar_senha, name='editar_senha'),
    url(r'^design/', views.design, name='design'),
    url(r'^editar-design/', views.editar_design, name='editar_design'),
    url(r'^ctrl-cadastro/', views.ctrl_cadastro, name='ctrl_cadastro'),
    url(r'^editar-ctrl-cadastro/', views.editar_ctrl_cadastro, name='editar_ctrl_cadastro'),
    url(r'^config-gerais/', views.config_gerais, name='config_gerais'),
    url(r'^editar-config-gerais/', views.editar_config_gerais, name='editar_config_gerais'),
    url(r'^suporte/', views.suporte, name='suporte'),
    url(r'^novo-atendimento/', views.novo_atendimento, name='novo_atendimento'),
    url(
        r'^protocolo-de-atendimento/(?P<slug>[-\w\W\d]+)/$', views.protocolo_atendimento,
        name='protocolo_de_atendimento'
    ),
    url(r'^em-construcao/', views.blank, name='blank'),
    url(r'^aguarde-aprovacao/', views.aguarde_aprovacao, name='aguarde_aprovacao'),
    url(r'^admin/', admin.site.urls),
]
