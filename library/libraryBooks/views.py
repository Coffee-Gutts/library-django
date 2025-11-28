from django.shortcuts import render, redirect, HttpResponse
from .models import Livros
from .forms import LivrosForm
# Create your views here.

def index(request):
    lista = Livros.objects.all()
    return render(request, 'index.html', {"Livross":lista})

def cadastro(request):
    
    if request.method == 'POST':
        form = LivrosForm(request.POST)
        if(form.is_valid()):
            form.save()
        else: 
            HttpResponse(str(form.errors))
            

    return render(request, 'cadastro.html')
    

    # if request.method == 'POST': ##cadastrar Livros
    #     nome= request.POST.get('nome')
    #     dataNascimento= request.POST.get('dataNascimento')
    #     cpf= request.POST.get('cpf')
    #     curso= request.POST.get('curso')
    #     anoMatricula= request.POST.get('anoMatricula')

    #     Livros = Livros(
    #                 nome=nome,
    #                 dataNascimento=dataNascimento,
    #                 cpf=cpf,
    #                 curso=curso,
    #                 anoMatricula=anoMatricula,
    #                 )
    #     Livros.save()

        # return redirect('index')
    

def deletarCadastro(request, id):
    Livros = Livros.objects.get(id=id)

    if request.method == 'POST':
        Livros.delete()
        return redirect('index')  # volta para a lista de Livross

    # GET request
    return render(request, 'deletarCadastro.html', {'Livros': Livros})


def editarCadastro(request, id):
    Livros = Livros.objects.get(id=id)

    if request.method == 'POST':
        form = LivrosForm(request.POST, instance=Livros)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse(str(form.errors))

    # GET request
    form = LivrosForm(instance=Livros)
    return render(request, 'editarCadastro.html', {'form': form, 'Livros': Livros})
