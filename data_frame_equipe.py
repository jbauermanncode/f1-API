from webscrapingF1 import WebscrapingF1
import dataframe_image as dfi
import pandas as pd

class DataFrameEquipe:

    dataframe = WebscrapingF1()

    def excluindo_linhas(self, temporada):

        dataframe = self.dataframe.webscraping_equipes(temporada)
        
        if ((temporada == '1981') or (temporada == '1983') or (temporada == '1987') 
            or (temporada == '1988') or (temporada == '1990')):
            exclui = 1
        elif ((temporada == '1991') or (temporada == '2005') or (temporada == '2006')
            or (temporada == '2007') or (temporada == '2008') or (temporada == '2010')
            or (temporada == '2011') or (temporada == '2012') or (temporada == '2013')
            or (temporada == '2018') or (temporada == '2019') or (temporada == '2020')
            or (temporada == '2021')):
            exclui = 2
        
        dataframe.drop(dataframe.tail(exclui).index, inplace=True)

        return dataframe
    
    def dataframeEquipes(self, temporada):
        
        dataframe = self.excluindo_linhas(temporada)
        cont = 0
        lista_equipe = []
        lista_posicao = []
        lista_pontos = []
        while(cont <= (dataframe.shape[0]-1)):
            lista_equipe.append(dataframe.Constructor[cont])
            if (temporada == '1981') or (temporada == '1983') or (temporada == '1987') or (temporada == '1988'):
                lista_posicao.append(dataframe.Pos[cont])
            elif ((temporada == '1990') or (temporada == '1991') or (temporada == '2005') 
                or (temporada == '2006') or (temporada == '2007') or (temporada == '2008') 
                or (temporada == '2010') or (temporada == '2011') or (temporada == '2012')
                or (temporada == '2013') or (temporada == '2018') or (temporada == '2019')
                or (temporada == '2020') or (temporada == '2021')):
                lista_posicao.append(dataframe['Pos.'][cont])
            
            if (temporada == '1981') or (temporada == '1983') or (temporada == '1987') or (temporada == '1988'):
                lista_pontos.append(dataframe.Pts[cont])
            elif ((temporada == '1990') or (temporada == '1991') or (temporada == '2005') 
                or (temporada == '2006') or (temporada == '2007') or (temporada == '2008') 
                or (temporada == '2010') or (temporada == '2011') or (temporada == '2012')
                or (temporada == '2013') or (temporada == '2018') or (temporada == '2019')
                or (temporada == '2020') or (temporada == '2021')):
                lista_pontos.append(dataframe.Points[cont])
            cont = cont +1

        equipes = []
        for equipe in lista_equipe:
            if equipe not in equipes:
                equipes.append(equipe)
        posicoes = []
        for posicao in lista_posicao:
            if posicao not in posicoes:
                posicoes.append(posicao)

        pontuacao = []
        for pontos in lista_pontos:
            if pontos not in pontuacao:
                pontuacao.append(pontos)

        lista_colunas = list(zip(posicoes,equipes,pontuacao))

        df = pd.DataFrame(lista_colunas, columns=['Posição','Equipe','Pontos'])

        #guardando o DataFrame 
        dfi.export(df,f'./temporadas/temporada-{temporada}/equipes/resultado-equipes-{temporada}.png', table_conversion='matplotlib')

        return df


