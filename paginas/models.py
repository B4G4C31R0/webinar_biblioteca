from django.db import models

# Create your models here.

class Teste(models.Model):
    nome= models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome
