# PLANIFICACIÓN DEL PROYECTO: TEKNO COMERCIAL

## 1. Información general

- **Nombre del proyecto:** Tekno comercial.
- **Tipo de proyecto:** Sistema de gestión comercial.
- **Integrantes:** Dos integrantes.
- **Modalidad de trabajo:** Desarrollo en equipo.
- **Lenguaje de programación:** Python.
- **Nivel de programación:** Principiante.
- **Entorno de desarrollo:** Visual Studio Code (VS Code).
- **Versión de Python:** Python 3.14.7.
- **Sistema operativo:** Windows.
- **Almacenamiento de datos previsto:** Archivos JSON.
- **Herramienta para diagramas:** diagrams.net.
- **Control de versiones y publicación:** Git y GitHub.
- **Estado actual:** Fase de planificación y organización.

## 2. Descripción del proyecto

Tekno comercial será un sistema de gestión comercial diseñado para ayudar a una pequeña empresa a administrar sus productos, controlar las existencias del inventario, registrar las ventas y consultar información sobre las operaciones realizadas.

El sistema contará con un menú principal desde el cual se podrá acceder a los diferentes módulos. La información se almacenará en archivos para permitir su consulta posterior, incluso después de cerrar el programa.

El proyecto se desarrollará utilizando Python y Visual Studio Code, procurando que el código sea claro, organizado y comprensible.
## 3. Objetivo general

Desarrollar un sistema de gestión comercial en Python que permita administrar productos, registrar ventas, controlar el inventario, almacenar información en archivos y generar reportes estadísticos a partir de los datos registrados.

## 4. Objetivos específicos

1. Crear un menú principal que permita acceder a todos los módulos del sistema.
2. Registrar, consultar, modificar y desactivar productos.
3. Validar los códigos, precios y cantidades de los productos.
4. Registrar ventas, calcular subtotales, aplicar el IVA del 12 % y obtener el total de cada operación.
5. Actualizar las existencias del inventario después de cada venta.
6. Registrar entradas de inventario y consultar el historial de movimientos.
7. Identificar los productos cuyas existencias sean iguales o inferiores al stock mínimo.
8. Almacenar y recuperar información mediante archivos.
9. Generar reportes de productos, ventas, inventario e indicadores estadísticos.
10. Realizar pruebas para verificar el funcionamiento del sistema y documentar sus resultados.
11. Elaborar diagramas de flujo, un manual técnico y un manual de usuario.
12. Organizar y publicar el proyecto en GitHub, manteniendo evidencia del desarrollo.

## 5. Alcance del proyecto

El proyecto Tekno comercial comprenderá el desarrollo de un sistema de gestión comercial utilizando el lenguaje de programación Python.

El sistema incluirá las siguientes funcionalidades:

1. **Gestión de empleados:** registrar empleados, consultar información, buscar empleados y modificar salarios.
2. **Gestión de productos:** registrar productos, consultar información, buscar productos y actualizar precios y existencias.
3. **Gestión de ventas:** seleccionar productos, registrar cantidades, calcular subtotales, aplicar el IVA del 12 % y obtener el total de las ventas.
4. **Control de inventario:** actualizar las existencias después de cada venta, registrar movimientos y consultar los niveles de stock.
5. **Generación de reportes:** obtener información sobre productos, inventario, ventas y empleados mediante consultas y cálculos estadísticos.
6. **Almacenamiento de información:** utilizar archivos JSON para guardar y recuperar los datos del sistema.
7. **Documentación:** elaborar un manual técnico, un manual de usuario y diagramas que expliquen el funcionamiento del sistema.
8. **Pruebas:** verificar el funcionamiento de los módulos y documentar los resultados obtenidos.

El desarrollo será realizado por dos integrantes, quienes colaborarán en la planificación, programación, pruebas y documentación del proyecto.

El código fuente y los archivos del proyecto se organizarán mediante Visual Studio Code y se utilizará GitHub como plataforma para almacenar y entregar el repositorio final.

### 5.1. Gestión de productos

Permitirá registrar productos, consultarlos por código, mostrar el listado general, modificar su información y desactivarlos cuando ya no estén disponibles para la venta.

### 5.2. Registro de ventas
El módulo permitirá registrar las ventas realizadas en el sistema mediante la selección de productos y sus respectivas cantidades.

El sistema verificará que exista suficiente inventario antes de confirmar cada operación. Posteriormente, calculará automáticamente el subtotal de cada producto, el subtotal general, el IVA del 12 % y el total que deberá pagar el cliente.

Una vez confirmada la venta, las existencias de los productos se actualizarán automáticamente. Además, la información de cada operación se almacenará en archivos JSON para permitir consultas posteriores y generar reportes.

### 5.3. Control de inventarios

El módulo permitirá administrar las existencias de los productos registrados en el sistema. Se podrán consultar las cantidades disponibles, actualizar las existencias y registrar las entradas y salidas de productos.

El sistema actualizará automáticamente el inventario después de cada venta confirmada. También permitirá identificar los productos cuyas existencias sean iguales o inferiores al stock mínimo establecido, con el propósito de facilitar el control y la reposición de mercancía.

Además, se conservará un historial de los movimientos de inventario para facilitar las consultas y la elaboración de reportes.

### 5.4. Reportes y estadísticas

El módulo permitirá generar reportes sobre la información almacenada en el sistema, facilitando el análisis de las operaciones comerciales.

Se podrán consultar las existencias máximas y mínimas de los productos, identificar los productos más vendidos, conocer el valor de las ventas más altas y calcular el promedio de ventas realizadas.

También permitirá consultar información relacionada con los empleados, como los salarios más altos y el promedio salarial, además de mostrar el total de ventas acumuladas y la cantidad de productos registrados.

Los reportes se generarán a partir de los datos almacenados en archivos JSON, permitiendo obtener información organizada para facilitar la supervisión y la toma de decisiones comerciales.

### 5.5. Gestión de archivos

Permitirá almacenar, consultar y recuperar la información necesaria para el funcionamiento del sistema.

El programa será inicialmente una aplicación de consola. No incluirá una interfaz gráfica, conexión con bancos, pagos electrónicos ni una tienda en línea, salvo que posteriormente se solicite como ampliación.

El sistema utilizará archivos JSON para almacenar la información de empleados, productos, ventas y movimientos de inventario. Estos archivos permitirán conservar los datos entre ejecuciones del programa, consultar registros anteriores y actualizar la información cuando sea necesario.

## 6. Herramientas y tecnologías

Para desarrollar el proyecto se utilizarán las siguientes herramientas:

- **Python:** lenguaje de programación utilizado para desarrollar la lógica del sistema.
- **Visual Studio Code:** editor donde se organizarán, escribirán y ejecutarán los archivos del proyecto.
- **Archivos JSON:** formato previsto para almacenar y recuperar los datos.
- **diagrams.net:** herramienta para elaborar los diagramas de flujo.
- **Git:** herramienta para controlar las versiones y registrar los cambios realizados.
- **GitHub:** plataforma para alojar el repositorio, compartir el proyecto y documentar las aportaciones de los integrantes.

El proyecto será desarrollado por dos integrantes, quienes utilizarán las herramientas mencionadas para organizar el trabajo, desarrollar los módulos del sistema, realizar pruebas y mantener actualizada la documentación. GitHub será utilizado para compartir los avances y conservar el repositorio del proyecto, permitiendo que ambos integrantes colaboren en su desarrollo.

## 7. Organización del trabajo

El proyecto será desarrollado por dos integrantes, quienes participarán en las diferentes etapas de planificación, análisis, diseño, programación, pruebas y documentación.

El trabajo se realizará de manera coordinada y progresiva, procurando que ambos integrantes comprendan el funcionamiento general del sistema y puedan colaborar en las diferentes actividades.

Se establecerá una distribución inicial de responsabilidades para organizar el trabajo y facilitar el desarrollo de los módulos.

## 8. Distribución de responsabilidades

### Integrante 1

- Participar en la planificación y análisis del sistema.
- Colaborar principalmente en el desarrollo del módulo de gestión de productos.
- Colaborar en el desarrollo del módulo de registro de ventas.
- Participar en las pruebas y correcciones de los módulos.
- Contribuir a la elaboración de la documentación.

### Integrante 2

- Participar en la planificación y análisis del sistema.
- Colaborar principalmente en el desarrollo del módulo de control de inventarios.
- Colaborar en el desarrollo del módulo de reportes y estadísticas.
- Participar en las pruebas y correcciones de los módulos.
- Contribuir a la elaboración de la documentación.

### Responsabilidades compartidas

Ambos integrantes serán responsables de:

- Comprender el funcionamiento general del sistema.
- Participar en el diseño de los procesos y diagramas de flujo.
- Revisar el trabajo realizado por ambos.
- Verificar los cálculos y las validaciones.
- Colaborar en la integración de los módulos.
- Elaborar los manuales técnico y de usuario.
- Participar en las pruebas generales del sistema.
- Mantener actualizado el repositorio de GitHub.
- Preparar la presentación y demostración final.

La distribución de responsabilidades podrá modificarse según las necesidades del proyecto, procurando mantener una participación equilibrada.

## 9. Organización de las fases de desarrollo

El proyecto se desarrollará siguiendo el siguiente orden:

1. Planificación y organización del proyecto.
2. Análisis de requisitos y reglas de negocio.
3. Diseño de los procesos y elaboración de diagramas de flujo.
4. Diseño del almacenamiento y organización de los datos.
5. Preparación de la estructura principal y del menú del sistema.
6. Desarrollo del módulo de gestión de productos.
7. Desarrollo del módulo de registro de ventas.
8. Desarrollo del módulo de control de inventarios.
9. Desarrollo del módulo de reportes y estadísticas.
10. Integración de los módulos.
11. Ejecución de pruebas y corrección de errores.
12. Elaboración del manual técnico y manual de usuario.
13. Organización final del repositorio de GitHub.
14. Preparación de la presentación y demostración del sistema.

Cada fase deberá revisarse antes de avanzar a la siguiente.

## 10. Criterios generales de calidad

El sistema deberá cumplir con las siguientes condiciones:

- Presentar menús claros y comprensibles.
- Validar los datos ingresados por el usuario.
- Evitar códigos de productos duplicados.
- Impedir el registro de precios y cantidades negativos.
- Evitar ventas de productos inexistentes o sin suficiente inventario.
- Calcular correctamente los subtotales, el IVA y los totales.
- Almacenar y recuperar la información del sistema mediante archivos JSON, conservando los datos para cnsultas posteriores.
- Mostrar mensajes claros cuando ocurra un error.
- Permitir regresar al menú principal después de cada operación.
- Generar reportes basados en los datos almacenados.
- Mantener el código y la documentación organizados.
- Contar con pruebas y evidencias del funcionamiento.
- Facilitar la comprensión y el mantenimiento del programa.

## 11. Estrategia de desarrollo

## 11. Estrategia de desarrollo

El desarrollo del sistema se realizará de manera progresiva y organizada, siguiendo las fases establecidas en la planificación del proyecto.

Antes de implementar cada módulo, los integrantes deberán analizar los procesos que lo componen y documentar su objetivo, funcionamiento, entradas, procesamiento, salidas, reglas de negocio, validaciones, posibles errores y diagrama de flujo.

Posteriormente, se desarrollará cada módulo utilizando funciones, estructuras de control, ciclos, condicionales, listas y archivos JSON, según las necesidades del sistema.

Cada módulo será probado de manera individual antes de integrarlo con los demás, con el propósito de verificar su correcto funcionamiento y corregir posibles errores.

Una vez desarrollados y probados los módulos, se realizará su integración progresiva para comprobar el funcionamiento general del sistema.

Se procurará utilizar nombres comprensibles para las variables, funciones y archivos, así como comentarios cuando sean necesarios, manteniendo el código fuente organizado y fácil de comprender.

Los avances y cambios realizados por ambos integrantes se compartirán y organizarán mediante el repositorio de GitHub, donde se conservará el proyecto para su revisión y entrega final.

## 12. Consideraciones pendientes

## 12. Consideraciones pendientes

Antes de comenzar la implementación, se deberán definir y confirmar los siguientes aspectos:

- La estructura definitiva y organización de los archivos JSON que utilizará el sistema.
- El procedimiento para generar números únicos de venta.
- El formato para registrar y almacenar las fechas y horas de las operaciones.
- Las reglas para modificar o desactivar productos que tengan movimientos registrados en el sistema.
- El procedimiento para conservar y consultar el historial de ventas y movimientos de inventario.
- La organización y coordinación del trabajo entre los dos integrantes.
- La creación y configuración del repositorio de GitHub para almacenar, compartir y entregar el proyecto.
- La distribución de las tareas y el registro de las aportaciones realizadas por cada integrante.

Estos aspectos deberán definirse durante la etapa de análisis y organización, antes de implementar los módulos correspondientes, con el propósito de mantener un desarrollo ordenado y evitar inconsistencias en el funcionamiento del sistema.

## 13. Resultado esperado

## 13. Resultado esperado

Al finalizar el proyecto, se espera contar con un sistema funcional de gestión comercial desarrollado en Python, que permita administrar empleados y productos, registrar ventas, controlar inventarios y generar reportes estadísticos a partir de la información almacenada.

El proyecto será desarrollado por dos integrantes, quienes participarán en las diferentes etapas de planificación, análisis, programación, pruebas y documentación.

El proyecto deberá incluir los siguientes elementos:

- Código fuente completo y organizado.
- Archivos JSON necesarios para almacenar y consultar la información.
- Documento de análisis de los procesos.
- Diagramas de flujo de los procesos principales.
- Casos de prueba documentados.
- Capturas de pantalla que evidencien el funcionamiento del sistema.
- Manual técnico.
- Manual de usuario.
- Repositorio público de GitHub con el proyecto completo.
- Historial de cambios y evidencias de la participación de ambos integrantes.

El sistema deberá poder descargarse y ejecutarse en otra computadora siguiendo las instrucciones correspondientes, sin depender de archivos almacenados únicamente en los equipos de los integrantes.

El resultado final deberá cumplir con los requerimientos establecidos en los lineamientos del proyecto y permitir que el docente compruebe su funcionamiento mediante la descarga del repositorio de GitHub y la ejecución del programa.