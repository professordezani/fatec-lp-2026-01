# Faça um programa para aprovar o empréstimo bancário para
# a compra de uma casa. O usuário deverá informar o valor
# da casa, a quantidade de parcelas que deseja pagar e seu
# salário. O empréstimo deverá ser negado caso o valor da
# parcela exceda 30% do salário.

valor_casa = float(input('Digite o valor da casa: '))
quantidade_parcelas = int(input('Digite a quantidade de parcelas: '))
salario = float(input('Digite o salário: '))

valor_parcela = valor_casa/quantidade_parcelas

if valor_parcela > salario * 0.3:
    print('Empréstimo negado.')
else:
    print('Empréstimo aprovado.')
