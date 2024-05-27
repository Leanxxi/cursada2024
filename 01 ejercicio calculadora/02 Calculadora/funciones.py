
def ingresar_entero():
    while True:
        entero = input('ingrese entero')
        if entero.isdigit():
            numero = int(entero)
            print("El número ingresado es:", numero)
            break
        else:
            print("Error: La entrada no es un número.")
    return numero

def realizar_factorial(numero):
    if numero == 0:
        resultado = 1
    else: 
        resultado = numero * realizar_factorial(numero -1)
    return resultado

        