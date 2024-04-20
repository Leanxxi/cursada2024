#1. Realizar una función recursiva que calcule la suma de los primeros números naturales:

def sumar_naturales(numero : int):
    if numero == 0:
        resultado = 0
        return resultado
    else:
        resultado = numero + sumar_naturales(numero - 1)
    return resultado


numero = input("ingrese un numero a sumar")
print(f"resultado = {sumar_naturales(numero)}")