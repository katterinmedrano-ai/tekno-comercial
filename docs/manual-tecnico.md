# MANUAL TÉCNICO
# SISTEMA TEKNO COMERCIAL

## 1. Introducción

Tekno Comercial es un sistema de gestión empresarial desarrollado en Python. Su propósito es administrar empleados, productos, inventario, ventas y reportes de un pequeño negocio.

El sistema utiliza una estructura modular y archivos JSON para almacenar la información de forma persistente.

## 2. Tecnologías utilizadas

- **Lenguaje de programación:** Python.
- **Editor de código:** Visual Studio Code.
- **Almacenamiento:** archivos JSON.
- **Pruebas automatizadas:** módulo unittest de Python.
- **Control de versiones:** Git.
- **Repositorio de publicación:** GitHub.

## 3. Estructura del proyecto

El proyecto está organizado en las siguientes carpetas y archivos:

```text
TEKNO COMERCIAL/
├── data/
│   ├── productos.json
│   ├── empleados.json
│   ├── ventas.json
│   └── inventario.json
├── data_respaldo/
├── docs/
│   ├── analisis/
│   ├── diagramas/
│   └── pruebas/
├── evidencias/
├── src/
│   ├── archivos.py
│   ├── empleados.py
│   ├── estructuras.py
│   ├── inventario.py
│   ├── main.py
│   ├── productos.py
│   ├── reportes.py
│   └── ventas.py
├── tests/
│   ├── test_archivos.py
│   ├── test_empleados.py
│   ├── test_inventario.py
│   ├── test_productos.py
│   ├── test_reportes.py
│   └── test_ventas.py
├── manual-técnico.md
├── manual-usuario.md
├── README.md
└── .gitignore
```

## 4. Descripción de los módulos

### 4.1 archivos.py

Se encarga de la lectura y escritura de los archivos JSON.

Funciones principales:

- `validar_archivo()`: comprueba que el nombre del archivo esté permitido.
- `leer_archivo()`: obtiene los datos almacenados.
- `guardar_archivo()`: guarda la información en formato JSON.

También comprueba que los datos tengan una estructura de lista y utiliza un archivo temporal antes de reemplazar el archivo original.

### 4.2 estructuras.py

Define las estructuras de datos utilizadas por el sistema mediante diccionarios.

Incluye funciones para crear:

- Productos.
- Empleados.
- Ventas.
- Movimientos de inventario.

### 4.3 empleados.py

Contiene las operaciones de gestión de empleados:

- Registro.
- Consulta.
- Búsqueda.
- Modificación salarial.
- Desactivación y reactivación.
- Cálculo del promedio de salarios.

Los empleados pueden mantenerse activos o inactivos. Los empleados inactivos no pueden recibir modificaciones salariales hasta que sean reactivados.

### 4.4 productos.py

Contiene las operaciones de gestión de productos:

- Registro.
- Consulta.
- Búsqueda.
- Modificación.
- Desactivación y reactivación.
- Consultas complementarias de productos y categorías.

Los códigos de productos son únicos y permanentes. Si un código se registra incorrectamente, el producto debe desactivarse y registrarse nuevamente con el código correcto.

### 4.5 inventario.py

Controla las existencias y los movimientos de inventario.

Permite:

- Consultar existencias.
- Registrar entradas.
- Registrar salidas.
- Consultar el historial de movimientos.

Los movimientos manuales solamente se permiten para productos activos. Cada entrada o salida actualiza las existencias y registra el movimiento correspondiente.

### 4.6 ventas.py

Administra las operaciones de venta.

Permite:

- Registrar ventas con varios productos.
- Calcular subtotales.
- Calcular el IVA del 12 %.
- Calcular el total.
- Consultar el historial.
- Anular ventas y devolver existencias.

Las ventas anuladas permanecen registradas en el historial para conservar la información de las operaciones realizadas.

### 4.7 reportes.py

Genera información estadística y administrativa sobre:

- Productos.
- Productos con bajo stock.
- Valor del inventario.
- Ventas.
- Empleados y salarios.

Los reportes de ventas excluyen las operaciones anuladas. Los reportes salariales consideran únicamente empleados activos.

### 4.8 main.py

Contiene el menú principal y conecta los diferentes módulos del sistema.

Permite acceder a las opciones de empleados, productos, inventario, ventas y reportes, además de controlar la salida del programa.

## 5. Estructuras de almacenamiento JSON

Los datos se almacenan en cuatro archivos independientes.

| Archivo | Información almacenada |
|---|---|
| productos.json | Productos y existencias actuales |
| empleados.json | Información de empleados |
| ventas.json | Historial de ventas |
| inventario.json | Historial de movimientos |

Los archivos utilizan listas de diccionarios para organizar los registros.

El archivo `productos.json` conserva las existencias actuales, mientras que `inventario.json` conserva el historial de movimientos realizados.

## 6. Reglas de validación

El sistema contempla las siguientes reglas:

- No permitir códigos duplicados.
- No modificar los códigos permanentes de productos y empleados.
- No aceptar precios iguales o menores que cero.
- No aceptar salarios negativos.
- No aceptar cantidades negativas.
- No permitir registrar entradas o salidas con cantidades iguales o menores que cero.
- No permitir movimientos manuales en productos inactivos.
- No permitir ventas de productos inactivos.
- No permitir ventas con existencias insuficientes.
- No permitir modificar el salario de empleados inactivos.
- No permitir anular una venta más de una vez.
- No permitir registrar una venta de un producto inexistente.

## 7. Reglas de las ventas

Cada venta calcula:

- Subtotal de los productos.
- IVA del 12 %.
- Total de la operación.

Cuando se confirma una venta, se actualizan las existencias y se registra el movimiento correspondiente.

Cuando se anula una venta:

- Se conserva el registro histórico.
- Se cambia su estado a anulada.
- Se devuelven las cantidades al inventario.
- Se registran los movimientos de entrada correspondientes.
- Se evita que la misma venta sea anulada nuevamente.

## 8. Persistencia y respaldo de datos

El módulo `archivos.py` centraliza la lectura y escritura de información.

Los datos se guardan en archivos JSON para conservar los registros después de finalizar la ejecución del programa.

El guardado utiliza un archivo temporal antes de reemplazar el archivo original, ayudando a evitar que una interrupción durante la escritura deje el archivo original parcialmente escrito.

La carpeta `data_respaldo` contiene una copia de seguridad de los archivos de información. Esta copia permite conservar una versión de los datos ante posibles inconvenientes.

## 9. Ejecución del sistema

Desde la carpeta principal del proyecto se ejecuta:

```bash
python src/main.py
```

Para ejecutar las pruebas automatizadas:

```bash
python -m unittest discover -s tests -v
```

## 10. Pruebas del sistema

El proyecto cuenta con pruebas automatizadas desarrolladas utilizando el módulo `unittest` de Python.

Las pruebas están organizadas de acuerdo con los módulos del sistema:

- `test_archivos.py`: pruebas de lectura, escritura y validación de archivos.
- `test_empleados.py`: pruebas de gestión de empleados.
- `test_productos.py`: pruebas de gestión de productos.
- `test_inventario.py`: pruebas de entradas, salidas y consultas de inventario.
- `test_ventas.py`: pruebas de operaciones de ventas.
- `test_reportes.py`: pruebas de generación de reportes.

**Resultados de la ejecución final:**

- Total de pruebas: 32.
- Pruebas exitosas: 32.
- Pruebas fallidas: 0.
- Errores: 0.

Durante la primera ejecución se identificaron cuatro inconvenientes en las pruebas. Después de analizar las causas y realizar las correcciones correspondientes, se ejecutaron nuevamente y todas finalizaron correctamente.

Los resultados de ambas ejecuciones se encuentran documentados en `docs/pruebas/`.

## 11. Mantenimiento

Para realizar modificaciones al sistema se recomienda:

- Mantener la separación de responsabilidades entre módulos.
- Utilizar las funciones de `archivos.py` para acceder a los JSON.
- Conservar las reglas de validación.
- Evitar modificar directamente los datos almacenados.
- Realizar copias de seguridad antes de efectuar cambios importantes en los datos.
- Ejecutar las pruebas después de realizar cambios.

## 12. Publicación del proyecto

El código fuente y la documentación se publicarán en un repositorio público de GitHub para facilitar su revisión y entrega académica.
