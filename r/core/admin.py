from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, DesignSystem, ControleCadastro, ConfigsSistema, PasswordReset
from .forms import UserAdminCreationForm, UserAdminForm


class UserAdmin(BaseUserAdmin):

    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2')
        }),
    )
    form = UserAdminForm
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'permissao', 'slug')
        }),
        ('Informações Básicas', {
            'fields': (
                'name', 'cod_empresa', 'vendedor', 'endereco', 'nome_empresa', 'telefone', 'whatsapp',
                'last_login'
            )
        }),
        ('Assinatura', {
            'fields': ('plano', 'tipo_pagamento', 'inicio_ciclo', 'fim_ciclo')
        }),
        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
    )
    list_display = ['email', 'name', 'permissao', 'vendedor']


class PasswordResetAdmin(admin.ModelAdmin):
    list_display = ['user', 'key', 'created_at', 'confirmed']


class DesignSystemAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'cor_topo', 'cor_pn_retorno', 'cor_pn_aniversario', 'cor_pn_produto', 'slug']
    search_fields = ['usuario']


class ControleCadastroAdmin(admin.ModelAdmin):
    list_display = ['usuario']
    search_fields = ['usuario']


class ConfigsSistemaAdmin(admin.ModelAdmin):
    list_display = ['usuario']
    search_fields = ['usuario']


admin.site.register(User, UserAdmin)
admin.site.register(DesignSystem, DesignSystemAdmin)
admin.site.register(ControleCadastro, ControleCadastroAdmin)
admin.site.register(ConfigsSistema, ConfigsSistemaAdmin)
admin.site.register(PasswordReset, PasswordResetAdmin)
