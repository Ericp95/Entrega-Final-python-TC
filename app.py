from Funciones import agregar, mostrar

def menu():

    productos=[]

    while True:

      print("*****MENU*****")
      print("1_Agregar Productos")
      print("2_Mostar productos")
      print("3_Listar productos")
      print("4_Busqueda producto")
      print("5_Eliminar producto")
      print("6_SALIR")

      opciones=int(input("Ingrese opcion de 1 al 6"))

      match opciones:

        case "1":
            nombre=input("ingrese nombre del producto")
            productos=agregar(nombre,productos)
        case "2":
            mostrar(productos)
        case "6":
            print("Gracias por utilizar nuestro menu")
            break