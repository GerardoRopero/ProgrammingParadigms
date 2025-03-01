from math import factorial, radians

cos_lambda = lambda x, n: sum(((-1) ** k * x ** (2 * k)) / factorial(2 * k) for k in range(n))

x_grados = 45
x_radianes = radians(x_grados)

n = 10

resultado = cos_lambda(x_radianes, n)

print(f"cos({x_grados}°) ≈ {resultado}")
