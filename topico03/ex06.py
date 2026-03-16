# Você recebe uma string e sua tarefa é trocar casos. 
# Em outras palavras, converta todas as letras minúsculas
# em maiúsculas e vice-versa.
# Input: Fatec Rio Preto
# Output: fATEC rIO pRETO

texto = input('Digite um texto: ')

novo_texto = ''

for letra in texto:
    if letra.isupper():
        novo_texto = novo_texto + letra.lower()
    else:
        novo_texto = novo_texto + letra.upper()

print(novo_texto)