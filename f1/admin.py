from django.contrib import admin
from f1.models import Equipe, Piloto, Campeonato, DadosCampeonato, Temporada

class Pilotos(admin.ModelAdmin):
    list_display = ('pilotoID', 'nomePiloto', 'posicaoPiloto', 'pontuacaoPiloto', 'descricao', 'distribuicaoFrequencias', 
                    'graficoFrequencias', 'graficoPorcentagem', 'piePlot', 'imagemPiloto')
    list_display_links = ('pilotoID',)
    search_fields = ('pilotoID',)
    list_per_page = 20

admin.site.register(Piloto, Pilotos)

class Equipes(admin.ModelAdmin):
    list_display = ('equipeID','nomeEquipe','posicaoEquipe', 'pontuacao_equipe', 
                    'imagemEquipe',)
    list_display_links = ('equipeID',)
    search_fields = ('equipeID',)
    list_per_page = 20

admin.site.register(Equipe, Equipes)

class Campeonatos(admin.ModelAdmin):
    list_display = ('campeonatoID' ,'pilotosRegulamentoOriginal','pilotosRegulamentoDe2022', 
                    'pilotosRegulamentoVoltaMaisRápidaPole', 'pilotosRegulamentoDecrescimo','resultadoEquipes', )
    list_display_links = ('campeonatoID',)
    search_fields = ('campeonatoID',)
    list_per_page = 20

admin.site.register(Campeonato, Campeonatos)

class DadosDosCampeonatos(admin.ModelAdmin):
    list_display = ('dadosID','piloto', 'campeonato', )
    list_display_links = ('dadosID',)

admin.site.register(DadosCampeonato, DadosDosCampeonatos)

class Temporadas(admin.ModelAdmin):
    list_display = ('temporadaID','temporada', 'dadosCampeonato', )
    list_display_links = ('temporadaID',)

admin.site.register(Temporada, Temporadas)
