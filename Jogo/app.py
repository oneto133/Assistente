from flask import Flask, render_template, request
from random import randint
import pandas as pd
app = Flask(__name__)

class Saldo():
    def verificar(self, arq="csv/saldo.csv"):
        try:
            arq = pd.read_csv(arq, encoding="latin1")
            return arq.columns[0]
        except:
            print("Arquivo vazio")
            return 0  # Retorna 0 em caso de erro

    def alterar(self, valor, arq="csv/saldo.csv"):
        with open(arq, "w") as file:
            file.write(f"{valor}")

class main():
    def __init__(self):
        self.saldo = Saldo()

    def jogo(self, valor_aposta):
        saldo = float(self.saldo.verificar())
        casa = float(self.saldo.verificar("csv/casa.csv"))
        numero = self.numeros()

        if saldo <= 0:
            return {"mensagem": "Saldo insuficiente, faça uma recarga...", "saldo": saldo}

        if numero[0] == numero[1] and numero[1] == numero[2]:
            ganho = valor_aposta * 4
            novo_saldo = saldo + ganho
            self.saldo.alterar(novo_saldo)
            novo_casa = casa - ganho
            self.saldo.alterar(valor=novo_casa, arq="csv/casa.csv")
            return {"mensagem": f"+{ganho}", "saldo": novo_saldo, "numeros": numero}
        else:
            novo_saldo = saldo - valor_aposta
            self.saldo.alterar(str(novo_saldo))
            novo_casa = casa + valor_aposta
            self.saldo.alterar(valor=novo_casa, arq="csv/casa.csv")
            return {"mensagem": f"-{valor_aposta}", "saldo": novo_saldo, "numeros": numero}

    def numeros(self):
        numero1 = randint(1, 3)
        numero2 = randint(1, 3)
        numero3 = randint(1, 3)
        return numero1, numero2, numero3

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        valor_aposta = float(request.form["valor_aposta"])
        resultado_jogo = main().jogo(valor_aposta)
        return render_template("index.html", resultado=resultado_jogo)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)