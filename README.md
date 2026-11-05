# TEKNO COMERCIAL

## Descripción del proyecto

Tekno Comercial es un sistema de gestión empresarial desarrollado en Python para facilitar la administración de un pequeño negocio.

Permite gestionar empleados, productos, inventario, ventas y reportes mediante un menú principal interactivo.

El sistema utiliza archivos JSON para almacenar la información de forma persistente.

## Objetivo general

Desarrollar un sistema que permita organizar y controlar las operaciones principales de un pequeño negocio, facilitando el manejo de sus registros y la consulta de información.

## Módulos del sistema

### 1. Gestión de empleados
- Registrar empleados.
- Consultar y buscar empleados.
- Modificar salarios.
- Desactivar y reactivar empleados.
- Consultar el promedio de salarios.

### 2. Gestión de productos
- Registrar productos.
- Mostrar y buscar productos.
- Modificar información de productos.
- Desactivar y reactivar productos.

### 3. Gestión de inventario
- Consultar existencias.
- Registrar entradas y salidas manuales.
- Consultar el historial de movimientos.

### 4. Gestión de ventas
- Registrar ventas con varios productos.
- Calcular subtotales, IVA del 12 % y total.
- Consultar el historial de ventas.
- Anular ventas y registrar la devolución de existencias.

### 5. Reportes
- Consultar productos registrados.
- Identificar productos con bajo stock.
- Calcular el valor del inventario.
- Consultar estadísticas de ventas.
- Consultar información salarial de empleados.

## Tecnologías utilizadas

- Python.
- Visual Studio Code.
- Archivos JSON para el almacenamiento de información.
- Git y GitHub para el control de versiones y publicación del proyecto.

## Estructura del proyecto

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

## Requisitos para ejecutar el sistema

- Tener Python instalado.
- Contar con Visual Studio Code u otro editor compatible.
- Descargar o clonar el repositorio del proyecto.

## Ejecución del programa

Desde la carpeta principal del proyecto, ejecutar en la terminal:

```bash
python src/main.py
```

## Almacenamiento de información

Los datos del sistema se almacenan en archivos JSON ubicados en la carpeta `data`.

Los archivos utilizados son:

- `productos.json`: almacena la información de los productos.
- `empleados.json`: almacena los registros de empleados.
- `ventas.json`: conserva el historial de ventas.
- `inventario.json`: conserva el historial de movimientos de inventario.

La carpeta `data_respaldo` contiene una copia de seguridad de los archivos de información.

## Pruebas automatizadas

El proyecto cuenta con pruebas automatizadas desarrolladas utilizando el módulo `unittest` de Python.

Para ejecutarlas, utilizar el siguiente comando desde la carpeta principal:

```bash
python -m unittest discover -s tests -v
```

**Resultado de la última ejecución:**
- Total de pruebas: 32.
- Pruebas exitosas: 32.
- Pruebas fallidas: 0.
- Errores: 0.

Durante la primera ejecución se identificaron inconvenientes en cuatro pruebas. Estos fueron revisados y corregidos, logrando posteriormente que todas las pruebas finalizaran correctamente.

Los resultados de ambas ejecuciones se encuentran documentados en `docs/pruebas/`.

## Integrantes

- Integrante 1: Katterin.
- Integrante 2: Josué.

## Estado del proyecto

La implementación de los módulos principales y las pruebas automatizadas se encuentran completadas. Actualmente se trabaja en la finalización de los diagramas, la documentación y la preparación de la entrega final del proyecto.