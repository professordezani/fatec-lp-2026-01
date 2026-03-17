# Crie um programa que solicite ao usuário um número
# inteiro N e calcule a soma de todos os números pares
# de 1 até N (exlusivo, ou seja, N não deve ser
# considerado na soma)

n = int(input('Digite um número: ')) # 7

soma = 0

# for i in range(1, n):
#     if i % 2 == 0:
#         soma += i

for i in range(2, n, 2):
    soma += i

print(soma)