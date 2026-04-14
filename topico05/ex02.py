# Faça um programa que crie dois conjuntos x e y,
# com dez números inteiros cada um. Em seguida, crie:
# 1) Um conjunto resultante da união de x e y (todos os
# elementos de x e os elementos de y que não estão em x).
# 2) Um conjunto resultante da diferença entre x e y (todos
# os elementos de x que não existam em y).
# 3) Um conjunto resultante interseção entre x e y

x = {1, 2, 3}
y = {3, 4, 5}

# união
a = x | y
print(a)

# diferença
print(x - y)

# interseção
print(x & y)