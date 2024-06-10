# En una veterinaria se busca implementar un sistema de registro para llevar un seguimiento
# detallado de las mascotas atendidas en el establecimiento. El registro deberá contener la
# siguiente información:
# ● DNI del dueño de la mascota.
# ● Nombre de la mascota.
# ● Edad de la mascota.
# ● Especie de la mascota.
# ● Sexo de la mascota.
# ● Peso de la mascota.
# ● Fecha de la última visita.
# ● Historial médico.
# El programa debe permitir al veterinario:
# 1. Registrar nuevas mascotas, ingresando todos los datos requeridos.
# 2. Actualizar la información de una mascota en cada nueva visita, manteniendo un
# historial médico completo y actualizado.
# Además, se requiere que el sistema proporcione las siguientes funcionalidades:
# 1. Mostrar información completa de todas las mascotas: Esta función permitirá
# visualizar todos los datos registrados de todas las mascotas atendidas en la
# veterinaria.
# 2. Mostrar información completa solo de las mascotas que superen el promedio
# de edad: Esta opción mostrará únicamente los datos de las mascotas cuya edad
# supere el promedio de edad de todas las mascotas registradas.
# 3. Calcular el promedio de peso de todas las mascotas: Esta función calculará y
# mostrará el promedio de peso de todas las mascotas registradas en la veterinaria.
# 4. Contar la cantidad de perros registrados: Permitirá obtener el número total de
# perros registrados en el sistema.
# 5. Identificar el tipo de mascota más registrado: Esta función determinará cuál es el
# tipo de mascota (perro, gato, ave, etc.) que más se ha registrado en la veterinaria.


from funciones import *
import os
# fecha_hoy = datetime.date.today() para obtener la fecha de hoy
# fecha_formato_perzonalizado = fecha_hoy.strftime("%d/%m/%Y") para cambiar el formato a dia/mes/año



registro_mascotas = [
    ["12345678", "Luna", 3, "Perro", "Hembra", 8.5, "01/05/2024", "Vacunación anual"], 
    ["12345678", "Sol", 3, "Perro", "Hembra", 8.5, "01/05/2024", "Vacunación anual"],
    ["23456789", "Max", 7, "Gato", "Macho", 5.2, "28/04/2024", "Control de pulgas"],
    ["34567890", "Kiwi", 1, "Dragón", "Hembra", 88000, "02/05/2024", "Recorte de alas"],
    ["45678901", "Rocky", 5, "Perro", "Macho", 12.1, "30/04/2024", "Revisión dental"],
    ["56789012", "Coco", 2, "Gato", "Hembra", 4.8, "03/05/2024", "Desparasitación"]
]

def mostrar_menu():
    print("""bienvenido al Menu de la veterinaria
opciones:
          1-Registrar o logear mascota
          2-Dar consulta medica
          3-mostrar todas las mascotas
          4-mostrar solo mascotas que superen el promedio de edad
          5-calcular promedio de mascotas
          6-contar cantidad de perros
          7-identificar tipo de mascota mas registrada
          8-Salir
""")

normalizar_datos(registro_mascotas, 0)
enlistar_datos(registro_mascotas, 7) #transforma el dato del indice 7 en una lista para que se le pueda añadir un historial

while(True):
    mostrar_menu()
    opcion = int(input("Elija una opción"))
    match opcion:
        case 1:
            flag_mascota_encontrada = False
            
            dni = ingresar_dni()
            nombre_mascota = input("ingrese el nombre de su mascota para logearse ").capitalize()        
            mascota_encontrada = contar_mascotas(registro_mascotas, dni, nombre_mascota)
            flag_login = True
            if mascota_encontrada == True:
                
                print(f"login realizado con exito")
            else:
                print("al parecer no hay ninguna mascota registrada a ese nombre y DNI")
                respuesta = preguntar_si_o_no("¿desea añadir mascota nueva?")
                if respuesta == 'Si':
                    #registra nueva mascota
                    nueva_mascota = registrar_mascota(dni)
                    registro_mascotas.append(nueva_mascota)
                if respuesta == 'No':
                    flag_login = False
                    print("saliendo...")
            
        case 2:
            if flag_login == True:
                while flag_mascota_encontrada == False:
                                       
                    for mascota in registro_mascotas:
                        if mascota[1] == nombre_mascota and dni == mascota[0]:
                            historial = input("ingrese nuevo historial medico: ")
                            mascota[7].append(historial)
                            flag_mascota_encontrada = True
                    
                    if flag_mascota_encontrada == False:
                        print("no existe ninguna mascota asignada a ese nombre y a ese dni, escriba el nombre correctamente")

                    print("Dar consulta medica.")
            else:
                print("debe logear o registrar una mascota para poder actualizar su historial medico")
        case 3:
            mostrar_lista(registro_mascotas)
            print("Mostrar todas las mascotas.")
        case 4:
            print("Mostrar solo mascotas que superen promedio de edad.")
        case 5:
            print("Calcular el promedio de mascotas")
        case 6:
            print("Contar cantidad de perros.")
        case 7:
            print("Identificar tipo de mascota mas registrado.")
        case 8:
            print("Saliendo del sistema.")
            break
    os.system("pause")
    os.system("clear")
    

