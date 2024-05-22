#modulo de menus

from funciones import *

def mostrar_menu_principal():
    """muestra las opciones que se pueden elegir del programa principal
     Args:
        No recibe argumentos.

    Returns:
        No devuelve ningún valor.
    """
    print("""       Bienvenido al Menu
            1-Registrar ingresos
            2-Analizar datos
            3-Mostrar todos los datos
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
                sub_menu_ingresos()     
            case 2:
                #determinar día con más ingresos
                dia_con_mas_ingresos = encontrar_max_min_posc_lista(lista_ingresos, "posicion_maximo" )
                dia_con_menos_ingresos = encontrar_max_min_posc_lista(lista_ingresos,"posicion_minimo" )
                promedio_ingresos = calcular_el_promedio_de_listas(lista_ingresos)
                suma_ingresos = calcular_suma_de_lista(lista_ingresos)
                lista_dia_habil = limitar_rango_de_lista(lista_ingresos,5)
                promedio_dia_habil = calcular_el_promedio_de_listas(lista_dia_habil)
                promedio_finde = calcular_el_promedio_de_listas(lista_ingresos,7,5)
                bandera_de_calculos = True
            case 3:
                if bandera_de_calculos:
                    print(f"el día con mas ingresos es {lista_dias[dia_con_mas_ingresos]}")
                    print(f"el día con menos ingresos es {lista_dias[dia_con_menos_ingresos]}")
                    print(f"promedio de los ingresos{promedio_ingresos}")
                    print(f"la totalidad de los ingresos es:{suma_ingresos}")
                    print(f"promedio dia de semana:{promedio_dia_habil}")
                    print(f"promedio fin de semana:{promedio_finde}")
                    
                else:
                    print("Error: no ha analizado los datos de la opcion 2")
            case 4:
                break
            case _:
                print("error: opcion inesperada")
        os.system("pause")
        os.system("cls")

def mostrar_submenu_ingresos():
    """submenu de los ingresos de la opcion
     Args:
        No recibe argumentos.

    Returns:
        No devuelve ningún valor."""
    print("""
----------------Menu de registros de ingresos----------------
        1-Registrar Lunes
        2-Registrar Martes
        3-Registrar Miercoles
        4-Registrar Jueves
        5-Registrar Viernes
        6-Registrar Sabados
        7-Registrar Domingos
        8-Volver al menu principal  

""")

def sub_menu_ingresos():
    """registra cada opcion para guardar una variable en la lista de la semana
     Args:
        No recibe argumentos.

    Returns:
        No devuelve ningún valor.
    """
    while True:
        mostrar_submenu_ingresos()
        opcion = input("Ingrese Opcion")

        match opcion:
            case '1':
                registros_semanales(lista_ingresos, 0,lista_dias)
                #lunes
            case '2':
                registros_semanales(lista_ingresos, 1,lista_dias)
                #martes
            case '3':
                registros_semanales(lista_ingresos, 2,lista_dias)
                #miercoles
            case '4':
                registros_semanales(lista_ingresos, 3,lista_dias)
                #jueves
            case '5':
                registros_semanales(lista_ingresos, 4,lista_dias)
                #viernes
            case '6':
                registros_semanales(lista_ingresos, 5,lista_dias)
                #sabado
            case '7':
                registros_semanales(lista_ingresos, 6,lista_dias)
                #domingo
            case '8':
                #salir
                break
            case _:
                print("Error opcion no valida")
        os.system("pause")
        os.system("cls")
