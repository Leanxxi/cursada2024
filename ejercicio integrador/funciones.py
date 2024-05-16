# En un local de venta de zapatillas, se necesita desarrollar un programa para llevar un
# registro de las compras realizadas durante toda una semana. El programa debe permitir al
# usuario ingresar las compras diarias y calcular ciertas estadísticas al final de la semana.
# Funcionalidades del Programa:
# 1. Registro de Ingresos: El usuario podrá guardar en una única lista los ingresos totales
# realizados durante cada día de la semana.
# 2. Análisis de Datos:
# ● Determinar el día con más ingresos.
# ● Determinar el día con menos ingresos.
# ● Calcular el promedio de ingresos en la semana.
# ● Calcular el total de ingresos en la semana.
# ● Calcular el promedio de ingresos en días laborables (de lunes a viernes) y en
# días del fin de semana (sábado y domingo).
# ● Calcular el día con la mayor variación en los ingresos respecto al día anterior.
# 3. Muestra de datos: Una vez calculados todos los datos del punto 2, se deberán
# imprimir en pantalla

def ingresar_entero(mensaje = "ingrese entero")->int:
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


def ingresar_flotante()->float:
    """ingresa un caracter, intenta cambiarlo a un numero flotante, si tiene exito lo devuelve y rompe el bucle
    si no muestra un mensaje de error
    Returns:
        float: numero flotante ingresado
    """
    while True:  # Bucle para continuar solicitando hasta que se ingrese un flotante válido
        entrada = input("Ingrese un número flotante: ")
        try:
            # Intenta convertir la entrada a un número flotante
            numero = float(entrada)
            # Si tiene éxito, rompe el bucle y devuelve el número flotante
            return numero
        except ValueError:
            # Si falla la conversión, muestra un mensaje y continúa el bucle
            print("Error: El dato ingresado no es un número flotante. Inténtelo de nuevo.")