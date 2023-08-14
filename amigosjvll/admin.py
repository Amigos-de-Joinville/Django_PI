from django.contrib import admin

from .models import Cor, Raca, Especie, Animal

admin.site.register(Raca)
admin.site.register(Animal)
admin.site.register(Cor)
admin.site.register(Especie)
