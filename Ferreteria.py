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
    print("4. Registrar venta de productos: ")
    print("5. Stock bajo: ")
    print("6. Ventas del día: ")
    print("7. Total vendido en el día: ")
    print("8. Salir")

    opcion = input("Selecciona una opción: ")


    if opcion == "2":
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

    elif opcion == "7":
        print("===Total vendido en el día===")

        if ventas_del_dia:
            total_dia = 0
            for venta in ventas_del_dia:
                total_dia += venta["total"]
            print(f"Total vendido en el día: ${total_dia:.2f}")
            print(inventario)
        else:
            print("No se han registrado ventas hoy.")

    elif opcion == "8":
        print("Gracias por utilizar el sistema de inventario.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")