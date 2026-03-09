# Escreva um programa que leia a velocidade de um carro. 
# Se esta velocidade for maior que 80Km/h o programa deverá
# escrever uma mensagem na tela avisando que o usuário levou
# uma multa e o valor a ser pago. Considere R$ 7 reais por
# cada Km acima do limite.

velocidade = int(input('Digite a velocidade: '))

VELOCIDADE_MAXIMA = 80

if velocidade > VELOCIDADE_MAXIMA:
    multa = (velocidade - VELOCIDADE_MAXIMA) * 7
    print(f'Você levou uma multa de R$ {multa:.2f}.')
