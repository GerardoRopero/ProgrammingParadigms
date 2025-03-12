import math

class TuringMachine:
    def __init__(self, states, input_alphabet, tape_alphabet, initial_state, blank_symbol, final_states, transition_function):
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.state = initial_state
        self.blank_symbol = blank_symbol
        self.final_states = final_states
        self.transition_function = transition_function
        self.tape = []
        self.head = 0

    def reading_writing(self):

        if self.state in self.final_states:
            return False

        symbol = self.tape[self.head]
        if (self.state, symbol) not in self.transition_function:
            return False

        self.state, symbol, move = self.transition_function[(self.state, symbol)]

        self.tape[self.head] = symbol

        if move == 'R':
            self.head += 1
        elif move == 'L':
            self.head -= 1

        return True

    def run(self, input_string):
        self.tape = list(input_string) + [self.blank_symbol]
        self.head = 0

        while self.reading_writing():
            pass
        return ''.join(self.tape).strip(self.blank_symbol)

def limpiar_entrada(entrada):

    return '1' * int(entrada)

def limpiar_salida(salida):
    negativo = "-" in salida
    valor = salida.replace("+", "").replace("-", "").replace("_", "").count("1")
    return -valor if negativo else valor

def suma(x, y):
    maquina_turing = TuringMachine(
            {'q0', 'q1', 'q2', 'q3'},
            {'+', '1'},
            {'+', '1', '_'},
            'q0',
            '_',
            {'q3'},
            {
                ('q0', '1'): ('q0', '1', 'R'),
                ('q0', '+'): ('q1', '1', 'R'),
                ('q1', '1'): ('q1', '1', 'R'),
                ('q1', '_'): ('q2', '_', 'L'),
                ('q2', '1'): ('q2', '_', 'S'),
            }
        )

    output = maquina_turing.run(f"{limpiar_entrada(x)}+{limpiar_entrada(y)}")
    return limpiar_salida(output)

def resta(x, y):
    maquina_turing_resta = TuringMachine(
        {"q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12", "q13", "q14", "q15"},
        {'-', '1'},
        {'-', '1', '_', '0'},
        'q0',
        '_',
        {'q2', 'q6', 'q10'},
        {
            ('q0', '-'): ('q1', '-', 'R'),
            ('q1', '1'): ('q2', '1', 'S'),
            ('q1', '_'): ('q3', '_', 'L'),
            ('q3', '-'): ('q4', '-', 'L'),
            ('q4', '_'): ('q5', '_', 'R'),
            ('q5', '-'): ('q6', '0', 'S'),
            ('q0', '1'): ('q7', '1', 'R'),
            ('q7', '1'): ('q7', '1', 'R'),
            ('q7', '-'): ('q8', '-', 'R'),
            ('q8', '_'): ('q9', '_', 'L'),
            ('q9', '-'): ('q10', '_', 'S'),
            ('q8', '1'): ('q11', '1', 'R'),
            ('q11', '1'): ('q11', '1', 'R'),
            ('q11', '_'): ('q12', '_', 'L'),
            ('q12', '1'): ('q13', '_', 'L'),
            ('q13', '1'): ('q13', '1', 'L'),
            ('q13', '-'): ('q14', '-', 'L'),
            ('q14', '1'): ('q14', '1', 'L'),
            ('q14', '_'): ('q15', '_', 'R'),
            ('q15', '1'): ('q0', '_', 'R'),
        }
    )
    output = maquina_turing_resta.run(f"{limpiar_entrada(x)}-{limpiar_entrada(y)}")
    return limpiar_salida(output)

def multiplicacion(x, y):
    if y == 0:
        return 0
    if y == 1:
        return x
    return suma(x, multiplicacion(x, resta(y, 1)))

def division(x, y):
    if y > x:
        return 0
    return suma(1, division(resta(x, y), y))

def potencia(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    return multiplicacion(x, potencia(x, resta(y, 1)))


def raiz_cuadrada(x, i = 0):
    if x < 0 or x == 0:
        return i
    return raiz_cuadrada(resta(x, suma(1, multiplicacion(2, i))), suma(i, 1))

def logaritmo_natural(x, iteracion = 0):
    if x < 3:
        return iteracion
    return logaritmo_natural(division(x, 3), suma(iteracion, 1))

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return multiplicacion(x, factorial(resta(x, 1)))

def seno(x, precision=10):
        resultado = 0
        signo = 1

        for n in range(precision):
            exponente = suma(multiplicacion(2, n), 1)  # 2n + 1
            factorial_val = factorial(exponente)  # (2n+1)!
            potencia_val = potencia(x, exponente)  # x^(2n+1)
            termino = division(potencia_val, factorial_val)  # x^(2n+1) / (2n+1)!

            if n % 2 == 1:
                termino = resta(0, termino)  # Alternar signos (-1)^n

            resultado = suma(resultado, termino)

        return resultado







