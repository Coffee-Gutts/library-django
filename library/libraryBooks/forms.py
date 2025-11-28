from django.forms import ModelForm

from.models import Livros

class LivrosForm(ModelForm):
    class Meta: 
        model = Livros
        fields = ['nome','cpf','curso', 'dataNascimento', 'anoMatricula']        