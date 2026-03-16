# Usando while, escreva um programa que cadastre o estado civil 
# de uma pessoa, entretanto, o programa deve continuar
# perguntando enquanto o valor informado for diferente 
# de "solteiro" ou "casado".

# estado_civil = input('Digite o estado civil: ')

# while estado_civil != 'solteiro' and estado_civil != 'casado':
#     estado_civil = input('Digite o estado civil: ')

while True:
    estado_civil = input('Digite o estado civil: ')
    if estado_civil == 'solteiro' or estado_civil == 'casado':
        break
