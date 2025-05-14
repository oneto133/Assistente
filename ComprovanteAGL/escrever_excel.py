import openpyxl
import pandas as pd

class main:
    def __init__(self):
        pass

    def programa(self, data, origem, destino, metodo, categoria, valor):
        arquivo = r"C:\Users\rodri\OneDrive\transporteAGL.xlsx"
        df = pd.read_csv(r"csv/indice_nota.csv")
        linha_destino = int(df.columns[0]) #Normalmente as linhas dentro do csv estão em strings
        coluna_destino = 1
        ler = openpyxl.load_workbook(arquivo, data_only=False)
        planilha1 = ler["Planilha1"]
        dados = [data, origem, destino, metodo, categoria, float(valor)]

        for coluna, valor in enumerate(dados):
            planilha1.cell(row=linha_destino, column=coluna_destino + coluna, value=valor)
        
        with open("csv/indice_nota.csv", "w") as file:
            file.write(f"{linha_destino+1}")
        ler.save(arquivo)


if __name__ == "__main__":
    program = main()
    
