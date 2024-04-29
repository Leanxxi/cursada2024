
def ingresar_entero():
    while True:
        entero = int(input('ingrese entero'))
        if type(entero) == int:
            break
        else:
            print("Error en ingresar entero, ingrese nuevamente...")
    return entero
    
