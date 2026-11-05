# Crear la estructura de un producto
def crear_producto(codigo, nombre, categoria, precio,
                   existencias, existencia_minima):

    return {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "existencias": existencias,
        "existencia_minima": existencia_minima,
        "estado": "activo"
    }


# Crear la estructura de un empleado
def crear_empleado(codigo, nombre, salario):

    return {
        "codigo": codigo,
        "nombre": nombre,
        "salario": salario,
        "estado": "activo"
    }


# Crear la estructura de una venta
def crear_venta(numero, fecha, detalles, subtotal, iva, total):

    return {
        "numero": numero,
        "fecha": fecha,
        "detalles": detalles,
        "subtotal": subtotal,
        "iva": iva,
        "total": total,
        "estado": "confirmada"
    }


# Crear la estructura de un movimiento de inventario
def crear_movimiento(codigo, tipo, cantidad, descripcion, fecha):

    return {
        "fecha": fecha,
        "codigo_producto": codigo,
        "tipo": tipo,
        "cantidad": cantidad,
        "descripcion": descripcion
    }
