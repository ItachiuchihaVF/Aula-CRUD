from django.shortcuts import render, redirect
from .models import Aluno, Usuario

# Create your views here.
def home(request):
    return render(request, 'base.html')


def cadastro(request):
    if request.method == 'POST':
        data_usuario = Usuario()
        data_usuario.email = request.POST['email']
        data_usuario.senha = request.POST['senha']
        data_usuario.save()
        
        data_aluno = Aluno()
        data_aluno.nome = request.POST['nome']
        data_aluno.frase = request.POST['frase']
        data_aluno.save()
        
    return render(request, 'cadastro.html')

def listar(request):
    listar_frase = Aluno.objects.filter(ativo=True).all()
    args = {
        'listar_frase':listar_frase
    }
    return render(request, 'lista.html',args)
def deleter(resquest):
    item = Aluno.objects.get(id=id)
    if item is not None:
        item.ativo = false 
        item.save()
        return redirect('/aluno/listar')
    return render(request, 'lista.html') 


def login(request):
    if request.method == 'POST':
      data_usuario = Usuario()
      data_aluno.email = request.POST['email']
      data_usuario.senha = request.POST['senha']
      data_usuario.save()
    
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')