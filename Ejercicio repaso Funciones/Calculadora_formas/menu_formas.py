#Leandro Robles A311

import os
from funciones import *


bandera_primer_lado = False
bandera_segundo_lado = False
bandera_calculos_triangulo = False
bandera_calculos_rectangulo = False
bandera_calculos_cuadrado = False
while(True):
    print("""---------------menu-----------------\n1: ingresar primer lado\n2: ingresar segundo lado\n3: calcular datos del triangulo\n4: calcular datos del rectangulo\n5: calcular datos del cuadrado\n6: imprimir datos guardados\n7: borrar datos guardados\n8: salir""")
    opcion = ingresar_entero('ingrese opcion....')
    match opcion:
        case 1:
            primer_lado = ingresar_flotante()
            bandera_primer_lado = True
        case 2:
            segundo_lado = ingresar_flotante()
            bandera_segundo_lado = True
        case 3:
            #"Calcular datos del triangulo rectangulo (Hipotenusa y angulos, area, perimetro)")
            if (bandera_primer_lado == True and bandera_segundo_lado == True):
                hipotenusa = calcular_hipotenusa(primer_lado , segundo_lado)
                angulo_alpha = calcular_angulo_alpha(primer_lado , segundo_lado)
                angulo_beta = calcular_angulo_beta(primer_lado , segundo_lado)
                area_triangulo_equilatero = calcular_area_triangulo_equilatero(primer_lado , segundo_lado)
                perimetro_triangulo = calcular_perimetro_triangulo(primer_lado , segundo_lado, hipotenusa)
                bandera_calculos_triangulo = True
            else:
                print("debe ingresar los datos del primer y segundo lado")
        case 4:    
            #"Calcular datos rectangulo (Diagonal, area, perimetro, relacion de aspecto)")
            if bandera_primer_lado == True and bandera_segundo_lado == True:
                diagonal_rectangulo = calcular_hipotenusa(primer_lado, segundo_lado)
                area_rectangulo = calcular_area_rectangulo(primer_lado, segundo_lado)
                perimetro_rectangulo = calcular_perimetro_rectangulo(primer_lado, segundo_lado)
                relacion_de_aspecto = calcular_relacion_de_aspecto(primer_lado, segundo_lado)
                bandera_calculos_rectangulo = True
            else:
                print("debe ingresar los datos del primer y segundo lado")
        case 5:
            #"Calcular datos cuadrado (Diagonal, area, perimetro)"
            if bandera_primer_lado == True and bandera_segundo_lado == True: 
                diagonal_cuadrado = calcular_diagonal_cuadrado(primer_lado)
                perimetro_cuadrado = calcular_perimetro_cuadrado(primer_lado)
                area_cuadrado = calcular_area_rectangulo(primer_lado, primer_lado)
                bandera_calculos_cuadrado = True
            else:
                print("debe ingresar los datos del primer y segundo lado")
        case 6: #ver datos guardados
            if bandera_calculos_triangulo == True:
                print(f"""Datos Triangulo: \nhipotenusa: {hipotenusa}\nangulos: Alpha = {angulo_alpha} Beta = {angulo_beta}\narea = {area_triangulo_equilatero}\nperimetro = {perimetro_triangulo}""")
            else:
                print("sin datos del triangulo")
            if bandera_calculos_rectangulo == True:
                print(f"""Datos Rectangulo:\nDiagonal: {diagonal_rectangulo}\narea: {area_rectangulo}\nperimetro: {perimetro_rectangulo}\nrelacion de aspecto: {relacion_de_aspecto}""")
            else:
                print("sin datos del rectangulo")
            if bandera_calculos_cuadrado == True:
                print(f"""Datos Cuadrado:\n Diagonal: {diagonal_cuadrado}\n area:{area_cuadrado}\nperimetro:{perimetro_cuadrado}""")
            else:
                print("sin datos del cuadrado")
        case 7:
            if bandera_calculos_cuadrado == True or bandera_calculos_triangulo == True or bandera_calculos_triangulo == True:
                print("Borrando datos guardados")
                bandera_primer_lado = False
                bandera_segundo_lado = False
                bandera_calculos_triangulo = False
                bandera_calculos_rectangulo = False
                bandera_calculos_cuadrado = False
                primer_lado = None
                segundo_lado = None
            else:
                print("no hay datos para borrar...")

        case 8:
            break
        case _:
            print("opcion invalida")
    os.system("pause")
    os.system("cls")