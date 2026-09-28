inventario = {}

try:
    with open("Inventario.txt", "r") as archivo:
            contenido = archivo.read()
            print("Contenido del archivo Inventario.txt:")

            for linea in contenido.splitlines():
                datos = linea.split("|")
                nombre = datos[0]
                precio = float(datos[1])
                cantidad = int(datos[2])
                inventario[nombre] = {"precio": precio, "cantidad": cantidad}
                print(f"Producto: {nombre}, Precio: ${precio:.2f}, Cantidad: {cantidad}")
                print(datos)
except FileNotFoundError:
    print("El archivo Inventario.txt no existe. Se creará uno nuevo al guardar los cambios.") 

ventas_del_dia = []
def ventas_totales():
    total = 0
    for venta in ventas_del_dia:
        total += venta["total"]
    return total

print("===SISTEMA FERREMAX===")
usuario = input("Ingrese su número de empleado: ")
acceso_concedido = False

while True:        
    

    if usuario == "1234":
        acceso_concedido = True

        print("Acceso concedido. Bienvenido al sistema de inventario <<<<FERREMAX>>>>.")
        break
    else:
        print("Acceso denegado. Numero de empleado incorrecto. Intente nuevamente.")
        usuario = input("Ingrese su número de empleado: ")

while True:
    print("===Sistema de Inventario===")
    print("1. Agregar productos: ")
    print("2. Consultar productos: ")
    print("3. Buscar productos: ")
    print("4. Registrar venta de productos: ")
    print("5. Stock bajo: ")
    print("6. Ventas del día: ")
    print("7. Total vendido en el día: ")
    print("8. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("===Agregar productos===")
        nombre = input("Ingrese el nombre del producto: ")
        if nombre in inventario:
            print("El producto ya existe en el inventario. Por favor, actualice la cantidad o el precio si es necesario.")
            continue
        try:
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))

            if precio <= 0 or cantidad < 0:
                print("Error: El precio debe ser mayor que cero y la cantidad debe ser mayor o igual a cero.")
                continue
        except ValueError:
            print("Error: Por favor, ingrese valores numéricos válidos para el precio y la cantidad.")

        else:
            inventario[nombre] = {"precio": precio, "cantidad": cantidad}
            with open("Inventario.txt", "a") as archivo:
                archivo.write(f"{nombre}|{precio}|{cantidad}\n")
            print(f"Producto agregado: {nombre}")


    elif opcion == "2":
        print("===Consultar productos===")
        for producto, info in inventario.items():
            print(f"{producto}: Precio: ${info['precio']}, Cantidad: {info['cantidad']}")

    elif opcion == "3":
        print("===Buscar productos===")
        nombre = input("Ingrese el nombre del producto que desea buscar: ")

        if nombre in inventario:
            print(f"Producto: {nombre}")
            print(f"Precio: ${inventario[nombre]['precio']:.2f}")
            print(f"Cantidad disponible: {inventario[nombre]['cantidad']}")
        else:
            print("Producto no encontrado en el inventario.")

    elif opcion == "4":
        print("===Registro de venta de productos===")
        nombre = input("Ingrese el nombre del producto vendido: ")
        if nombre in inventario:
            try:
                cantidad = int(input("Ingrese la cantidad a vender: "))

                if cantidad <= 0:
                    print("La cantidad debe ser mayor que cero.")
                elif cantidad > inventario[nombre]["cantidad"]:
                    print("No hay suficiente stock para realizar la venta.")

                else:
                    precio = inventario[nombre]["precio"]
                    total = cantidad * precio
                    inventario[nombre]["cantidad"] -= cantidad

                    venta = {
                        "producto": nombre,
                        "cantidad": cantidad,
                        "precio": precio,
                        "total": total
                    }

                    ventas_del_dia.append(venta)
                    print("Venta realizada correctamente.")
                    print(f"Producto: {nombre}")
                    print(f"Cantidad: {cantidad}")
                    print(f"Precio unitario: ${precio:.2f}")
                    print(f"Total: ${total:.2f}")

            except ValueError:
                print("Cantidad inválida. Por favor, ingrese un número entero.")

        else:
            print("Producto no encontrado en el inventario.")

    elif opcion == "5":
        print("===Stock bajo===")
        stock_bajo = {producto: info for producto, info in inventario.items() if info["cantidad"] <= 5}

        if stock_bajo:
            print("Productos con stock bajo:")
            for producto, info in stock_bajo.items():
                print(f"{producto}: Cantidad disponible: {info['cantidad']}")
        else:
            print("No hay productos con stock bajo.")

    elif opcion == "6":
        print("===Ventas del día===")
        if ventas_del_dia:
            for venta in ventas_del_dia:
                print(f"Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio unitario: ${venta['precio']:.2f}, Total: ${venta['total']:.2f}")
        else:
            print("No se han registrado ventas hoy.")

    elif opcion == "7":
        print("===Total vendido en el día===")
        total_vendido = ventas_totales()
        print(f"Total vendido en el día: ${total_vendido:.2f}") 


    elif opcion == "8":
        with open("Inventario.txt", "w") as archivo:
            for producto, info in inventario.items():
                archivo.write(f"{producto}|{info['precio']}|{info['cantidad']}\n")
        print("===GRACIAS POR UTILIZAR EL SISTEMA DE INVENTARIO===")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")