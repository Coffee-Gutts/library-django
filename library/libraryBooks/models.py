from django.db import models

class Livros(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=100, blank=False, null=False)
    curso = models.CharField(max_length=10, blank=False, null=False)
    dataNascimento = models.DateField()
    anoMatricula = models.IntegerField()

    objects = models.Manager()      

