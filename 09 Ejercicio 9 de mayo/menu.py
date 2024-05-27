import datetime
from funciones import *
# fecha_hoy = datetime.date.today() para obtener la fecha de hoy
# fecha_formato_perzonalizado = fecha_hot.strftime("%d/%m/%Y") para cambiar el formato a dia/mes/año

registro_mascotas = [
    ["12345678", "Luna", 3, "Perro", "Hembra", 8.5, "01/05/2024", "Vacunación anual"],
    ["23456789", "Max", 7, "Gato", "Macho", 5.2, "28/04/2024", "Control de pulgas"],
    ["34567890", "Kiwi", 1, "Dragón", "Hembra", 88000, "02/05/2024", "Recorte de alas"],
    ["45678901", "Rocky", 5, "Perro", "Macho", 12.1, "30/04/2024", "Revisión dental"],
    ["56789012", "Coco", 2, "Gato", "Hembra", 4.8, "03/05/2024", "Desparasitación"]
]

while(True):
    opcion = int(input("Elija una opción"))
    match opcion:
        case 1:
            print("Registrar mascota.")
        case 2:
            print("Dar consulta medica.")
        case 3:
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
    

