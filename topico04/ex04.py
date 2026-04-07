# Faça um programa que contenha duas listas com 5 posições.
# Na primeira lista, deverá ser inserido o nome dos alunos.
# Na segunda lista, na mesma posição, a nota do aluno. Em
# seguida, mostre o nome dos alunos com a maior e a menor nota.

nomes = ['João', 'Matheus', 'Marcela', 'Maria', 'Henrique']
notas = [8.5, 3.2, 7.6, 9.2, 5.4]

maior_nota = max(notas)
menor_nota = min(notas)

indice_maior_nota = notas.index(maior_nota) # 3
indice_menor_nota = notas.index(menor_nota) # 1

print(nomes[indice_maior_nota], nomes[indice_menor_nota])