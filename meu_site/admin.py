from django.contrib import admin, messages
from .models import PlanoInternet, BusinessLead


from .models import Noticia

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




class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data_publicacao', 'imagem_preview')  # colunas exibidas na lista
    prepopulated_fields = {'slug': ('titulo',)}  # gera slug automaticamente
    search_fields = ('titulo', 'resumo', 'conteudo', 'categoria')  # campos pesquisáveis
    list_filter = ('categoria', 'data_publicacao')  # filtros laterais
    date_hierarchy = 'data_publicacao'  # navegação por data
    readonly_fields = ('data_publicacao', 'imagem_preview')  # campos somente leitura
    fields = ('titulo', 'slug', 'categoria', 'imagem', 'imagem_preview', 'resumo', 'conteudo', 'data_publicacao')
    
    def imagem_preview(self, obj):
        if obj.imagem:
            return f'<img src="{obj.imagem.url}" style="max-width: 100px; max-height: 100px; border-radius: 8px;" />'
        return "Nenhuma imagem"
    imagem_preview.allow_tags = True
    imagem_preview.short_description = "Preview da Imagem"

admin.site.register(Noticia, NoticiaAdmin)