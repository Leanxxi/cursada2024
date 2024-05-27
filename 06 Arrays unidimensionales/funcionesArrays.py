def ingresar_entero(mensaje = "ingrese entero")->int:
    """ingresa un numero entero, lo valida y lo devuelve

    Returns:
        int: numero entero ingresado
    """

    while True:
        entero = input(mensaje)
        if entero.isdigit():
            numero = int(entero)
            print("valor ingresado:", numero)
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

def mostrar_datos(lista : list)-> None:
    for elemento in lista:
        print(elemento)

# lista = [1,3,4,5,6,7,8,9,10,11,12]
# mostrar_datos(lista)

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
    """calcula el promedio pero solo de los numeros positivos sin incluir el 0

    Args:
        lista_de_numeros (list): lista de numeros ingresada

    Returns:
        float: promedio de los numeros positivos de la lista
    """
    suma_de_lista = 0
    for i in range(len(lista_de_numeros)):
        if lista_de_numeros[i] > 0:
            suma_de_lista += lista_de_numeros[i]
    
    promedio = suma_de_lista / len(lista_de_numeros)
    return promedio
#ejercicio 3
 # 3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista
# que recibe como parámetro.
def calcular_producto_de_todos_los_elementos_de_la_lista(lista_de_numeros : list)->float:
    """calcula el producto de todos los elementos de la lista
    Args:
        lista_de_numeros (list): lista de números
    Returns:
        float: producto de todos los elementos de la lista
    """
    producto_de_lista = 1
    for elemento in lista_de_numeros:
        producto_de_lista *= elemento
    
    return producto_de_lista

#ejercicio 4
# 4. Escribir una función que reciba como parámetros una lista de enteros y retorne la posición
# del valor máximo encontrado.  

def encontrar_max_min_posc_lista(lista_de_numeros : list, maximo_minimo_posicion = "maximo")-> float |int:
    """
    Ecuentra el maximo, el minimo o la posicion de los mismos segun el parametro
    Args:
        lista_de_numeros (list):lista de numeros
        
        maximo_minimo_posicion (str, optional): "maximo" = devuelve el valor maximo en la lista. el argumento por defecto es "maximo".
            Returns:
                float: valor maximo 
        
        maximo_minimo_posicion (str, optional):"minimo" devuelve el valor minimo de la lista
            Returns:
                float: valor minimo        
        maximo_minimo_posicion (str, optional):"posicion_minimo": devuelve la posicion del valor minimo en la lista. 
            Returns:
                int: posicion del valor minimo
        
        maximo_minimo_posicion (str, optional):"posicion_maximo": devuelve la posicion del valor maximo en la lista 
            Returns:
                int: posicion del valor maximo 
                  """
    for i in range(len(lista_de_numeros)):
        if i == 0:
            maximo = lista_de_numeros[i]
            minimo = lista_de_numeros[i]
            posicion_maximo = 0
            posicion_minimo = 0
        elif lista_de_numeros[i] > maximo:
            maximo = lista_de_numeros[i]
            posicion_maximo = i
        elif lista_de_numeros[i] < minimo:
            posicion_minimo = i
            minimo = lista_de_numeros[i]

    if maximo_minimo_posicion == "maximo":
        devuelvo = maximo
    elif maximo_minimo_posicion == "minimo":
        devuelvo = minimo
    elif maximo_minimo_posicion == "posicion_maximo":
        devuelvo = posicion_maximo
    elif maximo_minimo_posicion == "posicion_minimo":
        devuelvo = posicion_minimo
    else:
        raise ValueError("error: argumento invalido")
    
    return devuelvo

#ejercicio 5
# 5. Escribir una función que reciba como parámetros una lista de enteros y muestre la/las
# posiciones en donde se encuentra el valor máximo hallado.

def encontrar_pos_maximos(lista_de_numeros:list):
    """devuelve una lista con la poscicion de los valores maximos

    Args:
        lista_de_numeros (list): lista de numeros

    Returns:
        list: posicion de los valores maximos
    """
    maximo = encontrar_max_min_posc_lista(lista_de_numeros)
    maximos_posicion = []
    for i in range(len(lista_de_numeros)):
        if lista_de_numeros[i] == maximo:
            maximos_posicion.append(i)
    return maximos_posicion

# 6. Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista
# de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe
# reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente
# reemplazo y luego retornar la cantidad total de reemplazos realizados.

def reemplazar_nombres(lista_de_nombres : list, nombre_a_reemplazar : str, reemplazo : int)->list:
    """reemplaza los nombres seleccionados con su correspondiente reemplazo

    Args:
        lista_de_nombres (list): lista de nombres 
        nombre_a_reemplazar (str): nombre a reemplazar
        reemplazo (str): reemplazo del nombre

    Returns:
        int: cantidad de reemplazos 
    """
    cantidad_de_reemplazos = 0
    for i in range(len(lista_de_nombres)):
        if lista_de_nombres[i] == nombre_a_reemplazar:
            lista_de_nombres[i] = reemplazo.upper()
            cantidad_de_reemplazos += 1
    return cantidad_de_reemplazos
    


