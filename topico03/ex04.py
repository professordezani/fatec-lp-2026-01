# Usando while, faça um programa que leia um número 
# inteiro N e mostre na tela os N primeiros números da 
# Sequência de Fibonacci.
# Por exemplo, N = 7
# Output: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

n = int(input('Digite a quantidade de elementos: '))

a = 0
b = 1

print(a, end=' ')

contador = 1

while contador < n:
    print('->', b, end=' ')
    a, b = b, a + b
    # aux = b
    # b = a + b
    # a = aux
    contador += 1