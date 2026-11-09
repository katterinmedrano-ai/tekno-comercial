from empleados import (
    registrar_empleado,
    mostrar_empleados,
    buscar_empleado,
    modificar_salario,
    desactivar_empleado,
    reactivar_empleado,
    promedio_salarios
)

from productos import menu_productos
from inventario import menu_inventario
from ventas import menu_ventas
from reportes import menu_reportes


# Menú del módulo de empleados
def menu_empleados():

    while True:

        print("\n===== GESTIÓN DE EMPLEADOS =====")
        print("1. Registrar empleado")
        print("2. Mostrar empleados")
        print("3. Buscar empleado")
        print("4. Modificar salario")
        print("5. Desactivar empleado")
        print("6. Reactivar empleado")
        print("7. Promedio de salarios")
        print("8. Regresar al menú principal")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                registrar_empleado()

            elif opcion == 2:
                mostrar_empleados()

            elif opcion == 3:
                buscar_empleado()

            elif opcion == 4:
                modificar_salario()

            elif opcion == 5:
                desactivar_empleado()

            elif opcion == 6:
                reactivar_empleado()

            elif opcion == 7:
                promedio_salarios()

            elif opcion == 8:
                print("Regresando al menú principal...")
                break

            else:
                print("Error: seleccione una opción del 1 al 8.")

        except ValueError:
            print("Error: debe ingresar un número válido.")


# Menú principal del sistema
def menu_principal():

    while True:

        print("\n===================================")
        print("          TEKNO COMERCIAL")
        print("=====================================")
        print("1. Gestión de empleados")
        print("2. Gestión de productos")
        print("3. Gestión de inventario")
        print("4. Gestión de ventas")
        print("5. Reportes")
        print("6. Salir")
        print("===================================")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                menu_empleados()

            elif opcion == 2:
                menu_productos()

            elif opcion == 3:
                menu_inventario()

            elif opcion == 4:
                menu_ventas()

            elif opcion == 5:
                menu_reportes()

            elif opcion == 6:
                print("\nGracias por utilizar Tekno Comercial.")
                print("Programa finalizado.")
                break

            else:
                print("Error: seleccione una opción del 1 al 6.")

        except ValueError:
            print("Error: debe ingresar un número válido.")


if __name__ == "__main__":
    menu_principal()
    
