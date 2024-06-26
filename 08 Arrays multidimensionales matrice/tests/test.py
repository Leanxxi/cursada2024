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
# 7. El porcentaje de alumnas que promocionaron sobre el total de alumnas
from datos_test import lista_de_alumnos
import os

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

def mostrar_lista(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(f"|| {lista[i][j]}", end= " ")
        print("")

def ingresar_alumnos():
    lista_de_alumnos = []

    for i in range(10):
        lista_de_alumnos[i][0] = input("ingrese nombre del alumno")
        lista_de_alumnos[i][1] = input("Ingrese Apellido del alumno")
        lista_de_alumnos[i][2] = ingresar_entero("ingrese edad del alumno")
        lista_de_alumnos[i][3] = ingresar_entero("ingrese DNI")
        lista_de_alumnos[i][4] = input("Ingrese Genero del Alumno")
        while True:
            lista_de_alumnos[i][4] = ingresar_entero("Ingrese la nota del alumno")
            if lista_de_alumnos[i][4] < 0 or lista_de_alumnos[i][4] > 10:
                print("error: La nota no puede ser menor a 0 o mayor que 10")
            else:
                break
    return lista_de_alumnos

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


def mostrar_menu():
    print("""bienvenido al menu
          1-ingresar 10 alumnos
          2-realizar calculos
          3-mostrar resultados
          4-salir

    """)

def menu_principal(lista_de_alumnos):
    flag = False
    while True:
        mostrar_menu()
        opcion = ingresar_entero("Ingrese una opcion")
        match opcion:
            case 1:
                lista_de_alumnos = ingresar_alumnos()
            case 2:
                    if len(lista_de_alumnos) > 0: 
                        promedio_edades = calcular_promedio_lista_anidada(lista_de_alumnos, 4)
                        alumnos_promocionados = calcular_cantidad_alumnos_con_nota_mayor_a(lista_de_alumnos , 6)
                        alumnos_aprobados = calcular_cantidad_alumnos_con_nota_mayor_a(lista_de_alumnos, 4)
                        alumnos_desaprobados = len(lista_de_alumnos) - alumnos_aprobados
                        alumnos_masculinos = separar_lista_segun_genero(lista_de_alumnos, "M")
                        promedio_masculinos = calcular_promedio_lista_anidada(alumnos_masculinos,4)
                        alumnas = separar_lista_segun_genero(lista_de_alumnos, "F")
                        alumnas_promocionadas = calcular_cantidad_alumnos_con_nota_mayor_a(alumnas, 6)
                        porcentaje_alumnas_promocionadas = 100 / len(alumnas) *  alumnas_promocionadas
                        flag = True
                    else:
                        print("la lista no puede estar vacia")
            case 3:
                if flag:
                    mostrar_lista(lista_de_alumnos)
                    print(
f"""
promedio de edades de los alumnos: {promedio_edades}
la cantidad de alumnos promocionados es: {alumnos_promocionados}
la cantidad de alumnos aprobados es : {alumnos_aprobados}
la cantidad de alumnos desaprobados es: {alumnos_desaprobados}
el promedio de nota de los alumnos masculinos es : {promedio_masculinos}
el porcentaje de alumnas promocionadas es : {porcentaje_alumnas_promocionadas}%
""")
                else:
                    print("debe realizar los calculos primero")
            case 4:
                break
        os.system("pause")
        os.system("cls")


menu_principal(lista_de_alumnos)

    









        

