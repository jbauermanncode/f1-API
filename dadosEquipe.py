import unidecode
from data_frame_equipe import DataFrameEquipe
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from f1.models import Equipe

class DadosEquipe:

    data = DataFrameEquipe()

    def equipeID(self, temporada):

        dataframe = self.data.dataframeEquipes(temporada)

        lista_equipe_id = []

        for equipe in dataframe.Equipe:
            juntar_nome = equipe.replace(" ", "")
            equipe = unidecode.unidecode(juntar_nome)
            idEquipe = f'{equipe}{temporada}'
            lista_equipe_id.append(idEquipe)
        
        return lista_equipe_id
    
    def nomeEquipe(self, temporada):
        
        dataframe = self.data.dataframeEquipes(temporada)

        lista_equipes = []

        for equipe in dataframe.Equipe:
            lista_equipes.append(equipe)

        return lista_equipes
    
    def posicaoEquipe(self, temporada):

        dataframe = self.data.dataframeEquipes(temporada)

        lista_posicao_equipes = []

        for posicao in dataframe['Posição']:
            lista_posicao_equipes.append(posicao)
        
        return lista_posicao_equipes
    
    def pontuacaoEquipe(self, temporada):

        dataframe = self.data.dataframeEquipes(temporada)

        lista_pontuacao_equipes = []

        for pontuacao in dataframe.Pontos:
            lista_pontuacao_equipes.append(pontuacao) 

        return lista_pontuacao_equipes
    
    def juntarNomeEquipe(self, temporada):
        
        dataframe = self.data.dataframeEquipes(temporada)

        lista_juntar = []

        for equipe in dataframe.Equipe:
            equipe = f'{equipe}F1'
            juntar_nome = equipe.replace(" ", "")
            lista_juntar.append(juntar_nome)
        
        return lista_juntar



dados_equipe = DadosEquipe()

data = DataFrameEquipe()

def criando_equipes(temporada):
    
    dataframe = data.dataframeEquipes(temporada)

    for i in range(dataframe.shape[0]):
    
        equipeID = dados_equipe.equipeID(temporada)[i]
        nomeEquipe = dados_equipe.nomeEquipe(temporada)[i]
        posicaoEquipe = dados_equipe.posicaoEquipe(temporada)[i]
        pontuacaoEquipe = dados_equipe.pontuacaoEquipe(temporada)[i]
        imagemEquipe = f"temporada-{temporada}/equipes/{dados_equipe.juntarNomeEquipe(temporada)[i]}.jpg"

        equipe = Equipe(equipeID=equipeID, nomeEquipe=nomeEquipe, posicaoEquipe=posicaoEquipe, pontuacao_equipe=pontuacaoEquipe,
                        imagemEquipe=imagemEquipe)
        
        equipe.save()

criando_equipes('1981')
print(f'Sucesso!')



