# Escreva um programa que leia o salário de um
# funcionário e calcule o seu aumento. Caso o 
# salário atual seja superior a R$ 1.000,00 
# calcule um aumento de 10%, caso contrário, 
# calcule um aumento de 15%.

salario = float(input('Digite o salário: '))

if salario > 1000:
    novo_salario = salario * 1.10
else:
    novo_salario = salario * 1.15

print(novo_salario)