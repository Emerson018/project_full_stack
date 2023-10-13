#aqui ENVIA OS DADOS
from galeria.models import Fotografia
from django.shortcuts import render, get_object_or_404


def index(request):
    #se colocar um '-' na frente de 'data_fotografia', ele comeca pelo ultimo.
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    
    return render(request, 'galeria/index.html', {"cards": fotografias})

#
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})