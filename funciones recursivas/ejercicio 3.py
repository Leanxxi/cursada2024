#3. Realizar una función recursiva que la suma de los dígitos de un número:

def sumar_digitos(numero : int)-> int:
    if numero < 10:
        resultado = numero
    else:
        resultado = numero % 10 + sumar_digitos(numero // 10)
    
    return resultado

numero = input("ingrese su numero para sumar sus digitos")

print (f"{sumar_digitos(numero)}")