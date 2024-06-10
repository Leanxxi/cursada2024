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
        dni = ingresar_entero_positivo("ingrese dni del dueño de la mascota")
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

def ingresar_historial_medico_mascota_nueva():
    while True:
        lista_historial = []
        historial_medico= input("ingrese historial medico")
        if historial_medico == None:
            print("ingrese un historial medico valido")
        else:
            lista_historial.append(historial_medico)
            break
    return lista_historial

def ingresar_nuevo_historial():
    while True:
        historial_medico = input("ingrese historial medico")
        if historial_medico == None:
            print("ingrese un historial medico valido")
        else:
            break
        return historial_medico

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
    historial_medico = ingresar_historial_medico_mascota_nueva()
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

def contar_mascotas(registro_mascotas, dni, nombre_mascota):
    mascosta_encontrada = False
    for i in range(len(registro_mascotas)):
        if registro_mascotas[i][0] == dni and registro_mascotas[i][1] == nombre_mascota:
            mascosta_encontrada = True
    return mascosta_encontrada

def preguntar_si_o_no(pregunta = "desea continuar si/no"):
    """_summary_

    Args:
        pregunta (str, optional): _description_. Defaults to "desea continuar si/no".

    Returns:
        _type_: _description_
    """
    while True:
        respuesta = input(pregunta)
        respuesta = respuesta.capitalize()
        if respuesta != "Si" and respuesta != "No":
            print("respuesta invalida reponda con 'Si' o 'No'")
        else:
            break
    return respuesta

def mostrar_lista(lista: list):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print(f"|| {lista[i][j]}", end= " ")
        print("")
