from random import randint


numeros = []
while True:
    if len(numeros) < 6:
        jogada = randint(1, 60)
        if jogada not in numeros:
            numeros.append(jogada)
    else:
        break


for numero in numeros:
    print(numero)