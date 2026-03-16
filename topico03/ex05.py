# Usando for, faça um programa que leia um número 
# inteiro e mostre na tela se é ou não um número primo.

numero = int(input('Digite um número: '))

# numero = 6
# range(2, 6) = [2, 3, 4, 5]

for i in range(2, numero):
    if numero % i == 0:
        print(f'{numero} não é um número primo.')
        break
else:
    print(f'{numero} é um número primo.')