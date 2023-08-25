class uppercase(object):

    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args):
        return self.fun(args[0].upper())

@uppercase
def nome(name):
    return name

print(nome('João'))