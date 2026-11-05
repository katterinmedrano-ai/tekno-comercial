from archivos import leer_archivo, guardar_archivo

def registrar_empleado():

    empleados = leer_archivo("empleados.json")

    codigo = input("Ingrese el código del empleado: ").strip()

    if codigo == "":
        print("Error: el código no puede estar vacío.")
        return

    for empleado in empleados:
        if empleado["codigo"].lower() == codigo.lower():
            print("Error: el código ya está registrado.")
            return

    nombre = input("Ingrese el nombre del empleado: ").strip()

    if nombre == "":
        print("Error: el nombre no puede estar vacío.")
        return

    try:
        salario = float(input("Ingrese el salario: "))

        if salario < 0:
            print("Error: el salario no puede ser negativo.")
            return

    except ValueError:
        print("Error: debe ingresar un salario válido.")
        return

    nuevo_empleado = {
        "codigo": codigo,
        "nombre": nombre,
        "salario": salario,
        "estado": "activo"
    }

    empleados.append(nuevo_empleado)

    guardar_archivo("empleados.json", empleados)

    print("Empleado registrado correctamente.")
   
def mostrar_empleados():

    empleados = leer_archivo("empleados.json")

    if len(empleados) == 0:
        print("No hay empleados registrados.")
        return

    print("\n===== LISTA DE EMPLEADOS =====")

    for empleado in empleados:

        print("------------------------------")
        print("Código:", empleado["codigo"])
        print("Nombre:", empleado["nombre"])
        print("Salario:", empleado["salario"])
        print("Estado:", empleado["estado"])

    print("------------------------------")

def buscar_empleado():

    empleados = leer_archivo("empleados.json")

    busqueda = input("Ingrese el código o nombre del empleado: ").strip()

    if busqueda == "":
        print("Error: debe ingresar un código o nombre.")
        return

    encontrado = False

    for empleado in empleados:

        if (empleado["codigo"].lower() == busqueda.lower()
                or empleado["nombre"].lower() == busqueda.lower()):

            print("\n===== EMPLEADO ENCONTRADO =====")
            print("Código:", empleado["codigo"])
            print("Nombre:", empleado["nombre"])
            print("Salario:", empleado["salario"])
            print("Estado:", empleado["estado"])

            encontrado = True

    if encontrado == False:
        print("No se encontró ningún empleado.")

def modificar_salario():

    empleados = leer_archivo("empleados.json")

    codigo = input("Ingrese el código del empleado: ").strip()

    if codigo == "":
        print("Error: debe ingresar un código.")
        return

    for empleado in empleados:

        if empleado["codigo"].lower() == codigo.lower():

            if empleado["estado"] != "activo":
                print("No se puede modificar el salario de un empleado inactivo.")
                return

            print("Empleado:", empleado["nombre"])
            print("Salario actual:", empleado["salario"])

            try:
                nuevo_salario = float(input("Ingrese el nuevo salario: "))

                if nuevo_salario < 0:
                    print("Error: el salario no puede ser negativo.")
                    return

            except ValueError:
                print("Error: debe ingresar un salario válido.")
                return

            empleado["salario"] = nuevo_salario

            guardar_archivo("empleados.json", empleados)

            print("Salario modificado correctamente.")
            return

    print("No se encontró ningún empleado con ese código.")
def desactivar_empleado():

    empleados = leer_archivo("empleados.json")

    codigo = input("Ingrese el código del empleado: ").strip()

    # Validar que el código no esté vacío
    if codigo == "":
        print("Error: debe ingresar un código.")
        return

    for empleado in empleados:

        if empleado["codigo"].lower() == codigo.lower():

            if empleado["estado"] == "inactivo":
                print("El empleado ya se encuentra inactivo.")
                return

            empleado["estado"] = "inactivo"

            guardar_archivo("empleados.json", empleados)

            print("Empleado desactivado correctamente.")
            return

    print("No se encontró ningún empleado con ese código.")
def reactivar_empleado():

    empleados = leer_archivo("empleados.json")

    codigo = input("Ingrese el código del empleado: ").strip()

    if codigo == "":
        print("Error: debe ingresar un código.")
        return

    for empleado in empleados:

        if empleado["codigo"].lower() == codigo.lower():

            if empleado["estado"] == "activo":
                print("El empleado ya se encuentra activo.")
                return

            if (empleado["nombre"].strip() == ""
        or not isinstance(empleado["salario"], (int, float))
        or empleado["salario"] < 0):

                print("Error: los datos del empleado no son válidos.")
                print("No se puede reactivar el empleado.")
                return

            empleado["estado"] = "activo"

            guardar_archivo("empleados.json", empleados)

            print("Empleado reactivado correctamente.")
            return

    print("No se encontró ningún empleado con ese código.")

def promedio_salarios():

    empleados = leer_archivo("empleados.json")

    salarios = []

    for empleado in empleados:

        if empleado["estado"] == "activo":
            salarios.append(empleado["salario"])

    if len(salarios) == 0:
        print("No hay empleados activos para calcular el promedio.")
        return

    promedio = sum(salarios) / len(salarios)

    print("\n===== PROMEDIO DE SALARIOS =====")
    print("Cantidad de empleados activos:", len(salarios))
    print("Salario promedio: Q", round(promedio, 2))
    