from math import (sin, cos , sqrt, asin, tan, atan)

def ingresar_flotante():
    while True:  # Bucle para continuar solicitando hasta que se ingrese un flotante válido
        entrada = input("Ingrese un número flotante: ")
        try:
            # Intenta convertir la entrada a un número flotante
            numero = float(entrada)
            # Si tiene éxito, rompe el bucle y devuelve el número flotante
            return numero
        except ValueError:
            # Si falla la conversión, muestra un mensaje y continúa el bucle
            print("Error: El dato ingresado no es un número flotante. Inténtelo de nuevo.")

def calcular_hipotenusa(primer_lado, segundo_lado):
    hipotenusa = primer_lado ** 2 + segundo_lado ** 2
    hipotenusa = sqrt(hipotenusa)
    return hipotenusa

def calcular_angulo_alpha(primer_lado,segundo_lado):
    alpha = primer_lado / segundo_lado
    alpha = atan(alpha)
    return alpha

def calcular_angulo_beta(primer_lado,segundo_lado):
    beta = segundo_lado / primer_lado
    beta = atan(beta)
    return beta

def calcular_area_triangulo_equilatero(primer_lado,segundo_lado):
    area = (primer_lado * segundo_lado)/2
    return area

def calcular_perimetro_triangulo(primer_lado,segundo_lado,hipotenusa):
    perimetro = primer_lado + segundo_lado + hipotenusa
    return perimetro

def calcular_area_rectangulo(primer_lado,segundo_lado):
    area = primer_lado * segundo_lado
    return area

def calcular_perimetro_rectangulo(primer_lado, segundo_lado):
    perimetro = (primer_lado + segundo_lado) * 2
    return perimetro

def calcular_relacion_de_aspecto(primer_lado,segundo_lado):
    relacion_de_aspecto = f"{primer_lado}: {segundo_lado}"
    return relacion_de_aspecto

def calcular_diagonal_cuadrado(lado):
    diagonal = sqrt(2 * lado ** 2)
    return diagonal

def calcular_perimetro_cuadrado(lado):
    perimetro = lado * 4
    return perimetro

def ingresar_entero(mensaje : str):
    while True:
        entero = input(mensaje)
        if entero.isdigit():
            numero = int(entero)
            print("El número ingresado es:", numero)
            return numero
        else:
            print("Error: La entrada no es un número.")