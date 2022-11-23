from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from criacao_diretorios import Diretorio

class WebscrapingF1:

    diretorio = Diretorio()

    def webscraping_pilotos(self, temporada):

        url = f'https://en.wikipedia.org/wiki/{temporada}_Formula_One_World_Championship'

        response = urlopen(url)
        html = response.read()

        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('span', id = "World_Drivers'_Championship_standings").find_next('table')
        data_frame = pd.read_html( str(table) )[1]
        
        return data_frame


    def webscraping_equipes(self, temporada):

        url = f'https://en.wikipedia.org/wiki/{temporada}_Formula_One_World_Championship'

        response = urlopen(url)
        html = response.read()

        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('span', id = "World_Constructors'_Championship_standings").find_next('table')
            
        if ((temporada == '1981') or (temporada == '1983') 
            or (temporada == '1988') or (temporada == '1990') or (temporada == '1991')):
            data_frame = pd.read_html( str(table) )[0]
            
        elif ((temporada == '2008') or (temporada == '1987') or (temporada == '2005') 
            or (temporada == '2006') or (temporada == '2007') or (temporada == '2008')
            or (temporada == '2010') or (temporada == '2011') or (temporada == '2012')
            or (temporada == '2013') or (temporada == '2018') or (temporada == '2019')
            or (temporada == '2020') or (temporada == '2021')):
            data_frame = pd.read_html( str(table) )[1]

        return data_frame
