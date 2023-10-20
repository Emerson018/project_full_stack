#aqui ENVIA OS DADOS
from apps.galeria.models import Fotografia
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


def index(request):
    #se a autenticacao nao estiver feita:
    if not request.user.is_authenticated:
        messages.error(request, "Faça login para acessar a página.")
        return redirect('login')
    #aqui ta buscando todos os itens do BD
    #se colocar um '-' na frente de 'data_fotografia', ele comeca pelo ultimo.
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    
    return render(request, 'galeria/index.html', {"cards": fotografias})

#
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Faça login para pesquisar.")
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    #request.get=representacao da url. o 2° buscar se refere ao q foi escrito
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            #busca dentro do objeto se existe algo parecido dentro da
            #pesquisa q faça sentido na busca de algo
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/buscar.html', {"cards": fotografias})

def nova_imagem(request):
    return render(request, 'galeria/nova_imagem.html')

def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass