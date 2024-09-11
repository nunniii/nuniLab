"""Métodos em listas"""
lista_de_frutas = ['banana' , 'goiaba', 'laranja', 'maracujá']

""".append() : anexar ítem ao final da lista"""
lista_de_frutas.append('caju')

""".extend() : amplia lista anexando elementos do interável"""
lista_de_frutas.extend(['pêssego', 'uva'])
#Note a diferença: .extend não adicionou a lista ['pêssego, 'uva'] e sim, os interáveis dela. (isto que difere do .append().

""".insert(índice, objeto) : insere objeto no índice"""
lista_de_frutas.insert(2, 'melancia')

""".pop() : remove o último ítem da lista"""
lista_de_frutas.pop()

"""remove() : remove a primeira ocorrência de um objeto"""
lista_de_frutas.remove('laranja')

""".index() : retorna o índice de tal elemento"""
lista_de_frutas.index('banana')

"""len(list) : retorna tamanho da lista"""
len(lista_de_frutas)

""".reverse() : inverte a ordem da lista"""
lista_de_frutas.reverse()

""".sort() : ordena a lista"""
lista_de_frutas.sort()
