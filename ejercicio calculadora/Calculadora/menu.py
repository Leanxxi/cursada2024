import os
from funciones import *


def menu():
    bandera_primera_opcion = "no"
    bandera_segunda_opcion = "no"
    bandera_tercer_opcion = "no"
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        
        opcion = int(input("Su opcion: "))
        
        if opcion == 1:
            primer_operando = ingresar_entero()
            bandera_primera_opcion = "si" 
        elif opcion == 2:
            segundo_operando = ingresar_entero()
            bandera_segunda_opcion = "si" 
        elif opcion == 3:
            if bandera_primera_opcion == "si" and bandera_segunda_opcion == "si":
                suma = primer_operando + segundo_operando
                resta = primer_operando - segundo_operando
                division = primer_operando / segundo_operando
                multiplicacion = primer_operando * segundo_operando
                potencia = primer_operando ** segundo_operando
                resto = primer_operando % segundo_operando
                factorial = primer_operando
                bandera_tercer_opcion = "si"
            else:
                print("asegurese de que haya ingresado un valor en el primer y el segundo operando")
        elif opcion == 4:
            if bandera_tercer_opcion == "si":
                print(f"""A = {primer_operando} B = {segundo_operando}""")
                print(f"""A + B = {suma}\n A - B = {resta}\n A / B = {division}\n A * B = {multiplicacion}\n A ^ B = {potencia}\n A % B = {resto}\n
                        A! = {factorial}""")
            else:
                print("debe pasar primero por las opciones anteriories")
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")
        os.system("pause")
        os.system("cls")
    
    
menu()


