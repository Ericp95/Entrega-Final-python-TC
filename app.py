from Funciones import agregar, mostrar, buscar, borrar

def menu():

    productos=[]

    while True:

      print("*****MENU*****")
      print("1_Agregar Productos")
      print("2_Mostar productos")
      print("3_Busqueda producto")
      print("4_Eliminar producto")
      print("5_SALIR")

      opciones=int(input("Ingrese opcion de 1 al 6"))

      match opciones:

        case "1":
            nombre=input("ingrese nombre del producto")
            productos=agregar(nombre,productos)
        case "2":
            mostrar(productos)
        case "3":
            nombre=input("ingrese nombre del producto a buscar")
            productos= buscar(nombre,productos)
        case "4":
            nombre=input("ingrese nombre del producto que desea eliminar")
            productos=borrar(nombre, productos)
        case "5":
            print("Gracias por utilizar nuestro menu")
            break