#URLS DA GALERIA

from  django.urls import path
from galeria.views import index, imagem, buscar

#boas praticas. aqui só tem URLS se essas paginas forem relacionadas a GALERIA.
urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path("buscar", buscar, name="buscar"),

]