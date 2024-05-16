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
from funciones import (ingresar_entero)
import os

lista_dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
lista_ingresos = [0,0,0,0,0,0,0]


while True:
    print("""       Bienvenido al Menu
        1-Registrar ingresos
        2-Analizar datos
        3-Mostrar todos los datos
        4-salir

""")
    opcion = ingresar_entero('ingrese opcion')
    match opcion:   
        case 1:
            pass          
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass                  
        case 5:
            pass
        case 6:
            pass
        case 7:
            break
        case _:
            print("error: opcion inesperada")
    os.system("pause")
    os.system("cls")