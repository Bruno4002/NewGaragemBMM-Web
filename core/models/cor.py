from django.db import models

class Cor(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome, self.id

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'