import json

def abrir():
    with open("producto.json","r") as archivo:
        productos = json.load(archivo)

def actualizar(productos):
    with open("producto.json","w") as archivo:
        json.dump(productos, archivo)

def agregar(lista,productos):