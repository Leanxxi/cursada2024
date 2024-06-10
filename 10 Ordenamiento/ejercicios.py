# Listas simples:
# 1- Realizar una función que ordene una lista de entero en orden ascendente o
# descendente dependiendo de un parámetro que se le envíe, la función debe retornar
# la cantidad de cambios que se realizaron.
# 2- Realizar una función que ordene una lista de nombres de la A-Z o viceversa
# dependiendo de un parámetro que se le envíe, la función debe retornar la cantidad
# de cambios que se realizaron.
# 3- Similar a la función anterior, se debe realizar otra que ordene una lista de
# nombres por su largo, de manera ascendente o descendente, la función debe
# retornar la cantidad de cambios que se realizaron
# Matrices:
# 4- Ordenar una matriz de nombre-apellido de la A-Z o viceversa dependiendo de un
# parámetro que se le envíe, por otro lado, la función deberá recibir otro parámetro
# para indicar si la prioridad de ordenamiento la tendrá el nombre o el apellido.

lista_de_enteros = [3,6,4,2,7,8,4,6,1,2,6,9,7,6,4,2,23,4,1,2,4,6,7,81]
lista_de_nombres = ['Javier', 'Jorge', 'Ramon', 'Oliver', 'Zulma', 'Monica','Alberto','Mickey']
lista_de_nombres_completos = [
    ["Juan", "Pérez"],
    ["Ana", "García"],
    ["Luis", "Martínez"],
    ["María", "Sánchez"],
    ["Carlos", "López"],
    ["Elena", "Gómez"],
    ["Pablo", "Rodríguez"],
    ["Lucía", "Fernández"],
    ["Miguel", "González"],
    ["Sara", "Hernández"]
]

def ordenar(lista, parametro = "mayor"):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] < lista[j] and parametro == "mayor" or lista[i] > lista[j] and parametro == "menor":
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def ordenar_por_tamanio_string(lista, parametro = "mayor"):
     for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if(
                len(lista[i]) < len(lista[j]) and parametro == "mayor" or
                len(lista[i]) > len(lista[j]) and parametro == "menor"
            ):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


#ejercicio 1
ordenar(lista_de_enteros, "menor")
lista_de_enteros

#ejercicio 2
#alfabeticamente
ordenar(lista_de_nombres, "menor")

print(lista_de_nombres)

#al reves del alfabeto
ordenar(lista_de_nombres, "mayor")

print(lista_de_nombres)
#ejercicio 3
ordenar_por_tamanio_string(lista_de_nombres, "mayor")

print(lista_de_nombres)

#  Matrices:
# 4- Ordenar una matriz de nombre-apellido de la A-Z o viceversa dependiendo de un
# parámetro que se le envíe, por otro lado, la función deberá recibir otro parámetro
# para indicar si la prioridad de ordenamiento la tendrá el nombre o el apellido.


def ordenar_matriz_nombre_apellido(lista, parametro = "mayor", prioridad = 1):
    """

    Args:
        lista (_type_): _description_
        parametro (str, optional): _description_. Defaults to "mayor".
        prioridad (int, optional): _description_. Defaults to 1.
    """
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if(
            lista[i][prioridad] < lista[j][prioridad] and parametro == "mayor" 
            or lista[i][prioridad] > lista[j][prioridad] and parametro == "menor"
            ):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def mostrar_lista(lista: list):
    """_summary_

    Args:
        lista (list): _description_
    """
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(f"|| {lista[i][j]}", end= " ")
        print("")

ordenar_matriz_nombre_apellido(lista_de_nombres_completos)

mostrar_lista(lista_de_nombres_completos)
