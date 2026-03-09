# Faça um programa para jogar Jokenpô (clássico pedra, papel 
# e tesoura) com você. Você deverá informar uma das opções, 
# o programa deverá então sortear uma das três opções possíveis
# e mostrar quem ganhou na tela.
import random

computador = random.randint(0, 2)

if computador == 0:
    computador = 'pedra'
elif computador == 1:
    computador = 'papel'
else: 
    computador = 'tesoura'

jogador = input('Digite a opção: ')

estado_vitoria1 = computador == 'pedra' and jogador == 'tesoura'
estado_vitoria2 = computador == 'tesoura' and jogador == 'papel'
estado_vitoria3 = computador == 'papel' and jogador == 'pedra'

if computador == jogador:
    print('Empate')
elif estado_vitoria1 or estado_vitoria2 or estado_vitoria3:
     print('O computador ganhou')
else:
    print('O jogador ganhou')