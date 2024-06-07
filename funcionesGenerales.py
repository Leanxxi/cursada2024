def ingresar_entero(mensaje="Ingrese un número entero: ") -> int:
    """
    Solicita al usuario que ingrese un número entero, lo valida y lo devuelve.

    Args:
        mensaje (str): El mensaje que se muestra al solicitar la entrada.

    Returns:
        int: El número entero ingresado por el usuario.
    """
    while True:
        entrada = input(mensaje)
        try:
            numero = int(entrada)
            print("Valor ingresado:", numero)
            return numero
        except ValueError:
            print("Error: La entrada no es un número entero válido. Inténtelo de nuevo.")

def ingresar_entero_positivo(mensaje = "ingrese entero positivo")->int:
    """ingresa un numero entero, lo valida y lo devuelve

    Returns:
        int: numero entero ingresado
    """

    while True:
        entero = input(mensaje)
        if entero.isdigit():
            numero = int(entero)
            print("valor ingresado:", numero)
            return numero
        else:
            print("Error: La entrada no es un número.")

def mostrar_lista(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(f"|| {lista[i][j]}", end= " ")
        print("")
