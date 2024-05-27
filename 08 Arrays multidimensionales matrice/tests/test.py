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
            print(f"|| {lista[i][j]}")

lista_anidada = []

for i in range(10):
    lista_anidada[i][0] = input("ingrese nombre del alumno")
    lista_anidada[i][1] = input("Ingrese Apellido del alumno")
    lista_anidada[i][2] = ingresar_entero("ingrese DNI")
    lista_anidada[i][3] = input("Ingrese Genero del Alumno")
    while True:
        lista_anidada[i][4] = ingresar_entero("Ingrese la nota del alumno")
        if lista_anidada[i][4] < 0 or lista_anidada[i][4] > 10:
            print("error: La nota no puede ser menor a 0 o mayor que 10")
        else:
            break



        

