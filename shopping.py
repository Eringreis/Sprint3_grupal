

############# Ejecucion del Sistema ##############
methodShopping = input("Que tipo de envio necesitas (rapido o largo): ")
distance = int(input("Ingrese la distancia de tu envio: "))

print("Detalla el producto que deseas enviar: ")

name = input("Ingrese el nombre del producto: ")
description = input("Ingrese la descripción del producto: ")
stock = int(input("Ingrese el stock del producto: "))

productAdd = {
    "name": name,
    "description": description,
    "stock": stock,
}


bodega_A = [
    {"name": "tenedores", "description": "tenedores de carton", "stock": 401},
    {"name": "tenedores", "description": "tenedores de carton", "stock": 20}
]
bodega_B = [
    {"name": "tenedores", "description": "tenedores de carton", "stock": 401}
]


def add_productFast(distance):

    stockBodega = 0

    if(distance > 1000):

        for produc in bodega_A:
            stockBodega = stockBodega + int(produc["stock"])
        print(stockBodega)
        if(stockBodega + productAdd["stock"] < 500):
            bodega_A.append(productAdd)
            print("El producto se ha agregado en la bodega A")
            print(bodega_A)
        else:
            print("No hay espacio suficiente en la bodega A")

    elif (distance <= 1000):
        for produc in bodega_B:
            stockBodega = stockBodega + int(produc["stock"])

        if(stockBodega + productAdd["stock"] < 500):
            bodega_B.append(productAdd)
            print("El producto se ha agregado en la bodega B")
            print(bodega_B)
        else:
            print("No hay espacio suficiente en la bodega B")


add_productFast(distance)
