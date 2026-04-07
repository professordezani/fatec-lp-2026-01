# Faça um programa que gere 10 números inteiros. 
# Em seguida, crie uma nova lista removendo os números
# repetidos. No final, mostre essa nova lista.
numeros = [1, 2, 3, 4, 3, 2, 7, 5, 8, 6]


numeros_nao_repetidos = []

for numero in numeros:
    if numero not in numeros_nao_repetidos:
        numeros_nao_repetidos.append(numero)

print(numeros_nao_repetidos)