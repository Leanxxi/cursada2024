from funciones_test import *

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

proyecto = ingresar_proyecto(path_proyectos_csv)

todo_ok = validar_fecha_cronologicamente()

