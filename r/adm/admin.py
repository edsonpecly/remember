from django.contrib import admin
from .models import SolicitarPagamento, Suporte


class SolicitarPagamentoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'plano', 'pagamento', 'status']
    search_fields = ['usuario']


class SupoerteAdmin(admin.ModelAdmin):
    list_display = ['protocolo', 'usuario', 'telefone', 'email']
    search_fields = ['usuario']


admin.site.register(SolicitarPagamento, SolicitarPagamentoAdmin)
admin.site.register(Suporte, SupoerteAdmin)
