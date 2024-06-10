# 1) Crear una función que reciba como parámetro una cadena y determine la
# cantidad de vocales que hay de cada una (individualmente). La función
# retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2
# la cantidad.
# Por ej:
# cadena = “murcielaguito”
# “a” 1
# “e” 1
# “i” 2
# “o” 1
# “u” 2

cadena = "murcielaguito"

# def obtener_vocales(cadena : str):
#     matriz = [['a'],['e'],['i'],['o'],['u']]
#     contador_a = 0
#     contador_e = 0
#     contador_i = 0
#     contador_o = 0
#     contador_u = 0
#     for letra in cadena:
#         match letra:
#             case 'a':
#                 contador_a += 1
#             case 'e':
#                 contador_e += 1
#             case 'i':
#                 contador_i += 1
#             case 'o':
#                 contador_o += 1
#             case 'u':
#                 contador_u += 1
#     matriz[0].append(contador_a)
#     matriz[1].append(contador_e)
#     matriz[2].append(contador_i)
#     matriz[3].append(contador_o)
#     matriz[4].append(contador_u)
#     return matriz
 
# matriz = obtener_vocales(cadena)
# print(matriz)



# 2) Crear una función que reciba una cadena y un caracter. La función deberá
# devolver el índice en el que se encuentre la primera incidencia de dicho
# caracter, o -1 en caso de que no esté.

# def obtener_vocal(cadena, caracter):
#     indice = -1
#     for i in range(len(cadena)):
#         if cadena[i] == caracter:
#             indice = i
#             break
    
#     return indice


# letra = obtener_vocal("hola", 'u')    
# print(letra)    

# 3) Crear una función que reciba como parámetro una cadena y determine si la
# misma es o no un palíndromo. Deberá retornar un valor booleano indicando
# lo sucedido.

# def definir_palindromo(cadena):
#     for i in range(len(cadena)):
#         if cadena[i] == cadena[-1-i]:
#             palindromo = True
#         else:
#             palindromo = False
#     return palindromo



# palindromo = definir_palindromo("neuquen")
# print(palindromo)


# 4) Crear una función que reciba como parámetro una cadena y suprima los
# caracteres repetidos.
# Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.
def suprimir_caracteres_repetidos(cadena):
    nueva_cadena = []
    caracteres_repetidos = []
    for i in range(len(cadena)):
        if cadena[i] not in caracteres_repetidos:
            caracteres_repetidos.append(cadena[i])
            nueva_cadena.append(cadena[i])

    nueva_cadena = "".join(nueva_cadena)
    
    return nueva_cadena

    

nueva_cadena = suprimir_caracteres_repetidos(cadena)

print(nueva_cadena)

# 5) Crear una función que reciba una cadena por parámetro y suprima las
# vocales de la misma.
# Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.

def suprimir_vocales(cadena):
    letras_a_suprimir = ['a','e','i','o','u']
    nueva_cadena = []
    for i in range(len(cadena)):
        if cadena[i] not in letras_a_suprimir:
            nueva_cadena.append(cadena[i])

    nueva_cadena = "".join(nueva_cadena)
    
    return nueva_cadena

nueva_cadena_sin_vocales = suprimir_vocales(cadena)
print(nueva_cadena_sin_vocales)
# 6) Crear una función para contar cuántas veces aparece una subcadena dentro
# de una cadena.
# Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá
# retornar el valor 2.

cadena = "el panadero con el pan"
subcadena = "pan"

def contar_subcadena(cadena, subcadena):
    contador_subcadena = 0
    coincidencias = []
    if subcadena in cadena and len(subcadena) < len(cadena):
        for i in range(len(cadena)):
            if subcadena[i] == cadena[i:i+len(subcadena)]:
                contador_subcadena += 1
                    
    return contador_subcadena

subcadenas = contar_subcadena(cadena, subcadena)

print(f"{subcadenas}")
# CASO INVESTIGACIÓN CRIMINAL: CSI UTN


# Se ha encontrado una muestra de ADN en el lugar del crimen que
# contiene la siguiente secuencia de bases nitrogenadas:
# “CGTTTAATG”. La investigación ha revelado tres posibles
# sospechosos, cada uno con su propia muestra de ADN:
# ● Juan Pérez
# Muestra de ADN: "CGGGGCTAAAATTTTTTACGATCG"
# ● María Rodríguez
# Muestra de ADN: "AACGTTTAATGTTCTAAGCTGCG"
# ● Carlos Sánchez
# Muestra de ADN: "CGGGGCTAAAATTTTTTACGATCG"

# Para resolver el caso, nos piden que desarrollemos un programa
# que compare las combinaciones de bases nitrogenadas de la
# muestra encontrada con las muestras de los sospechosos.
# Mostrar el nombre por pantalla en caso de encontrar al asesino, o
# la leyenda “SON TODOS INOCENTES”.

