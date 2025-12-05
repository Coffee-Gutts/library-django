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
