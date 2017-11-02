from django.conf.urls import url
from r.adm import views


urlpatterns = [
    url(r'^$', views.home_adm, name='home_adm'),
    url(r'^venc-planos/', views.venc_planos, name='venc_planos'),
    url(r'^cadastro-vendedor/', views.cadastro_vendedor, name='cadastro_vendedor'),
    url(r'^sistema-revendedores/', views.sistema_revendedores, name='sistema_revendedores'),
    url(r'^venc-planos-boleto/', views.venc_planos_boleto, name='venc_planos_boleto'),
    url(r'^solicitacao-acesso/', views.solicitacao_acesso, name='solicitacao_acesso'),
    url(r'^solicitacao-acesso-boleto/', views.solicitacao_acesso_boleto, name='solicitacao_acesso_boleto'),
    url(r'^editar-conta/(?P<slug>[-\w\W\d]+)/$', views.editar_conta, name='editar_conta'),
    url(r'^clientes/', views.adm_clientes, name='adm_clientes'),
    url(r'^clientes-ouro/', views.adm_clientes_ouro, name='adm_clientes_ouro'),
    url(r'^clientes-prata/', views.adm_clientes_prata, name='adm_clientes_prata'),
    url(r'^clientes-bronze/', views.adm_clientes_bronze, name='adm_clientes_bronze'),
    url(r'^clientes-deb-bol/', views.adm_clientes_boleto, name='adm_clientes_boleto'),
]