import datetime

def ingresar_entero_positivo(mensaje = "ingrese entero positivo")->int:
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


def ingresar_dni():
    while True:
        dni = input("ingrese dni del dueño de la mascota")
        if dni > 0 or type(dni) == int: 
            break
        else:
            print("DNI invalido, ingrese DNI correctamente.")
    return dni

def ingresar_sexo():
    while True:
        sexo = input("ingrese sexo").capitalize()
        if sexo == "Macho" or sexo == "Hembra":
            break
        else:
            print("ingrese sexo correctamente")
    return sexo

def registrar_mascota(dni):
    cliente = []
    dni_duenio = dni
    nombre_mascota = input("ingrese nombre de mascota")
    edad_mascota = ingresar_entero_positivo("ingrese edad de la mascota")
    especie_mascota = input("ingrese especie de la mascota")
    sexo_mascota = ingresar_sexo()
    peso_mascota = ingresar_entero_positivo("ingrese peso de la mascota")
    ultima_visita = datetime.date.today()
    ultima_visita = ultima_visita.strftime("%d/%m/%Y")
    while True:
        historial_medico= input("ingrese historial medico")
        if historial_medico == None:
            print("ingrese un historial medico valido")
        else:
            break
    cliente.append(dni_duenio)
    cliente.append(nombre_mascota)
    cliente.append(edad_mascota)
    cliente.append(especie_mascota)
    cliente.append(sexo_mascota)
    cliente.append(peso_mascota)
    cliente.append(ultima_visita)
    cliente.append(historial_medico)
    return cliente

def normalizar_datos(lista, indice):
    for elemento in lista:
        elemento[indice] = int(elemento[indice])

def enlistar_datos(lista, indice):
    for elemento in lista:
        #elemento_guardado = elemento[indice] 
        elemento[indice] = [elemento[indice]]

def encontrar_cliente(registro: list, cliente : list)->bool:
    for cliente_registrado in registro:
        if cliente_registrado[0] == cliente[0]:
            respuesta = input("al parecer ya hay una mascota registrada a su DNI, ¿desea ingresar una nueva mascota? si/no").upper()
            while True:
                if respuesta == "SI":
                    respuesta = True
                    break
                elif respuesta == "NO":
                    respuesta = False
                    break
                else:
                    print("respuesta invalida, por favor responda con 'si' o con 'no'")
        else:
            print("no se encontró, ningun cliente con ese DNI, ingrese una nueva mascota")
            respuesta = True
    return respuesta

#def agregar_nuevo_historia():

