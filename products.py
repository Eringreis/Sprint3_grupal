import time

products = [
  {"name": "vasos", "description": "vasos de plástico", "stock": 325, },
  {"name": "cuchillos", "description": "cuchillos de plasticos", "stock": 489,},

  ]


def set_stockProduct(products):
    productUser = input("Ingrese el nombre del producto: ")
    action = input("Deseas agregar o quitar stock: ")

    for product in products:
        if(product["name"] == productUser):
            if(action == "agregar"):
                product["stock"] = product["stock"] + int(input("Ingrese la cantidad a agregar: "))
            elif(action == "quitar"):
                product["stock"] = product["stock"] - int(input("Ingrese la cantidad a quitar: "))
            print("El producto ha sido modificado correctamente")
            print(product)


def add_product():
    name = input("Ingrese el nombre del producto: ")
    description = input("Ingrese la descripción del producto: ")
    stock = input("Ingrese el stock del producto: ")

    while int(stock) < 300 or int(stock) > 500:
      print("El stock debe estar entre 300 y 500")
      stock = input("Ingrese el stock del producto: ")

    products.append({
        "name": name,
        "description": description,
        "stock": stock,
    })

    print(products)

def delete_product():
     name = input("Ingrese el nombre del producto: ")
     for product in products:
        if(product["name"] == name):
            products.remove(product)
            print("El product ha sido eliminado correctamente")
     print(products)

def getAllProducts(products):
    print("--------listando productos--------")
    for product in products:
        time.sleep(1)
        print(product)
        if product["stock"] < 400:
            print("El producto esta por agotarse")


############# Ejecucion del Sistema ##############
action = input("Ingrese la accion que desea realizar (agregar, eliminar, editar o listar): ")

if(action == "agregar"):
    add_product()
elif(action == "eliminar"):
    delete_product()
elif(action == "listar"):
    getAllProducts(products)
elif(action == "editar"):
    set_stockProduct(products)




