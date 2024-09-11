"""
Este script mostra qual caractere mais aparece na string
"""

while True:
    minha_string = input("Digite uma frase: ")
    tamanho_string = len(minha_string)
    c = 0
    contagem = 0
    letra = ''

    while c < tamanho_string:
        conta = minha_string.count(minha_string[c])
        if contagem < conta and minha_string[c].split():
            letra = minha_string[c]
            contagem = conta
        c += 1
    print(letra, contagem)
