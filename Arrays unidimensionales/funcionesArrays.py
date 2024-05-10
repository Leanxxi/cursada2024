def ingresar_entero(mensaje = "ingrese entero")->int:
    """ingresa un numero entero, lo valida y lo devuelve

    Returns:
        int: numero entero ingresado
    """

    while True:
        entero = input(mensaje)
        if entero.isdigit():
            numero = int(entero)
            print("El número ingresado es:", numero)
            return numero
        else:
            print("Error: La entrada no es un número.")

def ingresar_flotante()->float:
    """ingresa un caracter, intenta cambiarlo a un numero flotante, si tiene exito lo devuelve y rompe el bucle
    si no muestra un mensaje de error
    Returns:
        float: numero flotante ingresado
    """
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




def crear_lista_de_numeros()->list:
    """crea una lista vacia, en la cual se le pueden ir agregando solamente numeros
    si lo ingresado por el usuario no es un número saldrá un mensaje de error
    si lo ingresado por el usuario es un numero, preguntará si desea seguir añadiendo numeros

    Returns:
        list: lista de numeros
    """
    lista = []
    seguir = "si"
    while "si":
        if seguir == "si":
            numero_a_agregar = ingresar_flotante()
            lista.append(numero_a_agregar)
            seguir = input("desea seguir añadiendo numeros:")
        elif seguir == "no": 
            break
        else:
            seguir = input("¿seguir si/no?")
    return lista



#---------------------------------------------------------------
#ejercicio 1

def calcular_el_promedio_de_listas(lista_de_numeros : list)->float :
    """calcula el promedio de la lista de numeros argumentada
    Args:
        lista (list): lista de numeros
    Returns:
        float: promedio de la lista de numeros
    """
    suma_de_lista = 0
    for i in range(len(lista_de_numeros)):
        suma_de_lista += lista_de_numeros[i]
    
    promedio = suma_de_lista / len(lista_de_numeros)
    return promedio

#----------------------------------------------------------------
#ejercio 2

def calcular_promedio_positivos(lista_de_numeros : list)->float :
    """_summary_

    Args:
        lista_de_numeros (list): _description_

    Returns:
        float: _description_
    """
    suma_de_lista = 0
    for i in range(len(lista_de_numeros)):
        if lista_de_numeros[i] > 0:
            suma_de_lista += lista_de_numeros[i]
    
    promedio = suma_de_lista / len(lista_de_numeros)
    return promedio