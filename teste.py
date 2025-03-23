from random import randint
numero: int
numero = randint(1,60)
lista = list()

lista.append(numero)

while len(lista) < 6:
    num = randint(1, 60)
    if num not in lista:
        lista.append(num)

print(lista) 