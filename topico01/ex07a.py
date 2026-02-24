# Implemente um programa que tenha como entrada o valor em
# reais e mostre o valor correspondente em dólar.

import requests

response = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')

resultado = response.json()

COTACAO_DOLAR = float(resultado['USDBRL']['bid'])

reais = float(input('Digite o valor em reais: '))

dolar = reais / COTACAO_DOLAR

# print(f'{reais} corresponde a {dolar:.2f} dolares.')
print(f'{reais} corresponde a {round(dolar, 2)} dolares.')
