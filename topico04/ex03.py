# Faça um programa que crie uma lista vazia. Em seguida,
# o usuário deverá informar as notas de trabalhos obtidas
# (pode variar de 0 até quantos trabalhos forem informados).
# Por fim, mostre a média aritmética das notas obtidas.

notas = []

while True:

    nota = int(input('Digite uma nota: '))

    if nota == -1:
        break

    notas.append(nota)


media = sum(notas)/len(notas)
print(media)