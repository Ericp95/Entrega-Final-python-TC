import json

def abrir(productos):
    with open("producto.json", "r") as archivo:
        for linea in archivo:
            productos.append(linea.strip().title())
        

def actualizar(productos):
    with open("producto.json","w") as archivo:
        json.dump(productos, archivo)

def agregar(lista,productos):
    nombre=input("ingrese nombre del producto")
    if nombre.strip()=="":
        print("el producto no puede estar vacio")
    else:
        
        