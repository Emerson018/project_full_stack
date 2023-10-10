#URLS DA GALERIA

from  django.urls import path
from galeria.views import index, imagem

#boas praticas. aqui só tem URLS se essas paginas forem relacionadas a GALERIA.
urlpatterns = [
    path('', index),
    path('imagem/', imagem)

]