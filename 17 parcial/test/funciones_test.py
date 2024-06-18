import os
import csv
import json
import datetime

# Funciones de validación


def validar_fecha_cronologicamente(fecha_inicial, fecha_final):
    fecha_inicial_lista = fecha_inicial.split('-')
    for elemento in fecha_inicial_lista:
        elemento = int(elemento)
    
    fecha_final_lista = fecha_final.split('-')
    for elemento in fecha_final_lista:
        elemento = int(elemento)
    
    todo_ok = True
    
    if(
        (fecha_final_lista[2] < fecha_inicial_lista[2]) or
        
        (fecha_final_lista[2] == fecha_inicial_lista[2] and
        fecha_final_lista[1] < fecha_inicial_lista[1]) or
        
        (fecha_final_lista[2] == fecha_inicial_lista[2] and 
         fecha_final_lista[1] == fecha_inicial_lista[1] and 
         fecha_inicial_lista[0] < fecha_inicial_lista[0]) 
        ):
        todo_ok = False
    
    return todo_ok



# Funciones de entrada de datos
def ingresar_flotante(mensaje : str)->float:
    """ingresa un caracter, intenta cambiarlo a un numero flotante, si tiene exito lo devuelve y rompe el bucle
    si no muestra un mensaje de error
    Returns:
        float: numero flotante ingresado
    """
    while True:  # Bucle para continuar solicitando hasta que se ingrese un flotante válido
        entrada = input(mensaje)
        try:
            # Intenta convertir la entrada a un número flotante
            numero = float(entrada)
            # Si tiene éxito, rompe el bucle y devuelve el número flotante
            return numero
        except ValueError:
            # Si falla la conversión, muestra un mensaje y continúa el bucle
            print("Error: El dato ingresado no es un número flotante. Inténtelo de nuevo.")

def ingresar_entero_limitado(mensaje : str,limite_menor = 0 ,limite_mayor = 99999):
    while True:
        numero_limitado = ingresar_entero(mensaje)
        if numero_limitado < limite_menor or numero_limitado > limite_mayor:
            print(f"""error: el numero se encuentra fuera de los limites, ingrese un numero entre
                   {limite_menor} y {limite_mayor}""")
        else:
            break
    return numero_limitado

def ingresar_entero(mensaje = "Ingrese un número entero: ") -> int:
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

def es_bisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def pedir_fecha(mensaje):
    while True:
        print(mensaje)
        anio = ingresar_entero_limitado("ingrese año", 1900 , 2999)
        anio_bisiesto = es_bisiesto(anio)
        mes = ingresar_entero_limitado("ingrese mes", 1,12)
        dia= ingresar_entero_limitado("ingrese día",1,31)
        
        if mes == 2 and dia <= 29 and anio_bisiesto == True:
            break
        elif dia <= 30 and mes == 4 or mes == 6 or mes == 9 or mes == 11:
            break
        elif dia <= 31 and mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            break
        else:
            print(f"Error: Fecha invalida, el día {dia}-{mes}-{anio} no existe")

    fecha = f"{dia}-{mes}-{anio}"   
    return fecha


# Funciones de gestión de proyectos

path_proyectos_csv = '17 parcial\Proyectos - Proyectos.csv'

def leer_proyectos(path : str):
    with open(path, 'r') as archivo:
        for linea in archivo.readlines():
            print(linea, "",end = "")



# Ejemplo de uso:


def ingresar_proyecto(path):
    #with open(path, 'a') as archivo:
        nuevo_proyecto = []
        nombre_de_proyecto = input('Ingrese Nombre de proyecto: ')
        descripcion = input('Ingrese descripcion del proyecto: ')
        presupuesto = ingresar_entero('ingrese presupuesto: ')
        inicio_del_proyecto = datetime.date.today()
        inicio_del_proyecto = inicio_del_proyecto.strftime("%d-%m-%Y")
        while True:
            fecha_fin_del_proyecto = pedir_fecha("escriba a continuacion la fecha final del proyecto")
            fecha_ok = validar_fecha_cronologicamente()
            if fecha_ok == False:
                print("la fecha final del proyecto no puede ser menor que la fecha inicial")
            else:
                break
        nuevo_proyecto.append(nombre_de_proyecto)
        nuevo_proyecto.append(descripcion)
        nuevo_proyecto.append(presupuesto)
        nuevo_proyecto.append(inicio_del_proyecto)
        nuevo_proyecto.append(fecha_fin_del_proyecto)
        return nuevo_proyecto

nuevo_proyecto = ingresar_proyecto(path_proyectos_csv)

print(nuevo_proyecto)

        
# Funciones de manejo de archivos

#funciones extras

