import os
import csv
import json
import datetime


path_proyectos_csv = '17 parcial\Proyectos - Proyectos.csv'

#funciones de ingresos
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

#funciones de fecha
    #validaciones de fecha
def validar_fecha_cronologicamente(fecha_inicial, fecha_final):
    """

    Args:
        fecha_inicial (_type_): _description_
        fecha_final (_type_): _description_

    Returns:
        _type_: _description_
    """
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
    #ingreso de fechas
def pedir_fecha(mensaje = "")->str:
    """Pide una fecha y valida si esta misma existe y la devuelve en formato String

    Args:
        mensaje (str, optional): string para ingresar un mensaje. Defaults to "".

    Returns:
        str: devuelve la fecha en formato string
    """
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

def leer_proyectos(path : str):
    with open(path, 'r') as archivo:
        for linea in archivo.readlines():
            print(linea, "",end = "")

def generar_id(path : str):
    """genera un id distinto de los ya que ya existen en el path

    Args:
        path (str): ubicacion del archivo a leer
    """
    with open(path, 'r') as archivo:
       lineas = archivo.readlines()
       ultima_linea = len(lineas)
    return(ultima_linea)
#funciones de ingresos
def ingresar_proyecto(path: str):
    """ingresa un nuevo proyecto al archivo de proyectos

    Args:
        path (str): ubicacion del archivo
    """
    nuevo_proyecto = []
    nuevo_id = generar_id(path)
    nuevo_id = str(nuevo_id)
    nombre_de_proyecto = input('Ingrese Nombre de proyecto: ')
    descripcion = input('Ingrese descripcion del proyecto: ')
    presupuesto = ingresar_entero('ingrese presupuesto: ')
    inicio_del_proyecto = datetime.date.today()
    inicio_del_proyecto = inicio_del_proyecto.strftime("%d-%m-%Y")
    while True:
        fecha_fin_del_proyecto = pedir_fecha("escriba a continuacion la fecha final del proyecto")
        fecha_ok = validar_fecha_cronologicamente(inicio_del_proyecto, fecha_fin_del_proyecto)
        if fecha_ok == False:
            print("la fecha final del proyecto no puede ser menor que la fecha inicial")
        else:
            break
    nuevo_proyecto.append(nuevo_id)
    nuevo_proyecto.append(nombre_de_proyecto)
    nuevo_proyecto.append(descripcion)
    presupuesto = str(presupuesto) 
    nuevo_proyecto.append(inicio_del_proyecto)
    nuevo_proyecto.append(fecha_fin_del_proyecto)
    nuevo_proyecto.append(presupuesto)
    nuevo_proyecto.append('Activo')
    
    separador = ','
    nueva_cadena = separador.join((nuevo_proyecto))
    print(nueva_cadena)

    with open(path, 'a') as archivo:
        archivo.write('\n' + nueva_cadena)

#funciones para manejo de csv
def transformar_linea_a_lista(path, linea_a_tranformar):
    """crea una lista de la linea deseada separada por cada ','

    Args:
        path (_type_): _description_
        linea_a_tranformar (_type_): _description_

    Returns:
        _type_: _description_
    """
    with open(path, 'r') as archivo:
        contador_linea_leida = 0

        for linea in archivo.readlines():
            contador_linea_leida += 1
            if linea_a_tranformar == contador_linea_leida:
                linea_archivo = linea.strip('\n')
                lista = linea_archivo.split(',')
            
    return lista

def contar_lineas(path):
    with open(path, 'r') as archivo:
        contador_linea_leida = 0

        for linea in archivo.readlines():
            contador_linea_leida += 1
    return contador_linea_leida


def normalizar_datos(lista: list):
    for elemento in lista:
        elemento['id'] = int(elemento['id'])
        elemento['Presupuesto'] = int(elemento['Presupuesto'])        

def encontrar_proyecto(lista):

    ingreso_id = ingresar_entero_positivo("ingrese id para modificar el proyecto")
    todo_ok = False
    for proyecto in lista:
        if proyecto['id'] == ingreso_id:
            todo_ok = True
            devuelvo = proyecto
            break
    if todo_ok == False:
        print('no se encontró proyecto')
        devuelvo = todo_ok
    return devuelvo
        

def pasar_csv_a_lista_diccionarios(path):
    keys = ['id','Nombre del Proyecto','Descripcion','Fecha de inicio','Fecha de Fin','Presupuesto','Estado']
    lista = []
    lista_csv = []
    diccionario = {}
    lista_de_diccionarios = []
    with open(path, 'r+') as proyectos:
        for proyecto in proyectos:
            lista = transformar_linea_a_lista(path,proyecto)
            lista_csv.append(lista)
        # print(lista_csv)
        # for i in range(len(lista_csv)):
        #     for j in range(len(lista_csv[i])):
        #         diccionario[keys[j]] = lista_csv[i][j]
        #     lista_de_diccionarios.append(diccionario)     
        # print(lista_de_diccionarios)
        
    
lista = pasar_csv_a_lista_diccionarios(path_proyectos_csv)



# def mostrar_lista(lista):
#     for elemento in lista:
#         print(elemento)


# def modificar_nombre(id,lista):
#     for elemento in lista:
#         elemento['id'] = input("Modifique el nombre del proyecto: ")





