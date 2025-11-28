from django.shortcuts import render, redirect, HttpResponse
from .models import Aluno
from .forms import AlunoForm
# Create your views here.

def index(request):
    lista = Aluno.objects.all()
    return render(request, 'index.html', {"alunos":lista})

def cadastro(request):
    
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if(form.is_valid()):
            form.save()
        else: 
            HttpResponse(str(form.errors))
            

    return render(request, 'cadastro.html')
    

    # if request.method == 'POST': ##cadastrar aluno
    #     nome= request.POST.get('nome')
    #     dataNascimento= request.POST.get('dataNascimento')
    #     cpf= request.POST.get('cpf')
    #     curso= request.POST.get('curso')
    #     anoMatricula= request.POST.get('anoMatricula')

    #     aluno = Aluno(
    #                 nome=nome,
    #                 dataNascimento=dataNascimento,
    #                 cpf=cpf,
    #                 curso=curso,
    #                 anoMatricula=anoMatricula,
    #                 )
    #     aluno.save()

        # return redirect('index')
    

def deletarCadastro(request, id):
    aluno = Aluno.objects.get(id=id)

    if request.method == 'POST':
        aluno.delete()
        return redirect('index')  # volta para a lista de alunos

    # GET request
    return render(request, 'deletarCadastro.html', {'aluno': aluno})


def editarCadastro(request, id):
    aluno = Aluno.objects.get(id=id)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse(str(form.errors))

    # GET request
    form = AlunoForm(instance=aluno)
    return render(request, 'editarCadastro.html', {'form': form, 'aluno': aluno})
