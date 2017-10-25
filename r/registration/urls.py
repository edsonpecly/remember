from django.conf.urls import url
from r.registration import views


urlpatterns = [
    url(r'^cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    url(r'^consulta-cliente/', views.consulta_cliente, name='consulta_cliente'),
    url(r'^detalhe-cliente/(?P<slug>[-\w\W\d]+)/$', views.detalhe_cliente, name='detalhe_cliente'),
    url(r'^detalhe-cliente-produto/', views.detalhe_cliente_p, name='detalhe_cliente_p'),
    url(r'^editar-cliente/', views.editar_cliente, name='editar_cliente'),
    url(r'^confirm-del-cliente/', views.confirm_del_cliente, name='confirm_del_cliente'),
    url(r'^deletar-cliente/', views.delete_cliente, name='delete_cliente'),
    url(r'^profissional/', views.cadastro_profissional, name='cadastro_profissional'),
    url(r'^consulta-profissional/', views.consulta_profissional, name='consulta_profissional'),
    url(r'^detalhe-profissional/(?P<slug>[-\w\W\d]+)/$', views.detalhe_profissional, name='detalhe_profissional'),
    url(r'^editar-profissional/', views.editar_profissional, name='editar_profissional'),
    url(r'^servico/', views.cadastro_servico, name='cadastro_servico'),
    url(r'^consulta-servico/', views.consulta_servico, name='consulta_servico'),
    url(r'^detalhe-servico/(?P<slug>[-\w\W\d]+)/$', views.detalhe_servico, name='detalhe_servico'),
    url(r'^editar-servico/', views.editar_servico, name='editar_servico'),
    url(r'^confirm-del-servico/', views.confirm_del_servico, name='confirm_del_servico'),
    url(r'^deletar-servico/', views.delete_servico, name='delete_servico'),
    url(r'^produto/', views.cadastro_produto, name='cadastro_produto'),
    url(r'^consulta-produto/', views.consulta_produto, name='consulta_produto'),
    url(r'^detalhe-produto/(?P<slug>[-\w\W\d]+)/$', views.detalhe_produto, name='detalhe_produto'),
    url(r'^editar-produto/', views.editar_produto, name='editar_produto'),
    url(r'^confirm-del-produto/', views.confirm_del_produto, name='confirm_del_produto'),
    url(r'^deletar-produto/', views.delete_produto, name='delete_produto'),
]