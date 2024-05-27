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
import os
from datos import (lista_dias,lista_ingresos)

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


def ingresar_flotante(mensaje : str)->float:
    """ingresa un caracter, intenta cambiarlo a un numero flotante, si tiene exito lo devuelve y rompe el bucle
    si no muestra un mensaje de error
    Returns:
        float: numero flotante ingresado
    """
    while True:  # Bucle para continuar solicitando hasta que se ingrese un flotante válido
        entrada = input(mensaje)
        try:
            # Intenta convertir la entrada a un número flotante
            numero = float(entrada)
            # Si tiene éxito, rompe el bucle y devuelve el número flotante
            return numero
        except ValueError:
            # Si falla la conversión, muestra un mensaje y continúa el bucle
            print("Error: El dato ingresado no es un número flotante. Inténtelo de nuevo.")

def registros_semanales(lista_ingresos : list, i : int, lista_dias : list):
    """modifica el valor ingresado segun el día correspondiente

    Args:
        lista_ingresos (list): lista de los ingresos por dia
        i (int): valor correspondiente a cada día de la semana
        lista_dias (list): lista con los nombres de los días
    """    
    lista_ingresos[i] = ingresar_flotante(f"ingrese su monto para el día {lista_dias[i]}")


def encontrar_max_min_posc_lista(lista_de_numeros : list, maximo_minimo_posicion = "maximo")-> float |int:
    """
    Ecuentra el maximo, el minimo o la posicion de los mismos segun el parametro
    Args:
        lista_de_numeros (list):lista de numeros
        
        maximo_minimo_posicion (str, optional): "maximo" = devuelve el valor maximo en la lista. el argumento por defecto es "maximo".
            Returns:
                float: valor maximo 
        
        maximo_minimo_posicion (str, optional):"minimo" devuelve el valor minimo de la lista
            Returns:
                float: valor minimo        
        maximo_minimo_posicion (str, optional):"posicion_minimo": devuelve la posicion del valor minimo en la lista. 
            Returns:
                int: posicion del valor minimo
        
        maximo_minimo_posicion (str, optional):"posicion_maximo": devuelve la posicion del valor maximo en la lista 
            Returns:
                int: posicion del valor maximo 
                  """
    for i in range(len(lista_de_numeros)):
        if i == 0:
            maximo = lista_de_numeros[i]
            minimo = lista_de_numeros[i]
            posicion_maximo = 0
            posicion_minimo = 0
        elif lista_de_numeros[i] > maximo:
            maximo = lista_de_numeros[i]
            posicion_maximo = i
        elif lista_de_numeros[i] < minimo:
            posicion_minimo = i
            minimo = lista_de_numeros[i]

    if maximo_minimo_posicion == "maximo":
        devuelvo = maximo
    elif maximo_minimo_posicion == "minimo":
        devuelvo = minimo
    elif maximo_minimo_posicion == "posicion_maximo":
        devuelvo = posicion_maximo
    elif maximo_minimo_posicion == "posicion_minimo":
        devuelvo = posicion_minimo
    else:
        print("error: argumento invalido")
    
    return devuelvo
 

def calcular_el_promedio_de_listas(lista_de_numeros : list)->float :
    """calcula el promedio de la lista de numeros argumentada
    Args:
        lista (list): lista de numeros
    Returns:
        float: promedio de la lista de numeros
    """
    suma_de_lista = 0
    for i in range(len(lista_de_numeros)):
        suma_de_lista += lista_de_numeros[i]
    
    promedio = suma_de_lista / len(lista_de_numeros)
    return promedio

def calcular_suma_de_lista(lista_de_numeros : list)-> int | float :
    """
    suma todos los valores de la lista y los devuelve

    Args:
        lista_de_numeros (list): lista de numeros sumables

    Returns:
        int | float: suma total de cada valor de la lista
    """
    suma_de_lista = 0
    for i in range(len(lista_de_numeros)):
        if lista_de_numeros[i] > 0:
            suma_de_lista += lista_de_numeros[i]
    
    return suma_de_lista

def limitar_rango_de_lista(lista_completa : list, limite_superior : int, limite_inferior = 0 )->list:
    """_summary_

    Args:
        lista_completa (list): _description_
        limite_superior (int): _description_
        limite_inferior (int, optional): _description_. Defaults to 0.

    Returns:
        list: _description_
    """
    lista_cortada = []
    for i in range(len(lista_completa)):
        if i <= limite_superior or i >= limite_inferior:
            lista_cortada.append(lista_completa[i])
    
    return lista_cortada

def calcular_variacion_valor_anterior(lista_de_numeros,lista_dias):
    lista_de_variaciones = []
    for i in range(len(lista_de_numeros)):
        if i > 0:
            variacion = lista_de_numeros[i] - lista_de_numeros[i-1]
            print(f"{lista_dias[i-1]} - {lista_dias[i]} = {variacion}")
            lista_de_variaciones.append(variacion)
    return lista_de_variaciones

