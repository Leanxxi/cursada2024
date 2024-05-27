
from funciones_ABM import (ingresar_entero)

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