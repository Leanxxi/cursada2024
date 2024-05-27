# El programa debe permitir al usuario ingresar los siguientes datos para 10 alumnos:
# ● Nombre
# ● Edad
# ● DNI
# ● Género (M para masculino, F para femenino, NB para No Binario)
# ● Nota
# Después de ingresar los datos de todos los alumnos, el programa debe calcular y
# mostrar la siguiente información:

# 1. Listado de todos los alumnos con un formato similar al siguiente:

# 2. El promedio de edades de los alumnos.
# 3. La cantidad de alumnos que promocionaron (nota mayor o igual a 6).
# 4. La cantidad de alumnos que aprobaron (nota mayor o igual a 4).
# 5. La cantidad de alumnos que desaprobaron (nota menor a 4).
# 6. El promedio de nota de los alumnos masculinos.
# 7. El porcentaje de alumnas que promocionaron sobre el total de alumnas

from funciones_matrices import (ingresar_entero)

def mostrar_menu_principal():
    """muestra las opciones que se pueden elegir del programa principal
     Args:
        No recibe argumentos.

    Returns:
        No devuelve ningún valor.
    """
    print("""       Bienvenido al Menu 
            1-
            2-
            3-
            4-salir

    """)

def menu_principal():
    """menu principal del programa
     Args:
        No recibe argumentos.

    Returns:
        No devuelve ningún valor.
    """
    bandera_de_calculos = False
    while True:
        mostrar_menu_principal()
        opcion = ingresar_entero('ingrese opcion')
        match opcion: 
            case 1:
                pass 
            case 2:
                pass 