from django.db import models
from .modelo import Modelo
from .cor import Cor
from .acessorio import Acessorio

class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.RESTRICT)
    acessorios = models.ForeignKey(Acessorio, on_delete=models.RESTRICT)
    ano = models.IntegerField()
    cor = models.ForeignKey(Cor, on_delete=models.RESTRICT)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.modelo} {self.ano} {self.cor} R${self.preco}"
    
    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"