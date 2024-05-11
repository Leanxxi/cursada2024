# 1. Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el
# promedio de todos los números.
# 2. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el
# promedio de los números positivos.
# 3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista
# que recibe como parámetro.
# 4. Escribir una función que reciba como parámetros una lista de enteros y retorne la posición
# del valor máximo encontrado.
# 5. Escribir una función que reciba como parámetros una lista de enteros y muestre la/las
# posiciones en donde se encuentra el valor máximo hallado.
# 6. Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista
# de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe
# reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente
# reemplazo y luego retornar la cantidad total de reemplazos realizados.

from funcionesArrays import *
import os


lista_de_nombres = ["Javier", "Luis", "Jose", "Ramiro", "Guillermo", "Javier"]
lista_creada = crear_lista_de_numeros()

while True:
    print("""Bienvenido al Menu
          1-calcular promedio de la lista
          2-calcular promedio de los positivos de la lista
          3-calcular producto de todos los elementos de la lista
          4-retornar la posicion del valor maximo de la lista
          5-encontrar la posicion del valor maximo de la lista
          6-reemplazar nombre de una lista y retornar la cantidad total de reemplazos realizados.
          7-salir

""")

    opcion = ingresar_entero('ingrese opcion')

    match opcion:   
        case 1:
            #1. Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el
            # promedio de todos los números.
            print(f"promedio = {calcular_el_promedio_de_listas(lista_creada)}")            
        case 2:
            # 2. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el
            # promedio de los números positivos.
            print(f"promedio positivos = {calcular_promedio_positivos(lista_creada)}")
        case 3:
            # 3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista
            # que recibe como parámetro.
            print(f"producto = {calcular_producto_de_todos_los_elementos_de_la_lista(lista_creada)}")
        case 4:
            # 4. Escribir una función que reciba como parámetros una lista de enteros y retorne la posición
            # del valor máximo encontrado.  
            print(f"posicion = {encontrar_max_min_posc_lista(lista_creada,'posicion_maximo')}")
        case 5:
            # 5. Escribir una función que reciba como parámetros una lista de enteros y muestre la/las
            # posiciones en donde se encuentra el valor máximo hallado.
            print(f"posicion de los valores maximos = {encontrar_pos_maximos(lista_creada)}")
        case 6:
            #6. Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista
            # de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe
            # reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente
            # reemplazo y luego retornar la cantidad total de reemplazos realizados.

            print(f"promedio positivos = {calcular_promedio_positivos(lista_creada)}")
        case 7:
            break
        case _:
            print("error: opcion inesperada")
    os.system("pause")
    os.system("cls")