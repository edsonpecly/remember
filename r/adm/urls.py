from django.conf.urls import url
from r.adm import views


urlpatterns = [
    url(r'^$', views.venc_planos, name='venc_planos'),
    url(r'^solicitacao-acesso/', views.solicitacao_acesso, name='solicitacao_acesso'),
    url(r'^editar-conta/(?P<slug>[-\w\W\d]+)/$', views.editar_conta, name='editar_conta'),
    url(r'^clientes/', views.adm_clientes, name='adm_clientes'),
    url(r'^clientes-ouro/', views.adm_clientes_ouro, name='adm_clientes_ouro'),
    url(r'^clientes-prata/', views.adm_clientes_prata, name='adm_clientes_prata'),
    url(r'^clientes-bronze/', views.adm_clientes_bronze, name='adm_clientes_bronze'),
]