
def fun():
    return

print(type(fun))
print(fun())

def g(var = None):
    return var
def f():
    return g
def fun():
    return f

print(fun()()())
