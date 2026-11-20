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
       
        if productos[0].strip()=="":
           print("el prosucto no puede estar vacio")
           return lista
        nuevalista=lista.copy()
        nuevalista.append(productos)
        actualizar(nuevalista)
        print(f"\n el producto: {productos[0].title()} agregado correctamente")
        return nuevalista


def mostrar(productos):
    print("*****lista de productos*****")
    for producto in productos:  
         productos.sort()
         print(f"Nombre Producto: {producto[0].title()} | Precio: ${producto[1]} | Categoría: {producto[2]}")   

def borrar(lista,nombre):
    nueva = lista.copy()

    for producto in nueva:
        if producto[0].lower() == nombre.lower():
            nueva.remove(producto)
            actualizar(nueva)
            print(f"El producto {nombre.title()} fue eliminado correctamente")
            return nueva

    print("El producto no existe")
    return lista

def buscar(lista, nombre):
    for producto in lista:
        if producto[0].lower() == nombre.lower():
            print("\nProducto encontrado:")
            print(f"Nombre: {producto[0].title()}")
            print(f"Precio: ${producto[1]}")
            print(f"Categoría: {producto[2]}")
            return True

    print("El producto no existe")
    return False