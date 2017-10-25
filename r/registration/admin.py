from django.contrib import admin
from .models import Cliente, Profissional, Servico, Produto


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'created_at']
    search_fields = ['nome']


class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'created_at']
    search_fields = ['nome']


class ServicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'periodicidade', 'valor', 'created_at']
    search_fields = ['nome']


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'periodicidade', 'custo', 'valor', 'created_at']
    search_fields = ['nome']


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Profissional, ProfissionalAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Produto, ProdutoAdmin)
