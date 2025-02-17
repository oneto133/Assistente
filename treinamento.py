import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import csv
import numpy as np
class Treinamento():
    def __init__(self):

        """
        Os arquivos csv de perguntas e respostas são lidos e todos os dados são colocados
        dentro de suas listas correspondentes, em seguida as respostas são maepeadas e
        indexadas

        Args:
            x: vetoriza as perguntas

            modelo: recebe um regressão logistica para se obter a previsão de um resultado, usada para treinar a IA. O treino acontece com as perguntas e suas respostas correspondentes.
            
        """
        arq1 = "csv/perguntas.csv"
        arq2 = "csv/respostas.csv"
        ia = "pkl/minhaia.pkl"
        for c in range (0,2):
            
            perguntas = []
            respostas = []

            with open(arq1, 'r', encoding='utf-8') as arquivo:
                leitor = csv.reader(arquivo)
                for linha in leitor:
                    perguntas.extend(linha)
            with open(arq2, 'r', encoding='utf-8') as arquivo:
                leitor = csv.reader(arquivo)
                for linha in leitor:
                    respostas.extend(linha)


            respostas_map = {resposta: i for i, resposta in enumerate(respostas)}
            respostas_numericas = [respostas_map[resposta] for resposta in respostas]
            

            vetorizar = TfidfVectorizer()
            x = vetorizar.fit_transform(perguntas)
            modelo = LogisticRegression()
            modelo.fit(x, respostas_numericas)

            with open(ia, "wb") as arquivo:
                pickle.dump((vetorizar, modelo, respostas_map), arquivo)
            arq1 = "csv/iacomandos.csv"
            arq2 = "csv/iaexecutar.csv"
            ia = "pkl/comandos_ia.pkl"
        print("Treinado com sucesso")

if __name__ == "__main__":
    Treinamento()
