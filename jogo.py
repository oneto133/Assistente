"""
Esse é um jogo do tipo que cassino que só vai servir para a minha diversão, apenas para jogar dinheiro fora,
 se eu ganhar ganhei, se eu perder perdi"""




from random import randint
import pandas as pd


class main():
    def __init__(self):
        self.saldo = Saldo()

        self.jogo()

    def jogo(self):
        user = input("Welcome! press Enter to start game: ")
        print("""O Objetivo do jogo é realizar 3 cobinações perfeitas, no inicio do jogo\n
você irá definir de quanto em quanto você quer apostar, conforme você for ganhando\n
o seu saldo será acrescentadoe se perder, será subtraído, caso o seu saldo zere\n
não será mais possível realizar jogadas até que um valor seja adicionado\n\n\n
Divirta-se!""")
        
        valor = float(input(f"Seu saldo é {float(self.saldo.verificar()):.2f}\n"
        "Escolha o valor da sua aposta: "))

        while valor > float(self.saldo.verificar()):
            valor = float(input(f"Insira um valor menor que {self.saldo.verificar()}: "))
        jogo = input("Digite Sair para sair do jogo ou Enter para inicar: ")
        user = [valor]
        while jogo != "Sair":
            valor = float(user[0])
            saldo = self.saldo.verificar()
            casa = self.saldo.verificar("csv/casa.csv")
            if float(saldo) <= 0:
                print("Saldo insuficiente, faça uma recarga...")
                break
            
            numero = self.numeros()
            print(numero)
            if numero[0] == numero[1] and numero[1] == numero[2]:
                print(f"+{valor*3}")
                valor = float(self.saldo.verificar()) + float(valor*3)
                self.saldo.alterar(valor)
                valor = float(casa) - float(user[0])*3
                self.saldo.alterar(valor=valor, arq="csv/casa.csv")
            elif int(numero[0]) == 1 and int(numero[1]) == 2 and int(numero[2]) == 3:
                print(f"+{valor*2}")
                valor = float(self.saldo.verificar()) + float(valor*2)
                self.saldo.alterar(valor)
                valor = float(casa) - float(user[0])*2
                self.saldo.alterar(valor=valor, arq="csv/casa.csv")
            
            else:
                print("-{valor}".format(valor=valor))
                valor = float(saldo) - float(valor)
                self.saldo.alterar(str(valor))
                valor = float(casa) + float(user[0])
                self.saldo.alterar(valor=valor, arq="csv/casa.csv")

            print(f"Seu saldo é {float(self.saldo.verificar()):.2f}")
            jogo = input("")
            
    def numeros(self):
        numero1 = randint(1,3)
        numero2 = randint(1,3)
        numero3 = randint(1,3)

        return numero1, numero2, numero3
class Saldo():
    def verificar(self, arq="csv/saldo.csv"):
        try:
            arq = pd.read_csv(arq, encoding = "latin1")
            return arq.columns[0]
        except:
            print("Arquivo vazio")
    def alterar(self, valor, arq="csv/saldo.csv"):
        with open(arq, "w") as file:
            file.write(f"{valor}")


if __name__ == "__main__":
    main()
