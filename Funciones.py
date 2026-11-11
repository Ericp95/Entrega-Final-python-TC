import json

def abrir():
    with open("producto.json","r") as archivo:
        productos = json.load(archivo)

def actualizar():

