# Crie um programa que solicite ao usuário 
# uma palavra, em seguida conte e mostre quantas
# vogais existem na palavra digitada.

palavra = input('Digite uma palavra: ') # bola

contador = 0

vogais = 'aeiou'

for letra in palavra:
    if letra in vogais:
        contador += 1

# for letra in palavra:
#     for vogal in vogais:
#         if letra == vogal:
#             contador += 1

# for letra in palavra:
#     if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
#         contador += 1

print(f'A palavra {palavra} tem {contador} vogais.')