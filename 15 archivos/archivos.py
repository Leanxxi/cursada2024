# 1. Crear una función que reciba como parámetros una lista de
# números y el path de un archivo. La misma deberá guardar la lista
# en un archivo de texto.
# 2. Crear una función que reciba como parámetro el path de un
# archivo. La misma deberá leer el archivo del ejercicio anterior, solo
# dejando pasar a la lista los números múltiplos de 2.
# 3. Crear una función que reciba como parámetros dos paths: uno
# correspondiente a un archivo de origen y otro correspondiente a
# un archivo de destino. La función debe leer el contenido del
# archivo de origen y luego transcribirlo en el archivo de destino. En
# caso de error la función retornará algún tipo de código de error
# indicando que paso.
# 4. Crear una función llamada contar_elementos que recibe como
# parámetro el path de un archivo de texto que contiene un poema.
# La función deberá contar la cantidad de líneas, la cantidad de
# palabras y la cantidad de caracteres que contiene el poema. La
# función retornará un diccionario con los datos obtenidos.
import os
import csv
import json


# file = open('15 archivos./data1.txt', 'w')
# print(file)
# file.close()

# with open('15 archivos./data1.txt', 'r') as archivo:
#     lineas = archivo.readlines()
#     #print(lineas)

# # print(lineas)
# for l in lineas:
#     print(l.replace('\n', ''))

# with open('15 archivos./data1.txt', 'r') as archivo:
#     contenido = archivo.read()
#     lineas = contenido.split('\n')
#     print(lineas)

# with open('15 archivos./data1.txt', 'r') as archivo:
#     contenido = archivo.read()
#     pos = archivo.tell()
#     print(pos)
#     print(f'el archivo tiene {pos} caracteres de longitud')


with open('15 archivos./data1.txt', 'r') as archivo:
    archivo.seek(7)
    pos = archivo.tell()
    print(pos)
    contenido = archivo.read()
    lineas = contenido.split('\n')
    print(lineas)