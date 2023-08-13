from django.contrib import admin

from .models import Cor, Raca, Especie, Apelido, Animal

admin.site.register(Raca)
admin.site.register(Animal)
admin.site.register(Cor)
admin.site.register(Especie)
# admin.site.register(Idade)
admin.site.register(Apelido)

