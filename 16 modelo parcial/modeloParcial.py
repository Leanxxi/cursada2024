# Enunciado:
# La empresa "Recursos Inhumanos" nos ha solicitado desarrollar un software de gestión de
# empleados para llevar a cabo un control exhaustivo de los mismos.
# Datos correspondientes a cada empleado:
# ● ID
# ● Nombre
# ● Apellido
# ● DNI
# ● Puesto
# ● Salario
# Consideraciones:
# ● El programa deberá gestionar una lista de hasta 20 empleados. Cada empleado será
# representado mediante un diccionario.
# ● Si se alcanza el límite de 20 empleados, se deberá notificar al usuario. Solo se podrá
# ingresar un empleado en caso de que se efectúe una vacante nueva (o sea que se elimine
# uno).
# ● Al ingresar un empleado, el ID debe ser autoincremental, comenzando en 1. Cada
# empleado tendrá un ID único.
# ● El resto de los datos deberán ser ingresados por consola.
# Validaciones:
# ● Nombre y Apellido: Deben contener solo caracteres alfabéticos, ser nombres propios y no
# exceder los 20 caracteres. No pueden contener números ni caracteres especiales.
# ● Salario: Debe ser un valor numérico entero no menor a $234315.
# ● Puesto: Debe ser uno de los siguientes: “Gerente” / “Supervisor” / “Analista” / “Encargado”
# / “Asistente”.
# ● DNI: Debe ser un valor numérico entre 5000000 y 99999999.
# Opciones del menú:
# 1. Ingresar empleado: Pedirá los datos necesarios y dará de alta a un nuevo empleado,
# asignando un ID autoincremental.
# 2. Modificar empleado: Permitirá alterar cualquier dato del empleado excepto su ID. Se usará
# el ID para identificar al empleado a modificar. Se mostrará un submenú para seleccionar
# qué datos modificar. Se indicará si se realizaron modificaciones o no.

# 3. Eliminar empleado: Eliminará permanentemente a un empleado de la lista original. Se
# pedirá el ID del empleado a eliminar.
# 4. Mostrar todos: Imprimirá por consola la información de todos los empleados en formato
# de tabla:
# ****************************************************
# | Nombre | Apellido | Puesto | Salario |
# —-----------------------------------------------------------
# | German | Scarafilo | Gerente | $500.000 |
# | Giovanni | Lucchetta | Supervisor | $300.000 |
# ****************************************************

# 5. Calcular salario promedio: Calculará e imprimirá el salario promedio de todos los
# empleados.
# 6. Buscar empleado por DNI: Permitir al usuario buscar y mostrar la información de un
# empleado específico ingresando su DNI.
# 7. Ordenar empleados: Ofrecer la opción de ordenar y mostrar la lista de empleados por
# nombre, apellido, o salario de forma ascendente o descendente.
# 8. Salir: Terminará la ejecución del programa.
# Requisitos adicionales:
# ● El programa deberá estar correctamente modularizado, haciendo uso de módulos,
# paquetes y funciones propias para solicitar enteros, flotantes y cadenas, así como para las
# validaciones de cada uno de estos tipos de datos.
# ● El código debe estar programado de manera eficiente y siguiendo buenas prácticas de la
# programación y las reglas de estilo de la cátedra.
# Archivos

# 1. Al iniciar el programa, se deberá leer el archivo Empleados.csv para tener la lista de
# empleados actualizada.
# 2. Al finalizar el programa (puede ser en la opción salir) se deberá actualizar el archivo
# Empleados.csv, con los datos de los empleados.
# 3. Los empleados que hayan sido dados de baja deberán guardarse en un archivo Json,
# llamado “Bajas.json”
# 4. La opción 8 del menú, le solicitará al usuario que ingrese un sueldo. El programa deberá
# generar un reporte con todos los empleados que superen ese sueldo. Una función se
# encargará de realizar dicha acción, la misma deberá guardar el reporte en un archivo de
# texto indicando el número de reporte (el programa deberá recordar este dato de alguna
# forma), la fecha de solicitud del reporte, la cantidad de empleados que coinciden con el
# criterio y el listado.

# 5. La opción 9 del menú, le solicitará al usuario el apellido de un empleado. Realizar un
# informe con las mismas características que el punto anterior.