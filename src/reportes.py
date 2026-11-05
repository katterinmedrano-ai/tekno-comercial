from archivos import leer_archivo


def reporte_productos():

    productos = leer_archivo("productos.json")

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    print("\n===== REPORTE DE PRODUCTOS =====")

    for producto in productos:

        print("------------------------------")
        print("Código:", producto["codigo"])
        print("Nombre:", producto["nombre"])
        print("Categoría:", producto["categoria"])
        print("Precio: Q", producto["precio"])
        print("Existencias:", producto["existencias"])
        print("Existencias mínimas:", producto["existencia_minima"])
        print("Estado:", producto["estado"])


def reporte_bajo_stock():

    productos = leer_archivo("productos.json")

    encontrados = False

    print("\n===== REPORTE DE BAJO STOCK =====")

    for producto in productos:

        if (producto["estado"] == "activo"
                and producto["existencias"] <= producto["existencia_minima"]):

            print("------------------------------")
            print("Código:", producto["codigo"])
            print("Nombre:", producto["nombre"])
            print("Existencias actuales:", producto["existencias"])
            print("Existencias mínimas:", producto["existencia_minima"])

            encontrados = True

    if not encontrados:
        print("No hay productos con existencias bajas.")


def reporte_valor_inventario():

    productos = leer_archivo("productos.json")

    valor_total = 0

    for producto in productos:
        valor_total += producto["precio"] * producto["existencias"]

    print("\n===== VALOR DEL INVENTARIO =====")
    print("Valor total: Q", round(valor_total, 2))


def reporte_ventas():

    ventas = leer_archivo("ventas.json")

    ventas_validas = []

    for venta in ventas:

        if venta["estado"] != "anulada":
            ventas_validas.append(venta)

    if len(ventas_validas) == 0:
        print("No hay ventas válidas registradas.")
        return

    total_ventas = 0
    productos_vendidos = {}

    for venta in ventas_validas:

        total_ventas += venta["total"]

        for detalle in venta["detalles"]:

            codigo = detalle["codigo"]

            if codigo not in productos_vendidos:
                productos_vendidos[codigo] = {
                    "nombre": detalle["nombre"],
                    "cantidad": 0
                }

            productos_vendidos[codigo]["cantidad"] += detalle["cantidad"]

    promedio = total_ventas / len(ventas_validas)

    # Encontrar el total más alto
    venta_mayor = max(
        venta["total"] for venta in ventas_validas
    )

    # Encontrar la cantidad más alta de productos vendidos
    mayor_cantidad = 0

    if len(productos_vendidos) > 0:
        mayor_cantidad = max(
            producto["cantidad"]
            for producto in productos_vendidos.values()
        )

    print("\n===== REPORTE DE VENTAS =====")
    print("Cantidad de ventas válidas:", len(ventas_validas))
    print("Ingresos totales: Q", round(total_ventas, 2))
    print("Promedio por venta: Q", round(promedio, 2))

    print("\n===== VENTAS MÁS ALTAS =====")

    for venta in ventas_validas:

        if venta["total"] == venta_mayor:
            print("Número:", venta["numero"])
            print("Total: Q", venta["total"])
            print("------------------------------")

    print("\n===== PRODUCTOS MÁS VENDIDOS =====")

    if mayor_cantidad > 0:

        for codigo, producto in productos_vendidos.items():

            if producto["cantidad"] == mayor_cantidad:
                print("Código:", codigo)
                print("Nombre:", producto["nombre"])
                print("Cantidad vendida:", producto["cantidad"])
                print("------------------------------")

    else:
        print("No hay productos vendidos registrados.")


def reporte_empleados():

    empleados = leer_archivo("empleados.json")

    empleados_activos = []

    for empleado in empleados:

        if empleado["estado"] == "activo":
            empleados_activos.append(empleado)

    if len(empleados_activos) == 0:
        print("No hay empleados activos registrados.")
        return

    total_salarios = 0
    salario_mayor = empleados_activos[0]
    salario_menor = empleados_activos[0]

    for empleado in empleados_activos:

        total_salarios += empleado["salario"]

        if empleado["salario"] > salario_mayor["salario"]:
            salario_mayor = empleado

        if empleado["salario"] < salario_menor["salario"]:
            salario_menor = empleado

    promedio = total_salarios / len(empleados_activos)

    print("\n===== REPORTE DE EMPLEADOS =====")
    print("Empleados activos:", len(empleados_activos))
    print("Total de salarios: Q", round(total_salarios, 2))
    print("Promedio salarial: Q", round(promedio, 2))

    print("\nSalario más alto:")
    print(salario_mayor["nombre"], "- Q", salario_mayor["salario"])

    print("\nSalario más bajo:")
    print(salario_menor["nombre"], "- Q", salario_menor["salario"])


def menu_reportes():

    while True:

        print("\n===== REPORTES DEL SISTEMA =====")
        print("1. Reporte de productos")
        print("2. Reporte de productos con bajo stock")
        print("3. Valor total del inventario")
        print("4. Reporte de ventas")
        print("5. Reporte de empleados")
        print("6. Regresar al menú principal")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                reporte_productos()

            elif opcion == 2:
                reporte_bajo_stock()

            elif opcion == 3:
                reporte_valor_inventario()

            elif opcion == 4:
                reporte_ventas()

            elif opcion == 5:
                reporte_empleados()

            elif opcion == 6:
                print("Regresando al menú principal...")
                break

            else:
                print("Error: seleccione una opción del 1 al 6.")

        except ValueError:
            print("Error: debe ingresar un número válido.")
            