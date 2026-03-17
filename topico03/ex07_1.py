# Faça um programa que faça a entrada de um texto. 
# Se for um e-mail, retorne "E-mail válido", caso contrário,
# retorne "E-mail inválido". Para tanto, verifique se o texto
# possui o símbolo @

# Refaça o código abaixo usando while.
email = input('Digite um e-mail: ')
i = 0

while i < len(email):
    if email[i] == '@':
        print('E-mail válido.')
        break
    i += 1
else:
    print('E-mail inválido.')