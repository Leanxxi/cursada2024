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

#---------------------------------------------------------------
#ejercicio 1


lista_creada = crear_lista_de_numeros()

#print(f"promedio de numeros{calcular_el_promedio_de_listas(lista_creada)}")
#----------------------------------------------------------------
#ejercio 2
#Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el
#promedio de los números positivos.

def calcular_promedio_positivos(lista : list):
    suma_de_lista = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            suma_de_lista += lista[i]
    
    promedio = suma_de_lista / len(lista)
    return promedio

print(f"promedio positivos = {calcular_promedio_positivos(lista_creada)}")

