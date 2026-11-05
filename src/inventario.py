from archivos import leer_archivo, guardar_archivo
from datetime import datetime


def guardar_cambios_inventario(productos, movimientos):

    productos_anteriores = leer_archivo("productos.json")
    movimientos_anteriores = leer_archivo("inventario.json")

    try:
        guardar_archivo("productos.json", productos)
        guardar_archivo("inventario.json", movimientos)

    except Exception as error:

        try:
            guardar_archivo("productos.json", productos_anteriores)
            guardar_archivo("inventario.json", movimientos_anteriores)

        except Exception:
            print("Advertencia: no se pudieron restaurar todos los archivos.")

        raise error


def consultar_inventario():

    productos = leer_archivo("productos.json")

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    print("\n===== CONSULTA DE INVENTARIO =====")

    for producto in productos:

        print("------------------------------")
        print("Código:", producto["codigo"])
        print("Nombre:", producto["nombre"])
        print("Existencias:", producto["existencias"])
        print("Existencias mínimas:", producto["existencia_minima"])
        print("Estado:", producto["estado"])


def registrar_entrada():

    productos = leer_archivo("productos.json")

    codigo = input("Ingrese el código del producto: ").strip()

    if codigo == "":
        print("Error: debe ingresar un código.")
        return

    for producto in productos:

        if producto["codigo"].lower() == codigo.lower():

            if producto["estado"] != "activo":
                print("No se pueden registrar movimientos manuales en productos inactivos.")
                return

            try:
                cantidad = int(input("Ingrese la cantidad que ingresará: "))

                if cantidad <= 0:
                    print("Error: la cantidad debe ser mayor que cero.")
                    return

            except ValueError:
                print("Error: debe ingresar una cantidad entera válida.")
                return

            producto["existencias"] += cantidad

            movimientos = leer_archivo("inventario.json")

            movimiento = {
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "codigo_producto": producto["codigo"],
                "tipo": "entrada",
                "cantidad": cantidad,
                "descripcion": "Entrada manual de productos"
            }

            movimientos.append(movimiento)

            try:
                guardar_cambios_inventario(productos, movimientos)

            except Exception as error:
                print("Error al registrar la entrada:", error)
                return

            print("Entrada registrada correctamente.")
            return

    print("No se encontró ningún producto con ese código.")


def registrar_salida():

    productos = leer_archivo("productos.json")

    codigo = input("Ingrese el código del producto: ").strip()

    if codigo == "":
        print("Error: debe ingresar un código.")
        return

    for producto in productos:

        if producto["codigo"].lower() == codigo.lower():

            if producto["estado"] != "activo":
                print("No se pueden registrar movimientos manuales en productos inactivos.")
                return

            try:
                cantidad = int(input("Ingrese la cantidad que saldrá: "))

                if cantidad <= 0:
                    print("Error: la cantidad debe ser mayor que cero.")
                    return

            except ValueError:
                print("Error: debe ingresar una cantidad entera válida.")
                return

            if cantidad > producto["existencias"]:
                print("Error: no hay existencias suficientes.")
                return

            producto["existencias"] -= cantidad

            movimientos = leer_archivo("inventario.json")

            movimiento = {
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "codigo_producto": producto["codigo"],
                "tipo": "salida",
                "cantidad": cantidad,
                "descripcion": "Salida manual de productos"
            }

            movimientos.append(movimiento)

            try:
                guardar_cambios_inventario(productos, movimientos)

            except Exception as error:
                print("Error al registrar la salida:", error)
                return

            print("Salida registrada correctamente.")
            return

    print("No se encontró ningún producto con ese código.")


def mostrar_movimientos():

    movimientos = leer_archivo("inventario.json")

    if len(movimientos) == 0:
        print("No hay movimientos registrados.")
        return

    print("\n===== HISTORIAL DE INVENTARIO =====")

    for movimiento in movimientos:

        print("------------------------------")
        print("Fecha:", movimiento["fecha"])
        print("Código del producto:", movimiento["codigo_producto"])
        print("Tipo de movimiento:", movimiento["tipo"])
        print("Cantidad:", movimiento["cantidad"])
        print("Descripción:", movimiento["descripcion"])


def menu_inventario():

    while True:

        print("\n===== GESTIÓN DE INVENTARIO =====")
        print("1. Consultar inventario")
        print("2. Registrar entrada")
        print("3. Registrar salida")
        print("4. Mostrar movimientos")
        print("5. Regresar al menú principal")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                consultar_inventario()

            elif opcion == 2:
                registrar_entrada()

            elif opcion == 3:
                registrar_salida()

            elif opcion == 4:
                mostrar_movimientos()

            elif opcion == 5:
                print("Regresando al menú principal...")
                break

            else:
                print("Error: seleccione una opción del 1 al 5.")

        except ValueError:
            print("Error: debe ingresar un número válido.")