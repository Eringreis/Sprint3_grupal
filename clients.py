import random


clients = [
    {"ID": "1", "name": "Juan", "lastname": "Perez",
        "password": "12345678", "age": 18},
    {"ID": "2", "name": "Pedro", "lastname": "Gonzalez",
        "password": "12345678", "age": 40},
    {"ID": "3", "name": "Carlos", "lastname": "Lopez",
        "password": "12345678", "age": 32},
    {"ID": "4", "name": "Maria", "lastname": "Castro",
        "password": "12345678", "age": 23},
]


def addClient():
    name = input("Ingrese el nombre del cliente: ")
    lastName = input("Ingrese el apellido del cliente: ")
    age = input("Ingrese la edad del cliente: ")
    password = input("Ingrese la contraseña del cliente: ")

    user = {
        "ID": random.randrange(100),
        "name": name,
        "lastname": lastName,
        "age": age,
        "password": password
    }
    clients.append(user)
    print("El se ha registrado correctamente")

def deleteClient():
    user = input("Ingrese el nombre o id del cliente: ")
    for client in clients:
        if(client["ID"] == user or client["name"] == user):
            clients.remove(client)
            print("El cliente ha sido eliminado correctamente")


def getClient():
    user = input("Ingrese el nombre o id del cliente: ")
    for client in clients:
        if(client["ID"] == user or client["name"] == user):
            print("El cliente es: ", client)
            return client

############# Ejecucion del Sistema ##############

action = input("Ingrese la accion que desea realizar (agregar, eliminar o buscar): ")

if(action == "agregar"):
    addClient()
elif(action == "eliminar"):
    deleteClient()
elif(action == "buscar"):
    getClient()
