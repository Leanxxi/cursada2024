import os
from funciones import *


def menu():
    bandera_primera_opcion = False
    bandera_segunda_opcion = False
    bandera_tercer_opcion = False
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        
        opcion = int(input("Su opcion: "))
        
        if opcion == 1:
            primer_operando = ingresar_entero()
            bandera_primera_opcion = True
        elif opcion == 2:
            segundo_operando = ingresar_entero()
            bandera_segunda_opcion = True 
        elif opcion == 3:
            if bandera_primera_opcion == True and bandera_segunda_opcion == True:
                suma = primer_operando + segundo_operando
                resta = primer_operando - segundo_operando                
                multiplicacion = primer_operando * segundo_operando
                potencia = primer_operando ** segundo_operando
                if segundo_operando != 0:
                    resto = primer_operando % segundo_operando
                    division = primer_operando / segundo_operando
                else:
                    mensaje = "no se puede dividir por 0"
                    resto = mensaje
                    division = mensaje
                factorial = primer_operando
                bandera_tercer_opcion = True
            else:
                print("asegurese de que haya ingresado un valor en el primer y el segundo operando")
        elif opcion == 4:
            if bandera_tercer_opcion == True:
                print(f""" A = {primer_operando} B = {segundo_operando}""")
                print(f""" A + B = {suma}\n A - B = {resta}\n A / B = {division}\n A * B = {multiplicacion}\n A ^ B = {potencia}\n A % B = {resto}\n A! = {factorial}""")
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


