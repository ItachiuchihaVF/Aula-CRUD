from django.shortcuts import render, redirect
from .models import Aluno, Usuario

# Create your views here.

def index(request):
    if request.method == 'POST':
        data_usuario = Usuario()
        data_usuario.email = request.POST['email']
        data_usuario.senha = request.POST['senha']
        data_usuario.save()
        
        data_aluno = Aluno()
        data_aluno.nome = request.POST['nome']
        data_aluno.frase = request.POST['frase']
        data_aluno.save()
        
    return render(request, 'index.html')

def listar(request):
    listar_frase = Aluno.objects.filter(ativo=true).all()
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
    return render(requet, 'lista.html') 