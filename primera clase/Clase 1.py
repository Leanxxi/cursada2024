
continuar = True

for i in range(5):
    tipo = input("ingrese tipo")

    while(tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol"):
        tipo = input("reingrese tipo")

    precio = input("ingrese precio")
    while(precio < 100 and precio > 300):
        print("precio invalido")
        precio = input("reingrese precio")

    cantidad = input("ingrese cantidad")
    while(cantidad < 0 and cantidad > 1000):
        print("la cantidad no puede ser menor a 0 y mayor a 1000")
        cantidad = input("reingrese cantidad")

    marca = input("ingrese marca")
    fabricante = input("ingrese fabricante")
    
    
    if(tipo == "barbijo" and continuar):
        continuar = False
        barbijo_mas_caro = precio
        unidades_del_barbijo_mas_caro = cantidad
        fabricante_del_barbijo_mas_caro = fabricante
    elif(tipo == "barbijo" and precio > barbijo_mas_caro):
        barbijo_mas_caro = precio
        unidades_del_barbijo_mas_caro = cantidad
        fabricante_del_barbijo_mas_caro = fabricante

    if(i == 0 or cantidad > item_con_mas_unidades): #item con más unidades
        item_con_mas_unidades = cantidad
        fabrcante_con_mas_unidades = fabricante

    
