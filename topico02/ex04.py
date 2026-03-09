# Faça um programa em que ele sorteie um número entre 0 e 5. 
# O usuário deverá então adivinhar este número e o programa
# deverá escrever na tela se ele acertou ou não.
from random import randint

numero_sorteado = randint(0,5)

numero_escolhido = int(input('Digite um número: '))

if numero_escolhido == numero_sorteado:
    print('Parabéns!')
else:
    print(f'Você erro, o número sorteado foi {numero_sorteado}.')