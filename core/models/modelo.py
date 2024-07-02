from django.db import models
from .marca import Marca
from .categoria import Categoria

class Modelo(models.Model):
    name = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.RESTRICT)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.name}, ({self.id}), {self.marca}"
    
    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"