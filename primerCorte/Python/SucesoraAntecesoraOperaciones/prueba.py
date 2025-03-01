def S(n):
    return n + 1

def A(n):
    return n - 1

def suma(a, b):
    while b > 0:
        a = S(a)
        b = A(b)
    return a

def resta(a, b):
    while b > 0:
        a = A(a)
        b = A(b)
    return a

def multiplicacion(a, b):
    c = 0
    while b > 0:
        c = suma(c, a)
        b = A(b)
    return c

def division(a, b):
    if b == 0:
        return None
    c = 0
    while a >= b:
        a = resta(a, b)
        c = S(c)
    return c
