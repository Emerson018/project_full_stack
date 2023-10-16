from django.shortcuts import render

from usuarios.forms import LoginForms, CadastroForms

def login(request):
    #esse form passa as informacoes do form para o login
    form = LoginForms()
    #parametros = 1 = requisição. 2 = template/localizacao.
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()
    return render(request, "usuarios/cadastro.html", {"form": form})