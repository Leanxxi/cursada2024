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

#    
# 'r' - reading mode. The default. It allows you only to read the file, not to modify it. 
# When using this mode the file must exist.
# 'w' - writing mode. It will create a new file if it does not exist, otherwise will erase 
# the file and allow you to write to it.
# 'a' - append mode. It will write data to the end of the file. It does not erase the file, 
# and the file must exist for this mode.
# 'rb' - reading mode in binary. This is similar to r except that the reading is forced in 
# binary mode. This is also a default choice.
# 'r+' - reading mode plus writing mode at the same time. This allows you to read and write 
# into files at the same time without having to use r and w.
# 'rb+' - reading and writing mode in binary. The same as r+ except the data is in binary
# 'wb' - writing mode in binary. The same as w except the data is in binary.
# 'w+' - writing and reading mode. The exact same as r+ but if the file does not exist, 
# a new one is made. Otherwise, the file is overwritten.
# 'wb+' - writing and reading mode in binary mode. The same as w+ but the data is in binary.
# 'ab' - appending in binary mode. Similar to a except that the data is in binary.
# 'a+' - appending and reading mode. Similar to w+ as it will create a new file if the file 
# does not exist. Otherwise, the file pointer is at the end of the file if it exists.
# 'ab+' - appending and reading mode in binary. The same as a+ except that the data is in 
# binary.
# """
