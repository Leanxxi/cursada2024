#Realizar una función recursiva que calcule la potencia de un número:

def calcular_potencia(base : int, exponente : int):
    if exponente == 0:
        resultado = 1
    else: 
        resultado = base * calcular_potencia(base, exponente - 1)
    return resultado

base = input("ingrese su base")
exponente = input("ingrese su exponente")
print(f"resultado = {calcular_potencia(base , exponente)}")