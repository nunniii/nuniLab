
s = {1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7}  #{i...0}
print(s)

"""Type == <class 'set'>"""
print(type(s))

"""Pesquisa dentro do conjunto"""
def i3(num):
    return num in s
print(i3(4))

print(i3(8))

s = set('54632877565')
print(s)

"""Operações"""
a = {0, 1, 2, 3, 4, 5, 6}
b = {3, 4, 5, 6, 7, 8, 9}

print(a ^ b)
print(a - b)  
print(a | b)
print(a & b)
