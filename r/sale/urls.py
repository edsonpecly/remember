from django.conf.urls import url
from r.sale import views


urlpatterns = [
    url(r'^servicos/', views.venda_servico, name='venda_servico'),
    url(r'^rel-servicos/', views.rel_venda_servico, name='rel_venda_servico'),
    url(r'^detalhe-venda-servico/(?P<slug>[-\w\W\d]+)/$', views.detalhe_venda_servico, name='detalhe_venda_servico'),
    url(r'^editar-venda-servico/', views.editar_venda_servico, name='editar_venda_servico'),
    url(r'^confirm-del-vservico/', views.confirm_del_vservico, name='confirm_del_vservico'),
    url(r'^deletar-vservico/', views.delete_vservico, name='delete_vservico'),
    url(r'^produto/', views.venda_produto, name='venda_produto'),
    url(r'^rel-produto/', views.rel_venda_produto, name='rel_venda_produto'),
    url(r'^detalhe-venda-produto/(?P<slug>[-\w\W\d]+)/$', views.detalhe_venda_produto, name='detalhe_venda_produto'),
    url(r'^editar-venda-produto/', views.editar_venda_produto, name='editar_venda_produto'),
    url(r'^confirm-del-vproduto/', views.confirm_del_vproduto, name='confirm_del_vproduto'),
    url(r'^deletar-vproduto/', views.delete_vproduto, name='delete_vproduto'),
]