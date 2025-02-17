import csv
import pandas as pd

perguntas = []

#Criado apenas para organizar os dados dentro do arquivo csv


'''
with open("resposta.csv", 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        perguntas.append(linha)

print(perguntas)
'''
with open('csv/respostas.csv', 'a', encoding='utf-8', newline="") as arquivo:
    df = pd.read_csv('resposta.csv')
    for coluna in df.columns:
        arquivo.write(f'"{coluna}"\n')
