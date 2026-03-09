media = float(input('Digite a média: '))
faltas = int(input('Digite a quantidade de faltas: '))

if media < 4 or faltas > 20:
    print('reprovado')
elif media < 6:
    print('exame')
else:
    print('aprovado')