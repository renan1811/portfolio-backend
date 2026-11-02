"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ('id',)
    list_display = ('email', 'name')
    search_fields = ('email', 'name', 'groups__name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            },
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
        (_('Groups'), {'fields': ('groups',)}),
        (_('User Permissions'), {'fields': ('user_permissions',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'name',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ),
            },
        ),
    )


admin.site.register(models.User, UserAdmin)


@admin.register(models.Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'ordem')
    search_fields = ('nome', 'slug')
    list_filter = ('categoria',)
    ordering = ('ordem', 'nome')
    prepopulated_fields = {'slug': ('nome',)}


@admin.register(models.Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'destaque', 'publicado', 'ordem', 'atualizado_em')
    search_fields = ('titulo', 'slug', 'resumo', 'tecnologias__nome')
    list_filter = ('publicado', 'destaque', 'ano', 'tecnologias')
    ordering = ('ordem', '-ano')
    prepopulated_fields = {'slug': ('titulo',)}
    filter_horizontal = ('tecnologias',)
    readonly_fields = ('criado_em', 'atualizado_em')


@admin.register(models.Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'organizacao', 'tipo', 'data_inicio', 'atual', 'publicado', 'ordem')
    search_fields = ('titulo', 'organizacao', 'descricao')
    list_filter = ('tipo', 'atual', 'publicado')
    ordering = ('ordem', '-data_inicio')


@admin.register(models.Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'instituicao', 'data_inicio', 'em_andamento', 'publicado', 'ordem')
    search_fields = ('curso', 'instituicao', 'descricao')
    list_filter = ('em_andamento', 'publicado')
    ordering = ('ordem',)
