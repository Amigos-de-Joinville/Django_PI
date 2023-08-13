from django.contrib import admin

from .models import Cor, Raca, Apelido, Especie

# admin.site.register(Animal)
admin.site.register(Cor)
admin.site.register(Especie)
# admin.site.register(Idade)
admin.site.register(Apelido)
admin.site.register(Raca)
