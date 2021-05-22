from django.db import models
from django.db.models.base import Model


class Produto(models.Model):
    produto = models.CharField('Produto', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return self.produto


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.CharField('Email', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
