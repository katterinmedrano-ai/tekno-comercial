from archivos import leer_archivo, guardar_archivo
from datetime import datetime

IVA = 0.12

def guardar_cambios_venta(productos, ventas, movimientos):

    productos_anteriores = leer_archivo("productos.json")
    ventas_anteriores = leer_archivo("ventas.json")
    movimientos_anteriores = leer_archivo("inventario.json")

    try:
        guardar_archivo("productos.json", productos)
        guardar_archivo("ventas.json", ventas)
        guardar_archivo("inventario.json", movimientos)

    except Exception:

        archivos_restaurados = True

        try:
            guardar_archivo("productos.json", productos_anteriores)
        except Exception:
            archivos_restaurados = False

        try:
            guardar_archivo("ventas.json", ventas_anteriores)
        except Exception:
            archivos_restaurados = False

        try:
            guardar_archivo("inventario.json", movimientos_anteriores)
        except Exception:
            archivos_restaurados = False

        if not archivos_restaurados:
            print("Advertencia: no se pudieron restaurar todos los archivos.")

        raise
    
def generar_numero_venta(ventas):

    if len(ventas) == 0:
        return "V001"

    numeros = []

    for venta in ventas:
        numero = int(venta["numero"][1:])
        numeros.append(numero)

    siguiente = max(numeros) + 1

    return "V" + str(siguiente).zfill(3)

def registrar_venta():

    productos = leer_archivo("productos.json")
    ventas = leer_archivo("ventas.json")
    movimientos = leer_archivo("inventario.json")

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    detalles = []

    print("\n===== REGISTRO DE VENTA =====")

    while True:

        codigo = input(
            "Ingrese el código del producto (o escriba FIN para terminar): "
        ).strip()

        if codigo.lower() == "fin":
            break

        if codigo == "":
            print("Error: debe ingresar un código.")
            continue

        producto_encontrado = None

        for producto in productos:
            if producto["codigo"].lower() == codigo.lower():
                producto_encontrado = producto
                break

        if producto_encontrado is None:
            print("No se encontró el producto.")
            continue

        if producto_encontrado["estado"] != "activo":
            print("No se puede vender un producto inactivo.")
            continue

        try:
            cantidad = int(input("Ingrese la cantidad: "))

            if cantidad <= 0:
                print("Error: la cantidad debe ser mayor que cero.")
                continue

        except ValueError:
            print("Error: debe ingresar una cantidad entera válida.")
            continue

        cantidad_anterior = 0

        for detalle in detalles:
            if detalle["codigo"] == producto_encontrado["codigo"]:
                cantidad_anterior += detalle["cantidad"]

        disponible = producto_encontrado["existencias"] - cantidad_anterior

        if cantidad > disponible:
            print("Error: no hay existencias suficientes.")
            print("Existencias disponibles:", disponible)
            continue

        precio = producto_encontrado["precio"]
        subtotal = precio * cantidad

        detalle_venta = {
            "codigo": producto_encontrado["codigo"],
            "nombre": producto_encontrado["nombre"],
            "precio": precio,
            "cantidad": cantidad,
            "subtotal": round(subtotal, 2)
        }

        detalles.append(detalle_venta)

        print("Producto agregado a la venta.")

    if len(detalles) == 0:
        print("No se registró ningún producto. Venta cancelada.")
        return

    subtotal_venta = sum(
        detalle["subtotal"] for detalle in detalles
    )

    impuesto = round(subtotal_venta * IVA, 2)
    total = round(subtotal_venta + impuesto, 2)

    print("\n===== RESUMEN DE LA VENTA =====")

    for detalle in detalles:
        print(
            detalle["nombre"],
            "| Cantidad:", detalle["cantidad"],
            "| Subtotal: Q", detalle["subtotal"]
        )

    print("Subtotal: Q", round(subtotal_venta, 2))
    print("IVA (12%): Q", impuesto)
    print("TOTAL: Q", total)

    confirmar = input(
        "¿Desea confirmar la venta? (S/N): "
    ).strip().lower()

    if confirmar != "s":
        print("Venta cancelada. No se modificó el inventario.")
        return

    numero = generar_numero_venta(ventas)

    nueva_venta = {
        "numero": numero,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "detalles": detalles,
        "subtotal": round(subtotal_venta, 2),
        "iva": impuesto,
        "total": total,
        "estado": "confirmada"
    }

    nuevos_movimientos = []

    for detalle in detalles:

        for producto in productos:

            if producto["codigo"] == detalle["codigo"]:

                producto["existencias"] -= detalle["cantidad"]

                nuevos_movimientos.append({
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "codigo_producto": producto["codigo"],
                    "tipo": "salida",
                    "cantidad": detalle["cantidad"],
                    "descripcion": "Salida por venta " + numero
                })

                break

    ventas.append(nueva_venta)
    movimientos.extend(nuevos_movimientos)

    try:
        guardar_cambios_venta(productos, ventas, movimientos)

    except Exception as error:
        print("Error al guardar la venta:", error)
        print("Revise los archivos antes de continuar.")
        return

    print("\nVenta registrada correctamente.")
    print("Número de venta:", numero)
    print("Total cobrado: Q", total)

def mostrar_ventas():

    ventas = leer_archivo("ventas.json")

    if len(ventas) == 0:
        print("No hay ventas registradas.")
        return

    print("\n===== HISTORIAL DE VENTAS =====")

    for venta in ventas:

        print("------------------------------")
        print("Número:", venta["numero"])
        print("Fecha:", venta["fecha"])
        print("Estado:", venta["estado"])
        print("Subtotal: Q", venta["subtotal"])
        print("IVA: Q", venta["iva"])
        print("Total: Q", venta["total"])

        print("Productos:")

        for detalle in venta["detalles"]:
            print(
                detalle["nombre"],
                "| Cantidad:", detalle["cantidad"],
                "| Subtotal: Q", detalle["subtotal"]
            )
def anular_venta():

    ventas = leer_archivo("ventas.json")
    productos = leer_archivo("productos.json")
    movimientos = leer_archivo("inventario.json")

    numero = input(
        "Ingrese el número de la venta que desea anular: "
    ).strip()

    if numero == "":
        print("Error: debe ingresar el número de venta.")
        return

    venta_encontrada = None

    for venta in ventas:
        if venta["numero"].lower() == numero.lower():
            venta_encontrada = venta
            break

    if venta_encontrada is None:
        print("No se encontró la venta.")
        return

    if venta_encontrada["estado"] == "anulada":
        print("Esta venta ya se encuentra anulada.")
        return

    confirmar = input(
        "¿Está seguro de anular esta venta? (S/N): "
    ).strip().lower()

    if confirmar != "s":
        print("Anulación cancelada.")
        return

    # Verificar que todos los productos de la venta existan
    for detalle in venta_encontrada["detalles"]:

        producto_existe = False

        for producto in productos:
            if producto["codigo"] == detalle["codigo"]:
                producto_existe = True
                break

        if not producto_existe:
            print(
                "Error: no se encontró el producto",
                detalle["codigo"]
            )
            print("No se puede completar la anulación.")
            return

    movimientos_nuevos = []

    # Devolver las existencias de cada producto
    for detalle in venta_encontrada["detalles"]:

        for producto in productos:

            if producto["codigo"] == detalle["codigo"]:

                producto["existencias"] += detalle["cantidad"]

                movimientos_nuevos.append({
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "codigo_producto": producto["codigo"],
                    "tipo": "entrada",
                    "cantidad": detalle["cantidad"],
                    "descripcion": "Devolución por anulación " + numero
                })

                break

    venta_encontrada["estado"] = "anulada"

    movimientos.extend(movimientos_nuevos)

    try:
        guardar_cambios_venta(productos, ventas, movimientos)

    except Exception as error:
        print("Error al anular la venta:", error)
        print("Revise los archivos antes de continuar.")
        return

    print("Venta anulada correctamente.")
    print("Las existencias fueron devueltas al inventario.")

def menu_ventas():

    while True:

        print("\n===== GESTIÓN DE VENTAS =====")
        print("1. Registrar venta")
        print("2. Mostrar ventas")
        print("3. Anular venta")
        print("4. Regresar al menú principal")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                registrar_venta()

            elif opcion == 2:
                mostrar_ventas()

            elif opcion == 3:
                anular_venta()

            elif opcion == 4:
                print("Regresando al menú principal...")
                break

            else:
                print("Error: seleccione una opción del 1 al 4.")

        except ValueError:
            print("Error: debe ingresar un número válido.")
            