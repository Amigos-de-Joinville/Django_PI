# from django.db import models

# from amigosjvll.models import Apelido, Cor, Raca


# class Animal(models.Model):
#     apelido = models.ForeignKey(
#         Apelido, on_delete=models.PROTECT, related_name="animais"
#     )
#     especie = models.CharField(max_length=15, null=False, default=0)
#     raca = models.ForeignKey(
#         Raca, on_delete=models.PROTECT, related_name="animais"
#     )
#     cor = models.ForeignKey(
#         Cor, on_delete=models.PROTECT, related_name="animais"
#     )
#     idade = models.IntegerField(null=True,default=0)
    
#     def __str__(self):
#         return f"Apelido: {self.apelido} Raca: {self.raca} Cor: {self.cor}"
    
#     class Meta:
#         verbose_name = "animal"
#         verbose_name_plural = "animais"