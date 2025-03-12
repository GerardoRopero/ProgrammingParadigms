import MaquinaTuring

while True:
    print("------ Menú -------")
    print("1. Salir")
    print("2. Suma")
    print("3. Resta")
    print("4. Multiplicación")
    print("5. División")
    print("6. Raíz cuadrada")
    print("7. Potencia")
    print("8. Logaritmo natural")
    print("9. Seno")


    option = input("Elige una opción: ")

    if not option.isdigit():
        print("Por favor, ingresa un número válido.\n")
        continue

    option = int(option)

    if option == 1:
        print("Saliendo del programa...")
        break

    if option not in [2, 3, 4, 5, 6, 7, 8, 9]:
        print("Opción no válida. Inténtalo de nuevo.\n")
        continue

    if option in [2, 3, 4, 5, 7]:
        input1 = input("Ingresa el primer número: ")
        input2 = input("Ingresa el segundo número: ")

        if not input1.isdigit() or not input2.isdigit():
            print("Por favor, ingresa solo números enteros positivos.\n")
            continue

        input1, input2 = int(input1), int(input2)

    elif option == 6 or option == 8 or option == 9:
        input1 = input("Ingresa el número: ")

        if not input1.isdigit():
            print("Por favor, ingresa un número entero positivo.\n")
            continue

        input1 = int(input1)

    if option == 2:
        output = MaquinaTuring.suma(input1, input2)
    elif option == 3:
        output = MaquinaTuring.resta(input1, input2)
    elif option == 4:
        output = MaquinaTuring.multiplicacion(input1, input2)
    elif option == 5:
        if input2 == 0:
            print("Error: No se puede dividir por cero.\n")
            continue
        output = MaquinaTuring.division(input1, input2)
    elif option == 6:
        output = MaquinaTuring.raiz_cuadrada(input1)
    elif option == 7:
        output = MaquinaTuring.potencia(input1, input2)
    elif option == 8:
        output = MaquinaTuring.logaritmo_natural(input1)
    else:
        output = MaquinaTuring.seno(input1)


    print(f"El resultado es: {output}\n")