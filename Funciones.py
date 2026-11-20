import json


def abrir(productos):
    try:
        with open("producto.json", "r") as archivo:
            datos = json.load(archivo)
            productos.extend(datos)

    except FileNotFoundError:
        with open("producto.json", "w") as archivo:
            json.dump([], archivo)
        

def actualizar(lista):
    with open("producto.json","w") as archivo:
        json.dump(lista, archivo)

def agregar(lista,productos):
       
        if productos.strip()=="":
           print("el prosucto no puede estar vacio")
           return lista
        nuevalista=lista.copy()
        nuevalista.append(productos)
        actualizar(nuevalista)
        print(f"\n el producto: {productos.title()} agregado correctamente")
        return nuevalista


def mostrar(productos):
    print("*****lista de productos*****")
    
    actualizar(productos)
    for producto in productos:  
         productos.sort()
         print(producto.title())   

def borrar(lista, productos):
    if productos not in lista:
        print("el elemento a borrar no existe")
    nueva=lista.copy
    nueva.remove(productos)
    print(f"el producto {productos}, eliminado con exito")
    return nueva

def buscar(lista, producto):
    if producto in lista:
        print(f"el producto con el nombre {producto}, existe")
    else:
        print("el producto que busca, no existe")