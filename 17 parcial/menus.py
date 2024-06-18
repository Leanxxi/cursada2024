from funciones import *
from mostrar_menus import *
path_proyectos_csv = '17 parcial\Proyectos - Proyectos.csv'

def main():
    mostrar_menu
    while True:
        mostrar_menu()
        opcion = ingresar_entero("Ingrese una opcion")
        match opcion:
            case 1:
                ingresar_proyecto(path_proyectos_csv)               
            case 2:
                proyecto_modificado = submenu_modificar_proyecto(path_proyectos_csv)
                #establecer_modificacion_en_archivo(proyecto_modificado, path_proyectos_csv)
            case 3:
                print("3. Cancelar proyecto")
            case 4:
                print("4. Comprobar proyectos")
            case 5:
                print("5. Mostrar todos")
            case 6:
                print("6. Calcular presupuesto promedio")
            case 7:
                print("7. Buscar proyecto por nombre")
            case 8:
                print("8. Ordenar proyectos")
            case 9:
                print("9. Retomar proyecto")
            case 10:
                print("10. Generar reporte de presupuesto superior")
            case 11:
                print("11. Generar informe de búsqueda por nombre")
            case 12:
                break #salir
            case _:
                print("Ingrese una opcion existente")
        os.system("pause")
        os.system("cls")

def submenu_cambiar_estado():
    mostrar_submenu_cambiar_estado()
    while True:
        opcion = ingresar_entero_positivo("ingrese opcion")
        match opcion:
            case 1:
                estado = "Activo"
            case 2:
                estado = "Cancelado"
            case 3:
                estado = "Finalizado"
            case 4:
                break
            case _:
                print("Ingrese una opcion existente")
        print(f"Estado actualizado a estado: {estado}")
        os.system("pause")
        os.system("cls")
    return estado

# def establecer_modificacion_en_archivo(proyecto_modificado : list, path):
#     nueva_cadena = []
#     for i in range(len(proyecto_modificado)):
#         nueva_cadena.append(str(proyecto_modificado[i]))
#     separador = ','
#     nueva_cadena = separador.join((nueva_cadena))
#     print(nueva_cadena)

#     # with open(path, 'a') as archivo:
#     #     archivo.write('\n' + nueva_cadena)

def submenu_modificar_proyecto(path):
    while True:
        
        bandera_modificacion = False
        
        lista_proyectos = pasar_csv_a_lista_diccionarios(path)
        normalizar_datos(lista_proyectos)
            

        proyecto = encontrar_proyecto(lista_proyectos)
        if proyecto == False:
            continue
        mostrar_submenu_modificar_proyecto()
        opcion = ingresar_entero("ingrese una opcion")
        match opcion:
            case 1:
                proyecto['Nombre del Proyecto'] = input("Ingrese nuevo nombre del Proyecto")
                print(f"Se ha cambiado el nombre a {proyecto['Nombre del Proyecto']}")
                bandera_modificacion = True
            case 2:
                proyecto['Descripcion'] = input("Ingrese nueva descripcion")
                print(f"Se ha cambiado el descripcion a {proyecto['Descripcion']}")
                bandera_modificacion = True
            case 3:
                proyecto['Presupuesto'] = ingresar_entero('ingrese presupuesto: ')
                print(f"Se ha cambiado el presupuesto a {proyecto['Presupuesto']}")
                bandera_modificacion = True
            case 4:
                
                fecha_a_actualizar = pedir_fecha('ingrese fecha de Inicio a actualizar')
                fecha_ok = validar_fecha_cronologicamente(proyecto['Fecha Final'],fecha_a_actualizar)
                if fecha_ok == False:
                    print("La fecha Final no puede ser menor a la fecha de Inicio")
                else:
                    proyecto['Fecha de Inicio'] = fecha_a_actualizar
                    print(f"Se ha cambiado la fecha del inicio del proyecto a {proyecto['Fecha de Inicio']}")
                    bandera_modificacion = True
            case 5:
                fecha_a_actualizar = pedir_fecha('ingrese fecha de Inicio a actualizar')
                fecha_ok = validar_fecha_cronologicamente(fecha_a_actualizar,proyecto['Fecha de Inicio'])
                if fecha_ok == False:
                    print("La fecha Final no puede ser menor a la fecha de Inicio")
                else:
                    proyecto['Fecha de Fin'] = fecha_a_actualizar
                    print(f"Se ha cambiado la fecha del final del proyecto a {proyecto['Fecha de Fin']}")
                    bandera_modificacion = True
            case 6:
                estado = submenu_cambiar_estado()
                proyecto['Estado'] = estado
                bandera_modificacion = True
            case 7:
                break
            case _:
                print("Ingrese una opcion existente")
        if bandera_modificacion == True:
            return proyecto
        else:
            print("no se han realizado cambios")
        os.system("pause")
        os.system("cls")



main()