f = lambda x: x**2 - 4

biseccion = (lambda f, a, b, tol: (lambda g: g(g, a, b, tol))(
    lambda self, a, b, tol: (
        (lambda c: c if abs(f(c)) < tol else
            self(self, a, c, tol) if f(a) * f(c) < 0 else
            self(self, c, b, tol))((a + b) / 2)
    )
))(f, 1, 3, 1e-6)

print("Raíz encontrada:", biseccion)

