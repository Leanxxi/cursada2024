import os
from funciones import *


def menu():
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        
        opcion = int(input("Su opcion: "))
        
        if opcion == 1:
            primer_operando = int(input("Ingreso Primer Operando"))
        elif opcion == 2:
            segundo_operando = int(input("Ingreso Segundo Operando"))
        elif opcion == 3:
            pass
            #if primer_operando ==  or segundo_operando:
        elif opcion == 4:
            print("Informo todos los resultados")
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")
            
        os.system('clear')
    
    
menu()
