from django.db import models

class Livros(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    autor = models.CharField(max_length=100, blank=False, null=False)
    editora = models.CharField(max_length=100, blank=False, null=False)
    ISBN = models.IntegerField(max_length=13, blank=False, null=False)
    genero = models.CharField(max_length=100, blank=False, null=False)

    objects = models.Manager()      

