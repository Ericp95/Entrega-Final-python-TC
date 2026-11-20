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
    for producto in productos:  
         productos.sort()
         print(producto.title())   

def borrar(lista, productos):
    if productos not in lista:
        print("el elemento a borrar no existe")
        return lista
    nueva=lista.copy()
    nueva.remove(productos)
    actualizar(nueva)

    print(f"el producto {productos}, eliminado con exito")
    return nueva

def buscar(lista, producto):
    encontrado = False

    for item in lista:
        if item.lower() == producto.lower():
            encontrado = True
            break

    if encontrado:
        print(f"El producto {producto.title()} existe")
    else:
        print(f"El producto {producto.title()} no existe")