# Ejercicio 01: Escribe una función que calcule el área de un círculo. La función debe recibir
# el radio como parámetro y devolver el área.
# Ejercicio 02: Crea una función que verifique si un número dado es par o impar. La función
# debe imprimir un mensaje indicando si el número es par o impar.
# Ejercicio 03: Define una función que encuentre el máximo de tres números. La función
# debe aceptar tres argumentos y devolver el número más grande.
# Ejercicio 04: Diseña una función que calcule la potencia de un número. La función debe
# recibir la base y el exponente como argumentos y devolver el resultado.
# Nota: Todas las funciones deben estar probadas y se podrá acceder a cada una de
# ellas mediante un menú de opciones.
# Leandro Robles A311

def mostrar_menu():
    print("Bienvenido al menú de opciones")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Salir")

def calcular_area_circulo(radio, pi = 3.14):
    area = pi * (radio ** 2)
    return area

def verificar_pares_impares(numero):
    if numero % 2 == 0:
        print("su numero es par")
    elif numero % 2 == 1:
        print("su numero es impar")
    else:
        print("su numero no es par ni impar")

def encontrar_maximo_de_tres_numeros(numero_1 = 0, numero_2 = 0, numero_3 = 0):
    if numero_1 > numero_2:
        if numero_1 > numero_3:
            print(f"el numero {numero_1} es el mayor")
        else:
            print(f"el numero {numero_3} es el mayor")
    elif numero_2 > numero_3:
        print(f"el numero {numero_2} es el mayor")
    else:
        print(f"el numero {numero_3} es el mayor")

        
def calcular_potencia(base, exponente):
    resultado = base ** exponente
    return resultado

while True:
    mostrar_menu()
    opcion = input("ingrese una opcion")
    if opcion == "1":
        radio = float(input("ingrese radio"))
        print("radio: ",calcular_area_circulo(radio))
    elif opcion == "2":
        numero = float(input("ingrese un numero"))
        verificar_pares_impares(numero)
    elif opcion == "3":
        encontrar_maximo_de_tres_numeros(3 , 2 , 1)
    elif opcion == "4":
        print(f"el resultado es{calcular_potencia(2,4)}")
    elif opcion == "5":
        break
    else:
        print("opcion no valida")

