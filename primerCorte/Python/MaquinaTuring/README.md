# Turing Machine&#x20;

## Descripción

Este proyecto implementa una calculadora basada en una **Máquina de Turing** para realizar operaciones matemáticas básicas y avanzadas. Se compone de dos archivos principales:

- `MaquinaTuring.py`: Define la estructura y lógica de la Máquina de Turing, implementando operaciones como suma, resta, multiplicación, división, raíz cuadrada, potencia, logaritmo natural y seno.
- `Console.py`: Proporciona una interfaz de línea de comandos donde los usuarios pueden seleccionar la operación que desean realizar.

---

## Funcionamiento

El programa `Console.py` ejecuta un menú interactivo donde el usuario puede elegir una operación matemática. Dependiendo de la opción seleccionada, se solicita uno o dos números enteros como entrada, los cuales son procesados por `MaquinaTuring.py`.

Cada operación matemática es simulada mediante una Máquina de Turing con un conjunto de estados y reglas de transición.

### ¿Cómo funciona la Máquina de Turing?

La Máquina de Turing es un modelo teórico de computación que utiliza una cinta infinita dividida en celdas, un cabezal de lectura/escritura y un conjunto de reglas de transición para modificar los símbolos en la cinta.

El proceso de ejecución consiste en:

1. Inicializar la cinta con la entrada dada.
2. Leer el símbolo actual en la posición del cabezal.
3. Determinar la siguiente acción según el estado actual y el símbolo leído.
4. Modificar el símbolo en la cinta si es necesario.
5. Mover el cabezal a la izquierda (L) o derecha (R).
6. Repetir el proceso hasta alcanzar un estado final.

### Operaciones soportadas

1. **Suma** (`suma(x, y)`)

   - Convierte los números en una representación basada en "1s".
   - Los concatena en la cinta con un separador `+`.
   - Recorre la cinta y sustituye el separador por un "1", lo que efectúa la suma.

2. **Resta** (`resta(x, y)`)

   - Representa los números en "1s", separados por `-`.
   - Itera sobre la cinta eliminando pares de "1s", reduciendo el número en la izquierda.
   - Finaliza cuando no quedan más "1s" en la segunda parte.

3. **Multiplicación** (`multiplicacion(x, y)`)

   - Simula la multiplicación como sumas sucesivas.
   - Usa la función de suma repetidamente `y` veces.

4. **División** (`division(x, y)`)

   - Implementada como restas sucesivas.
   - Cada iteración resta `y` de `x` hasta que `x < y`.

5. **Raíz cuadrada** (`raiz_cuadrada(x)`)

   - Reduce `x` usando la fórmula `x - (2i + 1)`, donde `i` es el contador de iteraciones.
   - Cuando `x < 0`, el valor de `i` es la raíz aproximada.

6. **Potencia** (`potencia(x, y)`)

   - Calculada mediante multiplicaciones sucesivas de `x`, `y` veces.

7. **Logaritmo natural** (`logaritmo_natural(x)`)

   - Divide `x` por 3 de forma iterativa.
   - Cuenta el número de divisiones hasta llegar a 1 o un número cercano.

8. **Seno** (`seno(x)`)

   - Se aproxima con la serie de Taylor para `sen(x) = Σ (-1)^n * x^(2n+1) / (2n+1)!`.
   - Calcula cada término usando la Máquina de Turing para potencia, factorial y división.

---

## Estructura del Código

### `MaquinaTuring.py`

- **Funciones matemáticas**: Implementan operaciones matemáticas usando la Máquina de Turing.
- **Conversión de entradas**: Convierte números a la representación de la Máquina de Turing.
- **Procesamiento y simulación**: Ejecuta las reglas de transición en la cinta de la Máquina de Turing.

### `Console.py`

- Muestra un menú con las opciones disponibles.
- Solicita la entrada del usuario y valida los datos ingresados.
- Llama a las funciones de `MaquinaTuring.py` para realizar los cálculos.
- Muestra el resultado de la operación seleccionada.

---

## Ejemplo de Uso

Ejemplo de ejecución del programa en la terminal:

```bash
------ Menú -------
1. Salir
2. Suma
3. Resta
4. Multiplicación
5. División
6. Raíz cuadrada
7. Potencia
8. Logaritmo natural
9. Seno
Elige una opción: 2
Ingresa el primer número: 3
Ingresa el segundo número: 5
El resultado es: 8
```

---

