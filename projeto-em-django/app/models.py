from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    idade = models.IntegerField()
    data_de_nascimento = models.CharField(max_length=10)
    email = models.EmailField(max_length=50, default="")
    apelido = models.CharField(max_length=15, blank=True, null=True)
    observacao = models.TextField(max_length=80, blank=True, null=True)