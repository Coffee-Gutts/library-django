from django.db import models

class Livros(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    autor = models.CharField(max_length=100, blank=False, null=False)
    editora = models.CharField(max_length=100, blank=False, null=False)
    ISBN = models.CharField(max_length=13, blank=False, null=False)
    genero = models.CharField(max_length=100, blank=False, null=False)

    def exibir_info(self):
        return f"<strong>Título:</strong> {self.titulo}<br><strong>Autor:</strong> {self.autor}<br><strong>Editora:</strong> {self.editora}<br><strong>ISBN: </strong>{self.ISBN}<br> <strong>Gênero:</strong> {self.genero}"

    objects = models.Manager()      

