def crear_lista_de_numeros()->list:
    lista = []
    seguir = "si"
    while "si":
        if seguir == "si":
            numero_a_agregar = float(input("ingrese un numero"))
            lista.append(numero_a_agregar)
            seguir = input("desea seguir")
        elif seguir == "no": 
            break
        else:
            seguir = input("¿seguir si/no?")
    return lista



#---------------------------------------------------------------
#ejercicio 1

def calcular_el_promedio_de_listas(lista : list):
    suma_de_lista = 0
    for i in range(len(lista)):
        suma_de_lista += lista[i]
    
    promedio = suma_de_lista / len(lista)
    return promedio

#----------------------------------------------------------------
#ejercio 2