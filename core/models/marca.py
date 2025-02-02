from django.db import models

class Marca(models.Model):
    name = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name.upper()} ({self.id})"
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
       