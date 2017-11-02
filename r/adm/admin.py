from django.contrib import admin
from .models import SolicitarPagamento, Suporte, Vendedor, CadastroVendedor, InserirComissao, PagarComissao


class SolicitarPagamentoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'plano', 'pagamento', 'status']
    search_fields = ['usuario']


class SupoerteAdmin(admin.ModelAdmin):
    list_display = ['protocolo', 'usuario', 'telefone', 'email']
    search_fields = ['usuario']


class VendedorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'comissao']
    search_fields = ['nome']


class CadastroVendedorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'status', 'telefone']
    search_fields = ['nome']


class InserirComissaoAdmin(admin.ModelAdmin):
    list_display = ['vendedor', 'cliente', 'valor', 'created_at']
    search_fields = ['vendedor']


class PagarComissaoAdmin(admin.ModelAdmin):
    list_display = ['vendedor', 'valor', 'status', 'created_at']
    search_fields = ['vendedor']


admin.site.register(SolicitarPagamento, SolicitarPagamentoAdmin)
admin.site.register(Suporte, SupoerteAdmin)
admin.site.register(Vendedor, VendedorAdmin)
admin.site.register(CadastroVendedor, CadastroVendedorAdmin)
admin.site.register(InserirComissao, InserirComissaoAdmin)
admin.site.register(PagarComissao, PagarComissaoAdmin)
