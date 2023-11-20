from django.contrib import admin

from .models import Cor, Raca, Especie, Animal

# admin.site.register(Raca)
# admin.site.register(Animal)
# admin.site.register(Cor)
# admin.site.register(Especie)

# ...
@admin.register(Raca)
class RacaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)

@admin.register(Cor)
class CorAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)

@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especie', 'cor')
    search_fields = ('nome', 'especie__descricao', 'cor__descricao')
    list_filter = ('especie', 'cor','raca')
    ordering = ('nome', 'especie', 'cor')
    list_per_page = 25