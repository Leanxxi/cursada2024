from funciones import *

def mostrar_menu():
    print("Menu:")
    print("1. Ingresar proyecto")
    print("2. Modificar proyecto")
    print("3. Cancelar proyecto")
    print("4. Comprobar proyectos")
    print("5. Mostrar todos")
    print("6. Calcular presupuesto promedio")
    print("7. Buscar proyecto por nombre")
    print("8. Ordenar proyectos")
    print("9. Retomar proyecto")
    print("10. Generar reporte de presupuesto superior")
    print("11. Generar informe de búsqueda por nombre")
    print("12. Salir")

def main():
    mostrar_menu
    while True:
        mostrar_menu()
        opcion = ingresar_entero("Ingrese una opcion")
        match opcion:
            case 1:

                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                pass
            case 11:
                pass
            case 12:
                break
            case _:
                print("opcion invalida")
        os.system("pause")
        os.system("cls")


    