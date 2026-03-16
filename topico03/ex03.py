# Usando while, escreva um programa que leia um
# número inteiro qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input('Digite um número: '))

fatorial = numero

while numero > 1:
    numero -= 1
    fatorial = fatorial * numero

print(fatorial)