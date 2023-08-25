
# Solução primeira -> (n - 1) - 2
def fun1(n):
    if n > 1:
        for i in range(2, n - 1):
            if n % i == 0:
                return False
        return True
    return False

print(fun1(997))

# Solução segunda -> (int(sqrt(n)) - 2)

import math
def fun2(n):
    if n > 1:
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                return False
        return True
    return False

print(fun2(997))
