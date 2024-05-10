#Leandro Robles A311
#1. Realizar una función recursiva que calcule la suma de los primeros números naturales:

def sumar_naturales(numero : int):
    if numero == 0:
        resultado = 0
        return resultado
    else:
        resultado = numero + sumar_naturales(numero - 1)
    return resultado

#Realizar una función recursiva que calcule la potencia de un número:

def calcular_potencia(base : int, exponente : int):
    if exponente == 0:
        resultado = 1
    else: 
        resultado = base * calcular_potencia(base, exponente - 1)
    return resultado



#3. Realizar una función recursiva que la suma de los dígitos de un número:

def sumar_digitos(numero : int)-> int:
    if numero < 10:
        resultado = numero
    else:
        resultado = numero % 10 + sumar_digitos(numero // 10)
    
    return resultado




# Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La
# función deberá seguir el siguiente prototipo:
# Definición:
# La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de
# los dos anteriores:
def calcular_fibonacci(numero: int)->int:
    if numero < 2:
        resultado = numero
    else: 
        resultado = calcular_fibonacci(numero -1) + calcular_fibonacci(numero - 2)
    return resultado


def menu_funciones_recursivas():
    print("""1- ejercicio 1 sumar \n2- ejercicio 2 potencia\n3- ejercicio 3 sumar digitos\n4- ejercicio 4 fibonacci\n5- salir""")

    opcion = input("ingrese una opcion");
    while True:
        match opcion:
            case "1":
                numero = input("ingrese un numero a sumar")
                print(f"resultado = {sumar_naturales(numero)}")
            case "2":
                base = input("ingrese su base")
                exponente = input("ingrese su exponente")
                print(f"resultado = {calcular_potencia(base , exponente)}")
            case "3":
                numero = input("ingrese su numero para sumar sus digitos")
                print (f"{sumar_digitos(numero)}") 
            case "4":
                numero = input("ingrese un numero para calcular Fibonacci")
                print(f"resultado = {calcular_fibonacci(numero)}")
            case "5":
                break
            case _:
                print("ingrese una opcion correctamente")

menu_funciones_recursivas()


