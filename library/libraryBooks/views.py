from django.shortcuts import render, redirect, HttpResponse
from .models import Livros
from .forms import LivrosForm
# Create your views here.

def index(request):
    lista = Livros.objects.all()
    return render(request, 'index.html', {"livros": lista})

def cadastro(request):
    
    if request.method == 'POST':
        form = LivrosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else: 
            HttpResponse(str(form.errors))
    return render(request, 'cadastro.html')

def editar(request, id):
    livro = Livros.objects.get(id=id)
    if request.method == 'POST':
        form = LivrosForm(request.POST, instance=livro)
        if form.is_valid():
            for field, value in form.cleaned_data.items():
                if value:
                    setattr(livro, field, value)
            livro.save()
            return redirect('index')
        else:
            return HttpResponse(str(form.errors))
    else:
        form = LivrosForm(instance=livro)
    return render(request, 'editarCadastro.html', {"form": form, "livro": livro})

def deletar(request, id):
    livro = Livros.objects.get(id=id)
    livro.delete()
    return redirect('index')
