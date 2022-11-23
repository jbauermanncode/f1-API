from dataframe_invertido import DataFrameInvertido
from urllib.request import urlopen
from bs4 import BeautifulSoup
import unidecode

class Descricao:

    dataframe = DataFrameInvertido()

    def descricao_piloto(self, temporada):

        dataframe = self.dataframe.excluindo_ultimas_linhas_e_modificando(temporada)

        lista_descricao = []
        for piloto in dataframe.Driver:
            juntar_nome = piloto.replace(" ", "_")
            juntar_nome = unidecode.unidecode(juntar_nome)
            url = f'https://pt.wikipedia.org/wiki/{juntar_nome}'
            print(juntar_nome)
            response = urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            paragrafo = soup.find('table').find_next('p')
            descricao = paragrafo.get_text()
            descricao = descricao.replace("\n","")
            lista_descricao.append(descricao)
        
        return lista_descricao

descricao = Descricao()

lista = descricao.descricao_piloto('1981')

for i in lista:
    print(i)
    print()
    print('-_-' * 40)