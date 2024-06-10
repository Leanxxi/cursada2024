# En una institución educativa se busca desarrollar un programa para la gestión de
# profesores, con el fin de optimizar la organización de las clases impartidas en la
# escuela. Los requerimientos específicos del programa son los siguientes:
# 1. Mostrar la lista completa de profesores, excluyendo aquellos que no tengan
# clases asignadas o su estado sea inactivo.
# 2. Mostrar la lista de materias junto con la cantidad de profesores que las
# imparten.
# 3. Modificar la información de un profesor, permitiendo asignar o retirar clases.
# 4. Mostrar toda la información de un profesor específico, incluyendo aquellos
# que no tengan clases asignadas.
# 5. La capacidad de agregar un nuevo profesor, que inicia sin clases asignadas
# 6. La capacidad de dar de baja a un profesor, desasignandole las clases que
# tiene.

# Adicionalmente, se deben generar los siguientes informes:
# A. Identificar al profesor o profesores que imparten la mayor cantidad de materias.
# B. Identificar al profesor o profesores que imparten el mayor número de clases.
# C. Determinar la materia que se imparte con menor frecuencia.
# D. Calcular la cantidad total de clases impartidas.
# E. Identificar la clase a la que se le ha asignado el mayor número de profesores.
# F. Calcular el promedio de edad de los profesores masculinos.
# G. Calcular el promedio de la cantidad de clases impartidas por las profesoras
# femeninas.

# Datos de muestra:
# lista_profesores = [
# {"id":1,"nombre": "José", "apellido": "Pérez", "DNI": 12345678, "genero": "M", "edad": 80,
# "clases": ["A311", "314"], "materias": ["Programación", "Laboratorio"], "activo": True},
# {"id":2,"nombre": "Ana", "apellido": "García", "DNI": 23456789, "genero": "F", "edad": 45,
# "clases": [], "materias": ["Matemáticas", "Estadística"], "activo": False},
# {"id":3,"nombre": "Luis", "apellido": "Martínez", "DNI": 34567890, "genero": "M", "edad": 50,
# "clases": ["D301", "D302"], "materias": ["Física"], "activo": True},
# {"id":4,"nombre": "María", "apellido": "López", "DNI": 45678901, "genero": "F", "edad": 38,
# "clases": ["E401"], "materias": ["Química"], "activo": True},
# {"id":5,"nombre": "Carlos", "apellido": "González", "DNI": 56789012, "genero": "M", "edad":
# 60, "clases": ["F501", "F502", "F503"], "materias": ["Historia", "Geografía"], "activo": True},
# {"id":6,"nombre": "Elena", "apellido": "Rodríguez", "DNI": 67890123, "genero": "F", "edad":
# 29, "clases": [], "materias": ["Inglés"], "activo": False},

# {"id":7,"nombre": "Jorge", "apellido": "Fernández", "DNI": 78901234, "genero": "M", "edad":
# 35, "clases": ["H701", "H702", "H703", "H704"], "materias": ["Educación Física"], "activo":
# True},
# {"id":8,"nombre": "Lucía", "apellido": "Martín", "DNI": 89012345, "genero": "F", "edad": 40,
# "clases": ["I801", "I802"], "materias": ["Filosofía"], "activo": True},
# {"id":9,"nombre": "Miguel", "apellido": "Gutiérrez", "DNI": 90123456, "genero": "M", "edad":
# 55, "clases": [], "materias": ["Biología"], "activo": False},
# {"id":10,"nombre": "Isabel", "apellido": "Ruiz", "DNI": 12309876, "genero": "F", "edad": 33,
# "clases": ["K1001"], "materias": ["Arte"], "activo": True},
# {"id":11,"nombre": "Pedro", "apellido": "Hernández", "DNI": 23410987, "genero": "M",
# "edad": 47, "clases": [], "materias": ["Música"], "activo": False},
# {"id":12,"nombre": "Laura", "apellido": "Díaz", "DNI": 34521098, "genero": "F", "edad": 26,
# "clases": ["M1201", "M1202"], "materias": ["Literatura"], "activo": True}
# ]


from funciones_ABM import *

from menus import menu_principal

if __name__ == '__main__':
    menu_principal()