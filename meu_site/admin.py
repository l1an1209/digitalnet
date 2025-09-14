from django.contrib import admin, messages
from .models import PlanoInternet, BusinessLead

from .models import PlanoEmpresarial

admin.site.register(PlanoEmpresarial)

def marcar_como_destaque(modeladmin, request, queryset):
    atualizados = queryset.update(destaque=True)
    messages.success(request, f"{atualizados} plano(s) marcados como destaque.")


def remover_destaque(modeladmin, request, queryset):
    atualizados = queryset.update(destaque=False)
    messages.success(request, f"{atualizados} plano(s) removidos de destaque.")


@admin.register(PlanoInternet)
class PlanoInternetAdmin(admin.ModelAdmin):
    list_display = ("nome", "velocidade", "preco", "destaque")
    list_editable = ("preco", "destaque")
    list_filter = ("destaque",)
    search_fields = ("nome", "velocidade", "descricao")
    ordering = ("-destaque", "nome")
    actions = [marcar_como_destaque, remover_destaque]


@admin.register(BusinessLead)
class BusinessLeadAdmin(admin.ModelAdmin):
    list_display = ("created_at", "company_name", "contact_name", "phone", "status")
    list_filter = ("status", "created_at")
    search_fields = ("company_name", "cnpj", "contact_name", "email", "phone")
