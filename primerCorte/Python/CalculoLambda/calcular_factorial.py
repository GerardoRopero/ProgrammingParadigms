from functools import reduce

factorial_recursivo = (lambda x: (lambda y: 1 if y == 0 else y * x(x)(y - 1)))(lambda x: (lambda y: 1 if y == 0 else y * x(x)(y - 1)))
factorial_iterativo = lambda n: 1 if n == 0 else reduce(lambda x, y: x * y, range(1, n + 1))

print(factorial_recursivo(5))
print(factorial_iterativo(5))
