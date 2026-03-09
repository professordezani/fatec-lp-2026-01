# Faça um program que leia o ano de nascimento de uma
# pessoa e informe se ele ainda vai se alistar ao serviço 
# militar ou se ele está no período de se alistar ou se 
# ele perdeu o prazo para se alistar. Além disso, mostre 
# também a quantidade de anos que falta para se alistar 
# ou que passou do prazo.

from datetime import datetime as dt

ANO_ATUAL = dt.today().year

ano_nascimento = int(input('Digite o ano do nascimento: '))

idade = ANO_ATUAL - ano_nascimento
diferenca = abs(18 - idade)

if idade < 18:
    print(f'Ainda não chegou o ano para se alistar. Falta {diferenca} anos.')
elif idade == 18:
    print('Você precisa se alistar.')
else:
    print(f'Você perdeu o prazo do alistamento. Passou {diferenca} anos.')