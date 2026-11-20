from Funciones import abrir,agregar, mostrar, buscar, borrar

def menu():

    productos=[]

    abrir(productos)

    while True:

      print("*****MENU*****")
      print("1_Agregar Productos")
      print("2_Mostar productos")
      print("3_Busqueda producto")
      print("4_Eliminar producto")
      print("5_SALIR")

      opciones=input("Ingrese opcion de 1 al 6")

      match opciones:

        case "1":
            productoAgregar = input("Producto a agregar: ")
            precio = input("Precio del producto: ")
            categoria = input("Categoria del producto: ")
            
            fruta = [productoAgregar,float(precio),categoria]
            productos = agregar(productos, fruta)
        case "2":
            mostrar(productos)
        case "3":
            nombre=input("ingrese nombre del producto a buscar")
            buscar(productos,nombre)
        case "4":
            nombre=input("ingrese nombre del producto que desea eliminar")
            productos=borrar(productos,nombre)
        case "5":
            print("Gracias por utilizar nuestro menu")
            break

menu()