# El programa debe permitir al usuario ingresar los siguientes datos para 10 alumnos:
# ● Nombre
# ● Edad
# ● DNI
# ● Género (M para masculino, F para femenino, NB para No Binario)
# ● Nota
# Después de ingresar los datos de todos los alumnos, el programa debe calcular y
# mostrar la siguiente información:

# 1. Listado de todos los alumnos con un formato similar al siguiente:

# 2. El promedio de edades de los alumnos.
# 3. La cantidad de alumnos que promocionaron (nota mayor o igual a 6).
# 4. La cantidad de alumnos que aprobaron (nota mayor o igual a 4).
# 5. La cantidad de alumnos que desaprobaron (nota menor a 4).
# 6. El promedio de nota de los alumnos masculinos.
# 7. El porcentaje de alumnas que promocionaron sobre el total de alumnas.
import os

def ingresar_entero(mensaje="Ingrese un número entero: ") -> int:
    """
    Solicita al usuario que ingrese un número entero, lo valida y lo devuelve.

    Args:
        mensaje (str): El mensaje que se muestra al solicitar la entrada.

    Returns:
        int: El número entero ingresado por el usuario.
    """
    while True:
        entrada = input(mensaje)
        try:
            numero = int(entrada)
            print("Valor ingresado:", numero)
            return numero
        except ValueError:
            print("Error: La entrada no es un número entero válido. Inténtelo de nuevo.")

def ingresar_entero_positivo(mensaje = "ingrese entero positivo")->int:
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

def mostrar_lista(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(f"|| {lista[i][j]}", end= " ")
        print("")

def ingresar_alumno():
    alumno = []
    alumno.append(input("ingrese nombre del alumno"))
    alumno.append(ingresar_entero_positivo("ingrese edad del alumno"))
    alumno.append(ingresar_entero_positivo("ingrese DNI"))
    while True:
        genero = input("Ingrese Genero del Alumno").upper()
        if genero == "M" or genero == "F" or genero == "NB":
            alumno.append(genero)
            break
        else:
            print("Ingrese Genero del Alumno Correctamente 'M','F' o 'NB'")
    while True:
        nota = ingresar_entero("Ingrese la nota del alumno")
        if nota > 0 and nota < 10:
            alumno.append(nota)
            break
        else:
            print("error: La nota no puede ser menor a 0 o mayor que 10")
    return alumno

def calcular_promedio_lista_anidada(lista_anidada : list, columna : int)->float:
    if len(lista_anidada) > 0 and columna > 0 and columna > 0 or columna < len(lista_anidada[0]) :
        sumador = 0   
        
        for elemento in lista_anidada:
            if type(elemento[columna]) == int or type(elemento[columna]) == float:
                sumador += elemento[columna]
            else:
                print("error: no es un dato que se puede promediar")
        
        promedio = float(sumador) / len(lista_anidada)
        return promedio
    else:
        print("error general: parametros invalidos")

def separar_lista_segun_genero(lista_anidada, genero):
    lista_separada = []
    for elemento in lista_anidada:
        if elemento[3] == genero:
            lista_separada.append(elemento)
    return lista_separada

def calcular_cantidad_alumnos_con_nota_mayor_a(lista_de_alumnos, nota):
    cantidad_de_alumnos_con_nota_mayor_a = 0
    for alumno in lista_de_alumnos:
        if alumno[4] >= nota:
            cantidad_de_alumnos_con_nota_mayor_a += 1
    return cantidad_de_alumnos_con_nota_mayor_a

