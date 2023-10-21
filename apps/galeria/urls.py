#URLS DA GALERIA
from  django.urls import path
from apps.galeria.views import \
    index, imagem, buscar, nova_imagem,editar_imagem,deletar_imagem

#boas praticas. aqui só tem URLS se essas paginas forem relacionadas a GALERIA.
urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path("buscar", buscar, name="buscar"),
    path("nova-imagem", nova_imagem, name="nova_imagem"),
    path("editar-imagem/<int:foto_id>", editar_imagem, name="editar_imagem"),
    path("deletar-imagem/<int:foto_id>", deletar_imagem, name="deletar_imagem"),
]   