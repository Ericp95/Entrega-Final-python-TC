import json

def abrir(productos):
    with open("producto.json", "r") as archivo:
        datos = json.load(archivo)
        productos.extend(datos)
        

def actualizar(productos):
    with open("producto.json","w") as archivo:
        json.dump(productos, archivo)

def agregar(lista,productos):
    nombre=input("ingrese nombre del producto")
    if nombre.strip()=="":
        print("el producto no puede estar vacio")
    else:
        productos.append(nombre)
        actualizar()
        print(f"\n el producto: {nombre.title()} agregado correctamente")


def mostrar(productos):
    print("*****lista de productos*****")
    for producto in productos:  
         productos.sort()
         print(producto.title())   