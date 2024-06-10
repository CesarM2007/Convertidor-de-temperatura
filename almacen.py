
inventario = []

def agregar():
    producto = input("\nIngrese el nombre del producto a agregar: ").lower()
    cantidad =  int(input("Ingrese las existencias del producto: "))
    precio = float(input("Ingrese el precio del producto: "))

    inventario.append([producto,cantidad,precio])

def eliminar():
    
    aeliminar= input("\nIngrese nombre del producto que quiere eliminar: ").lower()

    for x in inventario:
        if x[0] == aeliminar:
            inventario.remove(x)

def cambiar():
    nombre = input("\nIngrese el nombre del producto que quiere actualizar la cantidad: ")
    cant = int(input("Cual es la nueva cantidad del producto: "))

    for x in inventario:
        if x[0] == nombre:
            x[1] = cant

def consulta():

    print("\nEste es su inventario")
    for x in inventario:
        print(x)

x = True

while x:
    (print("""\nIngrese opcion que quiere realizar
1.Agregar producto
2.Eliminar producto
3.Actualizar cantidad de producto
4.Consultar inventario
5.Cerrar programa"""))
    opcion = int(input("¿Qué opción quiere realizar?: "))
    
    if opcion == 1:
        agregar()
    elif opcion == 2:
        eliminar()
    elif opcion == 3:
        cambiar()
    elif opcion == 4:
        consulta()
    elif opcion == 5:
        print("\nGracias por usar el programa")
        x = False
    else:
        print("\nIngrese opcion valida")