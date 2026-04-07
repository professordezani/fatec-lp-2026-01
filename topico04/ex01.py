# Faça um programa que carregue uma lista com dez
# números inteiros. Em seguida, 
# crie e mostre uma lista resultante ordenada de maneira 
# crescente e crie e mostre uma lista resultante ordenada 
# de maneira decrescente.

# lista = [1, 3, 5, 2, 7, 8, 9, 4, 6, 0]

import random

lista = random.sample(10, range(100))

lista_ordenada_crescente = sorted(lista)
lista_ordenada_decrescente = sorted(lista, reverse=True)

print(lista_ordenada_crescente)
print(lista_ordenada_decrescente)