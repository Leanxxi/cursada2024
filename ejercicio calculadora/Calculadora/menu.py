import os
from funciones import *


def menu():
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        
        opcion = int(input("Su opcion: "))
        
        if opcion == 1:
            primer_operando = ingresar_entero()
        elif opcion == 2:
            segundo_operando = ingresar_entero()
        elif opcion == 3:
            pass
            suma = primer_operando + segundo_operando
            resta = primer_operando - segundo_operando
            division = primer_operando / segundo_operando
            multiplicacion = primer_operando * segundo_operando
            potencia = primer_operando ** segundo_operando
            resto = primer_operando % segundo_operando
            factorial = primer_operando
        elif opcion == 4:
            print("Informo todos los resultados")
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")
            
        os.system('clear')
    
    
menu()


