inventario = {
    "martillo": {"precio": 15.99, "cantidad": 10},
    "destornillador": {"precio": 7.49, "cantidad": 25},
    "taladro": {"precio": 89.99, "cantidad": 5},
    "llave inglesa": {"precio": 12.99, "cantidad": 8},
    "cinta métrica": {"precio": 5.99, "cantidad": 20},
    "sierra": {"precio": 49.99, "cantidad": 3}
}

ventas_del_dia = []
print("Bienvenido al sistema de inventario de la ferretería.")

while True:
    print("===Sistema de Inventario===")
    print("1. Agregar productos: ")
    print("2. Consultar productos: ")
    print("3. Buscar productos: ")
    print("4. Vender productos: ")
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
            print(f"Producto agregado: {nombre}")


    elif opcion == "2":
        print("===Consultar productos===")
        for producto, info in inventario.items():
            print(f"{producto}: Precio: ${info['precio']}, Cantidad: {info['cantidad']}")
    
    elif opcion == "5":
        print("===Stock bajo===")
        stock_bajo = {producto: info for producto, info in inventario.items() if info['cantidad'] <= 5}
        if stock_bajo:
            for producto, info in stock_bajo.items():
                print(f"{producto}: Cantidad: {info['cantidad']}")
        else:
            print("No hay productos con stock bajo.")

    elif opcion == "6":
        print("===Ventas del día===")
        if ventas_del_dia:
            for venta in ventas_del_dia:
                print(f"Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Total: ${venta['total']:.2f}")
        else:
            print("No se han registrado ventas hoy.")






    elif opcion == "8":
        print("Gracias por utilizar el sistema de inventario.")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 8.")