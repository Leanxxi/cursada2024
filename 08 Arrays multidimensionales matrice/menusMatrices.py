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

from funcionesMatrices import *

def mostrar_menu():
    print("""bienvenido al menu
          1-ingresar 10 alumnos
          2-realizar calculos
          3-mostrar resultados
          4-salir

    """)

def menu_principal():
    lista_de_alumnos = []
    flag = False
    while True:
        mostrar_menu()
        opcion = ingresar_entero("Ingrese una opcion")
        match opcion:
            case 1:
                for i in range(10):
                    lista_de_alumnos.append(ingresar_alumno()) 
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