from archivos import leer_archivo, guardar_archivo

def registrar_producto():

    productos = leer_archivo("productos.json")

    codigo = input("Ingrese el código del producto: ").strip()

    if codigo == "":
        print("Error: el código no puede estar vacío.")
        return

    for producto in productos:
        if producto["codigo"].lower() == codigo.lower():
            print("Error: el código ya está registrado.")
            return

    nombre = input("Ingrese el nombre del producto: ").strip()

    if nombre == "":
        print("Error: el nombre no puede estar vacío.")
        return

    categoria = input("Ingrese la categoría del producto: ").strip()

    if categoria == "":
        print("Error: la categoría no puede estar vacía.")
        return

    try:
        precio = float(input("Ingrese el precio del producto: "))

        if precio <= 0:
            print("Error: el precio debe ser mayor que cero.")
            return

        existencias = int(input("Ingrese las existencias actuales: "))

        if existencias < 0:
            print("Error: las existencias no pueden ser negativas.")
            return

        existencia_minima = int(input("Ingrese las existencias mínimas: "))

        if existencia_minima < 0:
            print("Error: las existencias mínimas no pueden ser negativas.")
            return

    except ValueError:
        print("Error: debe ingresar valores numéricos válidos.")
        return

    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "existencias": existencias,
        "existencia_minima": existencia_minima,
        "estado": "activo"
    }

    productos.append(nuevo_producto)

    guardar_archivo("productos.json", productos)

    print("Producto registrado correctamente.")

def mostrar_productos():

    productos = leer_archivo("productos.json")

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    print("\n===== LISTA DE PRODUCTOS =====")

    for producto in productos:

        print("------------------------------")
        print("Código:", producto["codigo"])
        print("Nombre:", producto["nombre"])
        print("Categoría:", producto["categoria"])
        print("Precio: Q", producto["precio"])
        print("Existencias:", producto["existencias"])
        print("Existencias mínimas:", producto["existencia_minima"])
        print("Estado:", producto["estado"])

    print("------------------------------")
   
def buscar_producto():

    productos = leer_archivo("productos.json")

    busqueda = input("Ingrese el código o nombre del producto: ").strip()

    if busqueda == "":
        print("Error: debe ingresar un código o nombre.")
        return

    encontrado = False

    for producto in productos:

        if (producto["codigo"].lower() == busqueda.lower()
                or producto["nombre"].lower() == busqueda.lower()):

            print("\n===== PRODUCTO ENCONTRADO =====")
            print("Código:", producto["codigo"])
            print("Nombre:", producto["nombre"])
            print("Categoría:", producto["categoria"])
            print("Precio: Q", producto["precio"])
            print("Existencias:", producto["existencias"])
            print("Existencias mínimas:", producto["existencia_minima"])
            print("Estado:", producto["estado"])

            encontrado = True

    if encontrado == False:
        print("No se encontró ningún producto.") 
        
def modificar_producto():

    productos = leer_archivo("productos.json")

    codigo = input("Ingrese el código del producto que desea modificar: ").strip()

    if codigo == "":
        print("Error: debe ingresar un código.")
        return

    for producto in productos:

        if producto["codigo"].lower() == codigo.lower():

            if producto["estado"] != "activo":
                print("No se puede modificar un producto inactivo.")
                return

            print("\n===== DATOS ACTUALES DEL PRODUCTO =====")
            print("Nombre:", producto["nombre"])
            print("Categoría:", producto["categoria"])
            print("Precio: Q", producto["precio"])
            print("Existencias mínimas:", producto["existencia_minima"])

            nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()

            if nuevo_nombre == "":
                print("Error: el nombre no puede estar vacío.")
                return

            nueva_categoria = input("Ingrese la nueva categoría: ").strip()

            if nueva_categoria == "":
                print("Error: la categoría no puede estar vacía.")
                return

            try:
                nuevo_precio = float(input("Ingrese el nuevo precio: "))

                if nuevo_precio <= 0:
                    print("Error: el precio debe ser mayor que cero.")
                    return

                nueva_existencia_minima = int(
                    input("Ingrese la nueva existencia mínima: ")
                )

                if nueva_existencia_minima < 0:
                    print("Error: la existencia mínima no puede ser negativa.")
                    return

            except ValueError:
                print("Error: debe ingresar valores numéricos válidos.")
                return

            producto["nombre"] = nuevo_nombre
            producto["categoria"] = nueva_categoria
            producto["precio"] = nuevo_precio
            producto["existencia_minima"] = nueva_existencia_minima

            guardar_archivo("productos.json", productos)

            print("Producto modificado correctamente.")
            return

    print("No se encontró ningún producto con ese código.")
        
def desactivar_producto():

    productos = leer_archivo("productos.json")

    codigo = input("Ingrese el código del producto que desea desactivar: ").strip()

    if codigo == "":
        print("Error: debe ingresar un código.")
        return

    for producto in productos:

        if producto["codigo"].lower() == codigo.lower():

            if producto["estado"] == "inactivo":
                print("El producto ya se encuentra inactivo.")
                return

            producto["estado"] = "inactivo"

            guardar_archivo("productos.json", productos)

            print("Producto desactivado correctamente.")
            return

    print("No se encontró ningún producto con ese código.")
    
def reactivar_producto():

    productos = leer_archivo("productos.json")

    codigo = input("Ingrese el código del producto que desea reactivar: ").strip()

    if codigo == "":
        print("Error: debe ingresar un código.")
        return

    for producto in productos:

        if producto["codigo"].lower() == codigo.lower():

            if producto["estado"] == "activo":
                print("El producto ya se encuentra activo.")
                return

            # Validar que los datos del producto sean correctos
            if (producto["nombre"].strip() == ""
                    or producto["categoria"].strip() == ""
                    or producto["precio"] <= 0
                    or producto["existencias"] < 0
                    or producto["existencia_minima"] < 0):

                print("Error: los datos del producto no son válidos.")
                print("No se puede reactivar el producto.")
                return

            producto["estado"] = "activo"

            guardar_archivo("productos.json", productos)

            print("Producto reactivado correctamente.")
            return

    print("No se encontró ningún producto con ese código.")
   
def contar_productos():

    productos = leer_archivo("productos.json")

    total = len(productos)

    activos = 0
    inactivos = 0

    for producto in productos:

        if producto["estado"] == "activo":
            activos += 1

        elif producto["estado"] == "inactivo":
            inactivos += 1

    print("\n===== RESUMEN DE PRODUCTOS =====")
    print("Total de productos:", total)
    print("Productos activos:", activos)
    print("Productos inactivos:", inactivos)
    
def mostrar_productos_bajo_stock():

    productos = leer_archivo("productos.json")

    encontrados = False

    print("\n===== PRODUCTOS CON EXISTENCIAS BAJAS =====")

    for producto in productos:

        if (producto["estado"] == "activo"
                and producto["existencias"] <= producto["existencia_minima"]):

            print("------------------------------")
            print("Código:", producto["codigo"])
            print("Nombre:", producto["nombre"])
            print("Existencias actuales:", producto["existencias"])
            print("Existencias mínimas:", producto["existencia_minima"])

            encontrados = True

    if encontrados == False:
        print("No hay productos con existencias bajas.")
        
def valor_total_inventario():

    productos = leer_archivo("productos.json")

    valor_total = 0

    for producto in productos:

        valor_producto = producto["precio"] * producto["existencias"]

        valor_total += valor_producto

    print("\n===== VALOR TOTAL DEL INVENTARIO =====")
    print("Valor total: Q", round(valor_total, 2))
    
def producto_mas_caro():

    productos = leer_archivo("productos.json")

    productos_activos = []

    for producto in productos:

        if producto["estado"] == "activo":
            productos_activos.append(producto)

    if len(productos_activos) == 0:
        print("No hay productos activos registrados.")
        return

    producto_caro = productos_activos[0]

    for producto in productos_activos:

        if producto["precio"] > producto_caro["precio"]:
            producto_caro = producto

    print("\n===== PRODUCTO MÁS CARO =====")
    print("Código:", producto_caro["codigo"])
    print("Nombre:", producto_caro["nombre"])
    print("Precio: Q", producto_caro["precio"])
    
def producto_mas_barato():

    productos = leer_archivo("productos.json")

    productos_activos = []

    for producto in productos:

        if producto["estado"] == "activo":
            productos_activos.append(producto)

    if len(productos_activos) == 0:
        print("No hay productos activos registrados.")
        return

    producto_barato = productos_activos[0]

    for producto in productos_activos:

        if producto["precio"] < producto_barato["precio"]:
            producto_barato = producto

    print("\n===== PRODUCTO MÁS BARATO =====")
    print("Código:", producto_barato["codigo"])
    print("Nombre:", producto_barato["nombre"])
    print("Precio: Q", producto_barato["precio"])
    
def buscar_productos_por_categoria():

    productos = leer_archivo("productos.json")

    categoria = input("Ingrese la categoría que desea buscar: ").strip()

    if categoria == "":
        print("Error: debe ingresar una categoría.")
        return

    encontrados = False

    for producto in productos:

        if (producto["categoria"].lower() == categoria.lower()
                and producto["estado"] == "activo"):

            print("\n===== PRODUCTO ENCONTRADO =====")
            print("Código:", producto["codigo"])
            print("Nombre:", producto["nombre"])
            print("Categoría:", producto["categoria"])
            print("Precio: Q", producto["precio"])
            print("Existencias:", producto["existencias"])

            encontrados = True

    if encontrados == False:
        print("No se encontraron productos activos en esa categoría.")
        
def contar_productos_por_categoria():

    productos = leer_archivo("productos.json")

    categoria = input("Ingrese la categoría que desea consultar: ").strip()

    if categoria == "":
        print("Error: debe ingresar una categoría.")
        return

    cantidad = 0

    for producto in productos:

        if (producto["categoria"].lower() == categoria.lower()
                and producto["estado"] == "activo"):

            cantidad += 1

    print("\n===== CANTIDAD DE PRODUCTOS POR CATEGORÍA =====")
    print("Categoría:", categoria)
    print("Cantidad de productos:", cantidad)
    
def listar_categorias():

    productos = leer_archivo("productos.json")

    categorias = []

    for producto in productos:

        if producto["estado"] == "activo":

            if producto["categoria"] not in categorias:
                categorias.append(producto["categoria"])

    if len(categorias) == 0:
        print("No hay categorías registradas.")
        return

    print("\n===== CATEGORÍAS REGISTRADAS =====")

    for categoria in categorias:
        print("-", categoria)
       
def existe_producto(codigo):

    productos = leer_archivo("productos.json")

    for producto in productos:

        if producto["codigo"].lower() == codigo.lower():
            return True

    return False

def menu_productos():

    while True:

        print("\n===== GESTIÓN DE PRODUCTOS =====")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Desactivar producto")
        print("6. Reactivar producto")
        print("7. Regresar al menú principal")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                registrar_producto()

            elif opcion == 2:
                mostrar_productos()

            elif opcion == 3:
                buscar_producto()

            elif opcion == 4:
                modificar_producto()

            elif opcion == 5:
                desactivar_producto()

            elif opcion == 6:
                reactivar_producto()

            elif opcion == 7:
                print("Regresando al menú principal...")
                break

            else:
                print("Error: seleccione una opción del 1 al 7.")

        except ValueError:
            print("Error: debe ingresar un número válido.")
            