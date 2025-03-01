def S(n):
    return n + 1

def A(n):
    return n - 1 

def suma(a, b):
    if b == 0:
        return a
    return S(suma(a, A(b)))

def multiplicacion(a, b):
    if b == 0:
        return 0
    return suma(a, multiplicacion(a, A(b)))

def resta(a, b):
    if b == 0:
        return a
    return resta(A(a), A(b))

def division(a, b):
    if b == 0:
        return None
    if b > a:
        return 0
    return S(division(resta(a, b), b))