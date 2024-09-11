"""
Este script ativa .upper() em todas as letras após um espaço.
"""

while True:

    minha_string = str(input("Digite uma frase: "))
    nova_string = ''

    c = 0
    tamanho_da_string = len(minha_string)

    while c < tamanho_da_string:
        if minha_string[c] == ' ':
            nova_string = nova_string + minha_string[c]
            nova_string = nova_string + minha_string[c + 1].upper()
        else:
            if minha_string[c - 1] == ' ':
                pass
            else:
                nova_string = nova_string + minha_string[c]

        print(nova_string)
        c += 1

    print(nova_string)
