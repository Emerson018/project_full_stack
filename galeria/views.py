#aqui ENVIA OS DADOS

from django.shortcuts import render


def index(request):

    dados = {
        1: {"nome": "Nebulosa do Sayrix",
            "legenda": "Webbtelescope.org / NASA /James Webb"},
        2: {"nome": "Galáxia do Sayrix",
            "legenda": "nasa.org / NASA / Hubble"}
    }

    return render(request, 'galeria/index.html', {"cards": dados})

#
def imagem(request):
    return render(request, 'galeria/imagem.html')