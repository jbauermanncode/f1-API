from django.db import models

# Create your models here.
from django.db import models

def upload_image_piloto(instance, filename):
    return f'{instance.nomePiloto}-{filename}'

def upload_image_campeonato(instance, filename):
    return f'{instance.campeonatoID}-{filename}'

def upload_image_equipe(instance, filename):
    return f'{instance.nomeEquipe}-{filename}'

class Piloto(models.Model):
    pilotoID = models.CharField(max_length=30, primary_key=True)
    nomePiloto = models.CharField(max_length=30)
    posicaoPiloto = models.CharField(max_length=10)
    pontuacaoPiloto = models.CharField(max_length=10)
    descricao = models.CharField(max_length=10000) 
    distribuicaoFrequencias = models.ImageField(upload_to=upload_image_piloto, blank=True, null=True)
    graficoFrequencias = models.ImageField(upload_to=upload_image_piloto, blank=True, null=True)
    graficoPorcentagem = models.ImageField(upload_to=upload_image_piloto, blank=True, null=True)
    piePlot = models.ImageField(upload_to=upload_image_piloto, blank=True, null=True)
    imagemPiloto = models.ImageField(upload_to=upload_image_piloto, blank=True, null=True)

    def __str__(self):
        return self.pilotoID

class Equipe(models.Model):
    equipeID = models.CharField(max_length=30, primary_key=True)
    nomeEquipe = models.CharField(max_length=30)
    posicaoEquipe = models.IntegerField(null=True)
    pontuacao_equipe = models.FloatField(null=True)
    imagemEquipe = models.ImageField(upload_to=upload_image_equipe, blank=True, null=True)

    def __str__(self):
        return self.equipeID

class Campeonato(models.Model):
    campeonatoID = models.CharField(max_length=30, primary_key=True)
    pilotosRegulamentoOriginal = models.ImageField(upload_to=upload_image_campeonato, blank=True, null=True)
    pilotosRegulamentoDe2022 = models.ImageField(upload_to=upload_image_campeonato, blank=True, null=True)
    pilotosRegulamentoVoltaMaisRápidaPole = models.ImageField(upload_to=upload_image_campeonato, blank=True, null=True)
    pilotosRegulamentoDecrescimo = models.ImageField(upload_to=upload_image_campeonato, blank=True, null=True)
    resultadoEquipes = models.ImageField(upload_to = upload_image_campeonato, blank=True, null=True)

    def __str__(self):
        return self.campeonatoID

class DadosCampeonato(models.Model):
    dadosID = models.CharField(max_length=30, primary_key=True)
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)

class Temporada(models.Model):
    temporadaID = models.CharField(max_length=30, primary_key=True)
    temporada = models.CharField(max_length=30)
    dadosCampeonato = models.ForeignKey(DadosCampeonato, on_delete=models.CASCADE)




    


