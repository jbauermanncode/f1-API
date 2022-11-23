import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from f1.models import Campeonato

def criando_campeonatos(temporada):

    campeonatoID = f'campeonato{temporada}'
    pilotosRegulamentoOriginal = f'temporada-{temporada}/pilotos/resultado-pilotos-original-{temporada}.png'
    pilotosRegulamentoDe2022 = f'temporada-{temporada}/pilotos/resultado-pilotos-regulamento-2022-{temporada}.png'
    pilotosRegulamentoVoltaMaisRápidaPole = f'temporada-{temporada}/pilotos/resultado-pilotos-regulamento-volta-e-pole-{temporada}.png'
    pilotosRegulamentoDecrescimo = f'temporada-{temporada}/pilotos/resultado_pilotos_com_decrescimo_pontos_{temporada}.png'
    resultadoEquipes = f'temporada-{temporada}/equipes/resultado-equipes-{temporada}.png'

    campeonato = Campeonato(campeonatoID=campeonatoID, pilotosRegulamentoOriginal=pilotosRegulamentoOriginal, 
                            pilotosRegulamentoDe2022=pilotosRegulamentoDe2022, pilotosRegulamentoVoltaMaisRápidaPole=pilotosRegulamentoVoltaMaisRápidaPole,
                        pilotosRegulamentoDecrescimo=pilotosRegulamentoDecrescimo, resultadoEquipes=resultadoEquipes)
        
    campeonato.save()

criando_campeonatos('1981')
print(f'Sucesso!')




