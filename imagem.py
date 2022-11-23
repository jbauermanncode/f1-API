from data_frame_equipe import DadosEquipe
from dataframe_invertido import DataFrameInvertido
from googleapiclient.discovery import build
import pprint
import urllib.request


class Imagem:

    dataframe = DataFrameInvertido()

    equipe = DadosEquipe()

    my_api_key = 'AIzaSyCrnmYduXWTop25z46fnB6OH82w38nu02k'
    my_cse_id = '5377046f54fe340ab'

    def imagem_pilotos(self, temporada):

        dataframe = self.dataframe.excluindo_ultimas_linhas_e_modificando(temporada)

        for piloto in dataframe.Driver:

            service = build("customsearch", "v1", developerKey=self.my_api_key)
            res = service.cse().list(q=piloto, cx=self.my_cse_id, searchType='image').execute()
            items = res['items']
            images = [d['link'] for d in items]

            piloto = piloto.replace(" ", "")
            urllib.request.urlretrieve(images[0], f"./temporadas/temporada-{temporada}/pilotos/{piloto}/{piloto}.jpg")
    
    def imagem_equipes(self, temporada):

        dataframe = self.equipe.dataframeEquipes(temporada)

        for equipe in dataframe.Equipe:

            equipe = f'{equipe}F1{temporada}'

            service = build("customsearch", "v1", developerKey=self.my_api_key)
            res = service.cse().list(q=equipe, cx=self.my_cse_id, searchType='image').execute()
            items = res['items']
            images = [d['link'] for d in items]

            equipe = equipe.replace(" ", "")
            urllib.request.urlretrieve(images[0], f"./temporadas/temporada-{temporada}/equipes/{equipe}.jpg")


imagem = Imagem()

imagem.imagem_pilotos('2021')

imagem.imagem_equipes('2021')
    