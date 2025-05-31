from django.db import models


class lista(models.Model):
    Nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)

    def __str__(self):
        return self.Nome
