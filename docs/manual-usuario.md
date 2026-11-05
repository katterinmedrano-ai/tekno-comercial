# MANUAL DE USUARIO
# SISTEMA TEKNO COMERCIAL

## 1. Introducción

Tekno Comercial es un sistema desarrollado en Python para facilitar la administración de un pequeño negocio. Permite gestionar empleados, productos, inventario, ventas y reportes mediante un menú principal.

Este manual explica cómo utilizar las diferentes opciones del sistema.

## 2. Requisitos para utilizar el sistema

Para ejecutar Tekno Comercial se necesita:

- Tener Python instalado.
- Contar con Visual Studio Code u otro editor compatible.
- Tener la carpeta completa del proyecto.
- Mantener la carpeta `data` y sus archivos JSON.

## 3. Inicio del sistema

1. Abrir la carpeta del proyecto en Visual Studio Code.
2. Abrir la terminal.
3. Ejecutar el siguiente comando:

```bash
python src/main.py
```

4. El sistema mostrará el menú principal.

## 4. Menú principal

El menú principal contiene las siguientes opciones:

1. Gestión de empleados.
2. Gestión de productos.
3. Gestión de inventario.
4. Gestión de ventas.
5. Reportes.
6. Salir.

Para ingresar a un módulo, escribir el número correspondiente y presionar Enter.

Si se introduce una opción incorrecta, el sistema mostrará un mensaje de error y volverá a solicitar una opción válida.

## 5. Gestión de empleados

Este módulo permite administrar los registros de los empleados.

Sus opciones son:

- **Registrar empleado:** permite ingresar el código, nombre y salario.
- **Mostrar empleados:** presenta los empleados registrados.
- **Buscar empleado:** permite localizar un empleado mediante su código o nombre.
- **Modificar salario:** permite actualizar el salario de un empleado activo.
- **Desactivar empleado:** cambia su estado a inactivo.
- **Reactivar empleado:** permite habilitar nuevamente a un empleado inactivo.
- **Promedio de salarios:** calcula el promedio salarial de los empleados activos.

Los códigos de los empleados son únicos y no pueden modificarse después del registro.

Los empleados inactivos no pueden recibir modificaciones salariales hasta que sean reactivados. Al reactivar un empleado, se conservan su código y sus datos anteriores.

## 6. Gestión de productos

Este módulo permite administrar los productos del negocio.

Sus opciones son:

- **Registrar producto:** permite ingresar código, nombre, categoría, precio, existencias y existencia mínima.
- **Mostrar productos:** presenta los productos registrados.
- **Buscar producto:** permite localizar un producto mediante su código o nombre.
- **Modificar producto:** permite actualizar la información autorizada del producto.
- **Desactivar producto:** cambia su estado a inactivo.
- **Reactivar producto:** permite habilitar nuevamente un producto.

Los códigos de los productos son únicos y permanentes. Si se registra un código incorrecto, se debe desactivar el registro y crear uno nuevo con el código correcto.

Al reactivar un producto se conserva su código original y se valida que sus datos sean correctos.

## 7. Gestión de inventario

Este módulo permite consultar y controlar las existencias.

Sus opciones son:

- **Consultar inventario:** muestra las existencias actuales y mínimas.
- **Registrar entrada:** aumenta las existencias de un producto activo.
- **Registrar salida:** disminuye las existencias de un producto activo, siempre que haya cantidad suficiente.
- **Mostrar movimientos:** presenta el historial de entradas y salidas.

Los movimientos manuales no están permitidos para productos inactivos.

Cada movimiento registrado actualiza las existencias y queda guardado en el historial.

## 8. Gestión de ventas

Este módulo permite registrar, consultar y anular ventas.

### Registro de ventas

1. Ingresar al módulo de ventas.
2. Seleccionar la opción de registrar venta.
3. Introducir el código del producto.
4. Indicar la cantidad.
5. Agregar otros productos si es necesario.
6. Escribir `FIN` cuando se hayan agregado todos los productos.
7. Revisar el resumen de la venta.
8. Confirmar la operación escribiendo `S` cuando el sistema lo solicite.

El sistema calcula automáticamente el subtotal, el IVA del 12 % y el total.

Solo se pueden vender productos activos y con existencias suficientes.

### Anulación de ventas

1. Ingresar a la opción de anular venta.
2. Introducir el número de la venta.
3. Revisar la información de la operación.
4. Confirmar la anulación cuando el sistema lo solicite.

La venta permanece registrada en el historial con estado anulada. Las existencias correspondientes se devuelven al inventario y se registra el movimiento de entrada correspondiente.

Una venta no puede anularse más de una vez.

## 9. Reportes

El módulo de reportes permite consultar información general del negocio.

Incluye:

- Reporte de productos.
- Reporte de productos con bajo stock.
- Valor total del inventario.
- Reporte de ventas.
- Reporte de empleados.

Las estadísticas de ventas no incluyen las ventas anuladas.

El reporte de productos con bajo stock considera los productos activos que tienen existencias iguales o inferiores a su cantidad mínima.

El valor total del inventario considera todos los productos registrados, incluidos los inactivos.

Los reportes salariales consideran únicamente empleados activos.

## 10. Almacenamiento de información

El sistema utiliza archivos JSON ubicados en la carpeta `data`:

- `productos.json`: almacena los productos y sus existencias actuales.
- `empleados.json`: almacena la información de los empleados.
- `ventas.json`: conserva el historial de ventas y sus estados.
- `inventario.json`: conserva el historial de movimientos de inventario.

Es importante no eliminar ni modificar manualmente estos archivos mientras se utiliza el sistema.

La carpeta `data_respaldo` contiene una copia de seguridad de los archivos de información. Se recomienda conservarla y actualizarla periódicamente cuando existan cambios importantes en los registros.

## 11. Finalización del sistema

Para salir, seleccionar la opción 6 del menú principal.

El sistema mostrará un mensaje de finalización y terminará la ejecución.

## 12. Recomendaciones

- Introducir correctamente los códigos y cantidades.
- Verificar los datos antes de confirmar una venta.
- No eliminar los archivos JSON.
- Mantener actualizada una copia de seguridad de la carpeta `data`.
- Utilizar las opciones del sistema para modificar los registros.
- Revisar las existencias antes de registrar movimientos o ventas.
- Consultar los reportes para conocer el estado general del negocio.
