from django.db import models
from datetime import datetime

#aqui tamo criando um Banco de Dados
class Fotografia(models.Model):
    #nome é uma string com charfield null


# aqui ta add uma categoria pra escolher no admin
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]

    nome = models.CharField(max_length=100,null=False,blank=False)
    legenda = models.CharField(max_length=200,null=False,blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False,blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

#é pra visualizar o item qndo chamado pra teste.
    def __str__(self):
        return f"Fotografia [nome={self.nome}]"