
l = ['a', 'b', 'c']

def InverterLista(lista):
    tamanhoDaLista = len(lista)
    metadeDoTamanhoDaLista = tamanhoDaLista//2
    for item in range(metadeDoTamanhoDaLista):
        aux = lista[item]
        lista[item] = lista[(tamanhoDaLista - 1) - item]
        lista[(tamanhoDaLista - 1) - item] = aux
    return lista

print(InverterLista(l))
