# Peça para o usuário digitar o seu ano de nascimento. O programa 
# deve calcular e mostrar a idade atual dele, considerando
# que o ano atual é 2026.
from datetime import datetime

ano_atual = datetime.today().year

ano_nascimento = int(input('Digite o ano de nascimento: '))

idade = abs(ano_nascimento - ano_atual)

print(f'{idade} anos.')