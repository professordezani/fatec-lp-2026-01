# Usando while, faça um programa que mostre a tabuada 
# de um número informado.

numero = int(input('Digite um número: '))

i = 1

while i <= 10:
    print(f'{numero} x {i:2} = {numero * i}')
    i += 1