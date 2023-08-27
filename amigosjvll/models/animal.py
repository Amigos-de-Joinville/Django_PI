from django.db import models

from amigosjvll.models import Especie, Raca, Cor


class Animal(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    idade = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    especie = models.ForeignKey(
        Especie, on_delete=models.PROTECT, related_name="animais"
    )
    raca = models.ForeignKey(
        Raca, on_delete=models.PROTECT, related_name="animais"
    )
    cor = models.ForeignKey(
        Cor, on_delete=models.PROTECT, related_name="animais"
    )
    foto = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome} {self.especie}"
    