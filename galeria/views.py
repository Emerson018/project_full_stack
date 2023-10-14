#aqui ENVIA OS DADOS
from galeria.models import Fotografia
from django.shortcuts import render, get_object_or_404


def index(request):
    #aqui ta buscando todos os itens do BD
    #se colocar um '-' na frente de 'data_fotografia', ele comeca pelo ultimo.
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    
    return render(request, 'galeria/index.html', {"cards": fotografias})

#
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    #request.get=representacao da url. o 2° buscar se refere ao q foi escrito
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            #busca dentro do objeto se existe algo parecido dentro da
            #pesquisa q faça sentido na busca de algo
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/buscar.html', {"cards": fotografias})