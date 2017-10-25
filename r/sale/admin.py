from django.contrib import admin
from .models import VendaServico, VendaProduto


class VendaServicoAdmin(admin.ModelAdmin):
    list_display = ['empresa', 'cliente', 'servico', 'status']
    list_filter = ['cliente']
    search_fields = ['cliente', 'servico']


class VendaProdutoAdmin(admin.ModelAdmin):
    list_display = ['empresa', 'cliente', 'produto', 'status']
    list_filter = ['cliente']
    search_fields = ['cliente', 'produto']


admin.site.register(VendaServico, VendaServicoAdmin)
admin.site.register(VendaProduto, VendaProdutoAdmin)
