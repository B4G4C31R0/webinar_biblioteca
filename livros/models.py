from django.db import models

# Create your models here.

class Autor(models.Model):
    autor= models.CharField(max_length=50)
    
    def __str__(self):
        return self.autor


class Livro(models.Model):
    titulo= models.CharField(max_length=50)
    sinopse= models.TextField()
    data_publicacao= models.DateField()
    autor= models.ManyToManyField('Autor')

    def __str__(self):
        return self.titulo
