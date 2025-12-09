from django.forms import ModelForm

from.models import Livros

class LivrosForm(ModelForm):
    class Meta: 
        model = Livros
        fields = ['titulo','autor','editora', 'ISBN', 'genero']      

    def __init__(self, *args, **kwargs):
        super(LivrosForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
