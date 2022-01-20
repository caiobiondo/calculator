from django.contrib import admin

from .models import Bof, Calculo, Calculoscombinada, Cboregracusteio


@admin.register(Bof)
class BofAdmin(admin.ModelAdmin):
    list_display = ('segmento', 'produto', 'modalidade', 'criacao', 'ativo')


@admin.register(Calculo)
class CalculoAdmin(admin.ModelAdmin):
    list_display = ('calculo', 'criacao')


@admin.register(Calculoscombinada)
class CalculoscombinadaAdmin(admin.ModelAdmin):
    list_display = ('ids_calc',)

@admin.register(Cboregracusteio)
class CboregracusteioAdmin(admin.ModelAdmin):
    list_display = ('produto', 'modalidade')



