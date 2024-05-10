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




lista_creada = crear_lista_de_numeros()




print(f"promedio positivos = {calcular_promedio_positivos(lista_creada)}")

while True:
    opcion = input("ingrese opcion")

    match opcion:   
        case 1:
            #1. Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el
            # promedio de todos los números.
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