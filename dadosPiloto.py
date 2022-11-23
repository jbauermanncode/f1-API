from urllib.request import urlopen
from bs4 import BeautifulSoup
import unidecode
from dataframe_invertido import DataFrameInvertido
import os, django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from f1.models import Piloto


class DadosPiloto:

    data = DataFrameInvertido()

    def pilotoID(self, temporada):

        dataframe = self.data.excluindo_ultimas_linhas_e_modificando(temporada)

        lista_id_pilotos = []

        for piloto in dataframe.Driver:
            juntar_nome = piloto.replace(" ", "")
            piloto = unidecode.unidecode(juntar_nome)
            idPiloto = f'{piloto}{temporada}'
            lista_id_pilotos.append(idPiloto)
        
        return lista_id_pilotos


    def nomePiloto(self, temporada):

        dataframe = self.data.excluindo_ultimas_linhas_e_modificando(temporada)

        lista_pilotos = []

        for piloto in dataframe.Driver:
            lista_pilotos.append(piloto)
        
        return lista_pilotos
    
    def posicaoPiloto(self, temporada):

        dataframe = self.data.excluindo_ultimas_linhas_e_modificando(temporada)

        lista_posicao_pilotos = []

        if ((temporada == '1981') or (temporada == '1983') or (temporada == '1987') or (temporada == '1988')):
            posicao = 'Pos'
        elif ((temporada == '1990') or (temporada == '2005') or (temporada == '2006') 
                or (temporada == '2007') or (temporada == '2008') or (temporada == '2010') 
                or (temporada == '2011') or (temporada == '2012') or (temporada == '2013') 
                or (temporada == '2018') or (temporada == '2019') or (temporada == '2020') 
                or (temporada == '2021')):
            posicao = 'Pos.'
        elif (temporada == '1991'):
            posicao = '.mw-parser-output .tooltip-dotted{border-bottom:1px dotted;cursor:help}Pos.'
        

        for posicao in dataframe[posicao]:
            lista_posicao_pilotos.append(posicao)
        
        return lista_posicao_pilotos
    
    def pontuacaoPiloto(self, temporada):

        dataframe = self.data.excluindo_ultimas_linhas_e_modificando(temporada)

        lista_pontuacao_pilotos = []

        if ((temporada == '1981') or (temporada == '1991') or (temporada == '2005') 
                or (temporada == '2006') or (temporada == '2007') or (temporada == '2008') 
                or (temporada == '2010') or (temporada == '2011') or (temporada == '2012') 
                or (temporada == '2013') or (temporada == '2018') or (temporada == '2019') 
                or (temporada == '2020') or (temporada == '2021')):

            pontos = 'Points'
        elif (temporada == '1983'):
            pontos = 'Pts'
        elif (temporada == '1987'):
            pontos = 'Points[1]'
        elif (temporada == '1988') or (temporada == '1990'):
            pontos = 'Points[a]'

        for pontuacao in dataframe[pontos]:
            lista_pontuacao_pilotos.append(pontuacao)
        
        return lista_pontuacao_pilotos
        
    def descricao(self, temporada):

        dataframe = self.data.excluindo_ultimas_linhas_e_modificando(temporada)

        lista_descricao = []
        for piloto in dataframe.Driver:
            juntar_nome = piloto.replace(" ", "_")
            juntar_nome = unidecode.unidecode(juntar_nome)
            url = f'https://pt.wikipedia.org/wiki/{juntar_nome}'
            response = urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            paragrafo = soup.find('table').find_next('p')
            descricao = paragrafo.get_text()
            descricao = descricao.replace("\n","")
            lista_descricao.append(descricao)
        
        return lista_descricao
    
    def juntarNomePiloto(self, temporada):

        dataframe = self.data.excluindo_ultimas_linhas_e_modificando(temporada)

        lista_juntar_pilotos = []

        for piloto in dataframe.Driver:
            piloto = piloto.replace(" ", "")
            lista_juntar_pilotos.append(piloto)

        return lista_juntar_pilotos


dados_piloto = DadosPiloto()

def criando_pilotos(temporada):

    dataframe = pd.read_csv(f'./temporadas/temporada-{temporada}/pilotos/resultado-pilotos-original-{temporada}.csv')

    for i in range(dataframe.shape[0]):

        pilotoID = dados_piloto.pilotoID(temporada)[i]
        nomePiloto = dados_piloto.nomePiloto(temporada)[i]
        posicaoPiloto = dados_piloto.posicaoPiloto(temporada)[i]
        pontuacaoPiloto = dados_piloto.pontuacaoPiloto(temporada)[i]
        descricao = dados_piloto.descricao(temporada)[i] 
        distribuicaoFrequencias = f"temporada-{temporada}/pilotos/{dados_piloto.juntarNomePiloto(temporada)[i]}/dist-freq-{dados_piloto.juntarNomePiloto(temporada)[i]}-{temporada}.png"
        graficoFrequencias = f"temporada-{temporada}/pilotos/{dados_piloto.juntarNomePiloto(temporada)[i]}/frequencia-plot-{dados_piloto.juntarNomePiloto(temporada)[i]}-{temporada}.png"
        graficoPorcentagem = f"temporada-{temporada}/pilotos/{dados_piloto.juntarNomePiloto(temporada)[i]}/porcentagem-plot-{dados_piloto.juntarNomePiloto(temporada)[i]}-{temporada}.png"
        piePlot = f"temporada-{temporada}/pilotos/{dados_piloto.juntarNomePiloto(temporada)[i]}/pie-plot-{dados_piloto.juntarNomePiloto(temporada)[i]}-{temporada}.png"
        imagemPiloto = f"temporada-{temporada}/pilotos/{dados_piloto.juntarNomePiloto(temporada)[i]}/{dados_piloto.juntarNomePiloto(temporada)[i]}.jpg"

        piloto = Piloto(pilotoID=pilotoID, nomePiloto=nomePiloto, posicaoPiloto=posicaoPiloto, pontuacaoPiloto=pontuacaoPiloto,
                        descricao=descricao, distribuicaoFrequencias=distribuicaoFrequencias, graficoFrequencias=graficoFrequencias,
                        graficoPorcentagem=graficoPorcentagem, piePlot=piePlot, imagemPiloto=imagemPiloto)
        piloto.save()

temporadas = ['1981']

for temporada in temporadas:
    criando_pilotos(temporada)
    print(f'{temporada} Sucesso!')
