gcd = (lambda f: (lambda a, b: a if b == 0 else f(f)(b, a % b)))(lambda f: (lambda a, b: a if b == 0 else f(f)(b, a % b)))
