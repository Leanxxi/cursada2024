# La división de higiene está trabajando en un control de stock para productos
# sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
# contagio, de cada una debe obtener los siguientes datos:
# 1. El tipo (validar "barbijo", "jabón" o "alcohol")
# 2. El precio: (validar entre 100 y 300)
# 3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
# 1000 unidades)
# 4. La marca y el Fabricante.
# Se debe informar lo siguiente:
# A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
# B. Del ítem con más unidades, el fabricante.
# C. Cuántas unidades de jabones hay en total.
#Leandro Nicolás Robles 311

pasar_primer_barbijo = True
acumulador_de_unidades_de_jabon = 0


for i in range(2):
    tipo = input("ingrese tipo")

    while(tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol"):
        tipo = input("reingrese tipo")

    precio = float(input("ingrese precio"))
    while(precio < 100 or precio > 300):
        print("precio invalido")
        precio = float(input("reingrese precio"))

    cantidad = int(input("ingrese cantidad"))
    while(cantidad < 0 or cantidad > 1000):
        print("la cantidad no puede ser menor a 0 y mayor a 1000")
        cantidad = int(input("reingrese cantidad"))

    marca = input("ingrese marca")
    fabricante = input("ingrese fabricante")
    
    
    if(tipo == "barbijo" and pasar_primer_barbijo):
        pasar_primer_barbijo = False
        barbijo_mas_caro = precio
        unidades_del_barbijo_mas_caro = cantidad
        fabricante_del_barbijo_mas_caro = fabricante
    elif(tipo == "barbijo" and precio > barbijo_mas_caro):
        barbijo_mas_caro = precio
        unidades_del_barbijo_mas_caro = cantidad
        fabricante_del_barbijo_mas_caro = fabricante

    if(i == 0 or cantidad > item_con_mas_unidades): #item con más unidades
        item_con_mas_unidades = cantidad
        fabricante_con_mas_unidades = fabricante
    if tipo == "jabon":
        acumulador_de_unidades_de_jabon += cantidad

if pasar_primer_barbijo == False:
    print(f"el barbijo mas caro cuesta:{barbijo_mas_caro} su cantidad de unidades es{unidades_del_barbijo_mas_caro},del fabricante {fabricante_del_barbijo_mas_caro}")
print(f"item con mas unidades:{item_con_mas_unidades} y su fabricante es{fabricante_con_mas_unidades}")
print(f"unidades de jabones en total: {acumulador_de_unidades_de_jabon}")

    
