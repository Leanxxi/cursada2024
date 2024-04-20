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

numero = input("ingrese un numero para calcular Fibonacci")
print(f"resultado = {calcular_fibonacci(numero)}")