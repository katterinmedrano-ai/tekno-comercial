# ANÁLISIS DE REQUERIMIENTOS

## 1. Información general del sistema

- **Nombre del proyecto:** Tekno Comercial.
- **Tipo de sistema:** Sistema de gestión comercial.
- **Lenguaje de programación:** Python.
- **Entorno de desarrollo:** Visual Studio Code.
- **Versión de Python:** 3.14.7.
- **Sistema operativo:** Windows.
- **Almacenamiento de información:** Archivos JSON.
- **Número de integrantes:** 2.
- **Tipo de aplicación:** Aplicación de consola.
- **Estado del proyecto:** Análisis de requerimientos.

## 2. Descripción general del sistema

Tekno Comercial será un sistema de gestión comercial desarrollado en Python, diseñado para facilitar la administración y el control de las actividades de una pequeña empresa.

El sistema permitirá gestionar la información de los empleados, productos, ventas e inventario, además de generar reportes que faciliten la consulta y el análisis de los datos almacenados.

La aplicación funcionará mediante un menú principal desde el cual el usuario podrá ingresar a los diferentes módulos del sistema. Cada módulo contará con opciones específicas para registrar, consultar, buscar y modificar información, según corresponda.

La información se almacenará en archivos JSON, permitiendo conservar los datos aunque el programa se cierre y vuelva a ejecutarse.

El sistema contará con validaciones para evitar errores durante el ingreso y procesamiento de información, como datos vacíos, códigos duplicados, cantidades negativas o registros inexistentes.

El propósito principal de Tekno Comercial es ofrecer una herramienta organizada, sencilla y funcional que facilite las operaciones comerciales de la empresa.

## 3. Objetivo general

Desarrollar un sistema de gestión comercial utilizando el lenguaje de programación Python, que permita administrar de manera organizada la información de los empleados, productos, ventas e inventario de una pequeña empresa.

El sistema tendrá como finalidad facilitar el registro, consulta, búsqueda y modificación de datos, controlar las existencias de productos, procesar las ventas aplicando el IVA del 12 % y generar reportes estadísticos a partir de la información almacenada en archivos JSON.

Además, se busca implementar validaciones que garanticen el correcto funcionamiento del sistema, evitando registros duplicados, datos incorrectos y operaciones que no cumplan con las reglas establecidas.

## 4. Objetivos específicos

1. **Desarrollar un menú principal:** crear una interfaz de consola que permita acceder de manera organizada a los diferentes módulos del sistema y regresar al menú principal después de cada operación.

2. **Implementar la gestión de empleados:** permitir registrar, mostrar, buscar y modificar los datos generales de los empleados, así como actualizar sus salarios y consultar estadísticas salariales.

3. **Implementar la gestión de productos:** permitir registrar, consultar, listar, buscar, modificar y desactivar productos, almacenando su código, nombre, categoría, precio de venta, cantidad disponible y existencia mínima.

4. **Desarrollar el módulo de ventas:** permitir seleccionar productos, indicar cantidades, calcular subtotales, subtotal general, IVA del 12 % y total de la venta, además de actualizar automáticamente las existencias.

5. **Implementar el control de inventario:** permitir consultar existencias, registrar entradas y salidas de productos, actualizar cantidades y generar alertas cuando un producto alcance su existencia mínima.

6. **Desarrollar el módulo de reportes:** generar información sobre productos, inventario, ventas y empleados, utilizando los datos almacenados en el sistema.

7. **Implementar el almacenamiento de información:** utilizar archivos JSON para guardar y recuperar los datos de empleados, productos, ventas e inventario.

8. **Incorporar validaciones:** evitar códigos duplicados, campos obligatorios vacíos, precios o cantidades negativas, ventas superiores a las existencias y operaciones sobre registros inexistentes.

9. **Realizar pruebas del sistema:** comprobar el funcionamiento de cada módulo mediante casos normales y excepcionales, documentando los resultados obtenidos.

10. **Elaborar la documentación:** preparar diagramas de flujo, análisis de procesos, manual técnico, manual de usuario y evidencias del funcionamiento.

11. **Utilizar Git y GitHub:** mantener un repositorio público y organizado que permita registrar los avances, cambios y aportaciones de los dos integrantes.

## 5. Requerimientos funcionales

Los requerimientos funcionales describen las operaciones y características que deberá realizar el sistema Tekno Comercial para cumplir con sus objetivos.

El sistema estará organizado en los siguientes módulos:

- Gestión de empleados.
- Gestión de productos.
- Gestión de ventas.
- Control de inventario.
- Generación de reportes.
- Administración de archivos y almacenamiento de información.

Cada módulo contará con opciones específicas y validaciones para garantizar el correcto funcionamiento del sistema.

### 5.1. Módulo de gestión de empleados

El sistema deberá permitir realizar las siguientes operaciones:

1. **Registrar empleados:** ingresar el código, nombre completo, puesto y salario de cada empleado.
2. **Mostrar empleados:** visualizar la lista de empleados registrados.
3. **Buscar empleados:** localizar un empleado mediante su código.
4. **Modificar datos generales:** permitir actualizar el nombre y el puesto de un empleado.
5. **Modificar salario:** permitir actualizar el salario de un empleado registrado.
6. **Consultar salario promedio:** calcular el promedio de los salarios de todos los empleados registrados.
7. **Consultar salario más alto:** identificar al empleado que tenga el salario más elevado.

**Reglas y validaciones:**

- No permitir códigos de empleados duplicados.
- No permitir campos obligatorios vacíos.
- No permitir salarios negativos.
- Verificar que el empleado exista antes de modificar sus datos.
- Validar que el salario ingresado sea numérico.
- Guardar los registros y modificaciones en un archivo JSON.
- Informar al usuario cuando no existan empleados registrados.

### 5.2. Módulo de gestión de productos

El sistema deberá permitir administrar los productos de la empresa mediante las siguientes operaciones:

1. **Registrar productos:** ingresar el código, nombre, categoría, precio de venta, cantidad disponible y existencia mínima de cada producto.
2. **Mostrar productos:** visualizar una lista de todos los productos registrados, incluyendo sus datos principales.
3. **Buscar productos:** localizar un producto mediante su código y mostrar toda su información.
4. **Modificar productos:** permitir actualizar el nombre, categoría, precio de venta y existencia mínima de un producto.
5. **Actualizar existencias:** modificar la cantidad disponible de un producto mediante las operaciones correspondientes de inventario.
6. **Desactivar productos:** permitir desactivar productos que ya no se encuentren disponibles para la venta, conservando su información histórica.

**Reglas y validaciones:**

- No permitir códigos de productos duplicados.
- No permitir campos obligatorios vacíos.
- No permitir precios negativos o iguales a cero.
- No permitir cantidades negativas.
- Validar que los precios sean valores numéricos.
- Validar que las cantidades sean números enteros.
- Verificar que el producto exista antes de buscarlo o modificarlo.
- No permitir vender productos desactivados.
- No eliminar físicamente los productos que tengan movimientos o ventas registrados; se deberá conservar su historial.
- Guardar los registros y modificaciones en archivos JSON.
- Informar al usuario cuando no existan productos registrados.

### 5.3. Módulo de gestión de ventas

El sistema deberá permitir registrar y administrar las ventas realizadas por la empresa mediante las siguientes operaciones:

1. **Registrar ventas:** permitir seleccionar uno o varios productos registrados e indicar la cantidad que se desea vender.
2. **Validar productos:** comprobar que cada producto seleccionado exista y se encuentre activo.
3. **Validar existencias:** verificar que la cantidad solicitada esté disponible en el inventario antes de confirmar la venta.
4. **Calcular subtotales:** multiplicar el precio de cada producto por la cantidad vendida.
5. **Calcular subtotal general:** sumar los subtotales de todos los productos incluidos en la venta.
6. **Calcular IVA:** aplicar el impuesto del 12 % al subtotal general.
7. **Calcular total:** sumar el subtotal general y el IVA correspondiente.
8. **Generar número de venta:** asignar un número único y consecutivo a cada venta registrada.
9. **Guardar ventas:** almacenar el número de venta, fecha, productos, cantidades, precios, subtotales, IVA y total en un archivo JSON.
10. **Actualizar inventario:** descontar automáticamente las cantidades vendidas de las existencias de cada producto.
11. **Consultar historial de ventas:** permitir visualizar las ventas que se hayan registrado anteriormente.
12. **Cancelar una venta:** permitir cancelar una venta antes de confirmarla definitivamente, sin modificar las existencias del inventario.

**Reglas y validaciones:**

- No permitir registrar una venta sin productos.
- No permitir cantidades iguales o inferiores a cero.
- No permitir vender productos inexistentes o desactivados.
- No permitir vender cantidades superiores a las existencias disponibles.
- Validar que las cantidades ingresadas sean números enteros.
- Utilizar el precio de venta registrado para cada producto al calcular la operación.
- Calcular correctamente los subtotales, el IVA del 12 % y el total.
- No descontar productos del inventario hasta que la venta haya sido confirmada.
- No generar números de venta duplicados.
- Guardar las ventas confirmadas en un archivo JSON.
- Informar al usuario cuando no existan ventas registradas.

**Fórmulas de cálculo:**

- Subtotal por producto = Precio unitario × Cantidad.
- Subtotal general = Suma de los subtotales de los productos.
- IVA = Subtotal general × 0.12.
- Total de venta = Subtotal general + IVA.

### 5.4. Módulo de control de inventario

El sistema deberá permitir administrar y controlar las existencias de los productos de la empresa mediante las siguientes operaciones:

1. **Consultar inventario:** mostrar la lista de productos con sus cantidades disponibles, precios y existencias mínimas.
2. **Registrar entradas de productos:** permitir aumentar las existencias cuando ingresen nuevas unidades al inventario.
3. **Registrar salidas de productos:** permitir disminuir las existencias por motivos distintos a una venta, registrando la razón de la salida.
4. **Actualizar existencias:** mantener las cantidades disponibles actualizadas después de cada entrada, salida o venta confirmada.
5. **Identificar productos con bajo inventario:** detectar los productos cuyas existencias sean iguales o inferiores a la cantidad mínima establecida.
6. **Consultar historial de movimientos:** mostrar las entradas y salidas realizadas, incluyendo la fecha, código del producto, tipo de movimiento, cantidad y descripción.
7. **Consultar movimientos por producto:** permitir visualizar el historial de movimientos de un producto específico mediante su código.

**Reglas y validaciones:**

- No permitir registrar movimientos de productos inexistentes.
- No permitir cantidades iguales o inferiores a cero.
- Validar que las cantidades ingresadas sean números enteros.
- No permitir salidas superiores a las existencias disponibles.
- No permitir modificar las existencias de productos desactivados sin una operación administrativa autorizada.
- Registrar la fecha de cada movimiento.
- Diferenciar las entradas, salidas por ajustes y salidas por ventas.
- Las ventas confirmadas deberán generar automáticamente una salida de inventario.
- Mantener actualizado el historial de movimientos.
- Guardar los movimientos y las existencias en archivos JSON.
- Informar al usuario cuando no existan productos o movimientos registrados.

**Información que deberá almacenarse en cada movimiento:**

- Código del producto.
- Tipo de movimiento: entrada, salida por ajuste o salida por venta.
- Cantidad de unidades.
- Fecha del movimiento.
- Descripción o motivo del movimiento.
- Número de venta, cuando el movimiento corresponda a una venta.

### 5.5. Módulo de generación de reportes

El sistema deberá permitir generar reportes que faciliten la consulta, el análisis y el control de las actividades comerciales de la empresa.

Se deberán implementar los siguientes reportes:

**1. Reportes de productos e inventario**

- Mostrar la lista general de productos registrados.
- Identificar el producto con mayor existencia.
- Identificar el producto con menor existencia.
- Mostrar los productos que se encuentren en su existencia mínima o por debajo de ella.
- Calcular el valor total del inventario, considerando el precio de venta y las cantidades disponibles.

**2. Reportes de ventas**

- Mostrar el historial de ventas realizadas.
- Calcular el total de ingresos obtenidos por las ventas.
- Identificar el producto que ha registrado la mayor cantidad de unidades vendidas.
- Identificar la venta con el importe más alto.
- Calcular el promedio de las ventas registradas.
- Consultar las ventas correspondientes a un período determinado.

**3. Reportes de empleados**

- Mostrar la lista de empleados registrados.
- Identificar al empleado con el salario más alto.
- Calcular el salario promedio de los empleados.
- Consultar la información general de los empleados.

**Reglas y validaciones:**

- Los reportes deberán obtener información de los archivos JSON.
- Los cálculos deberán realizarse utilizando los registros almacenados.
- No se deberán generar resultados incorrectos cuando no existan datos.
- Informar al usuario cuando no haya información suficiente para generar un reporte.
- Mostrar los resultados de manera clara y ordenada.
- Utilizar los datos actualizados de los diferentes módulos.
- Los reportes no deberán modificar la información almacenada.

**Resultados esperados:**

El sistema deberá presentar información confiable que permita conocer el estado del inventario, el comportamiento de las ventas y los datos generales de los empleados.

### 5.6. Módulo de administración de archivos y almacenamiento de información

El sistema deberá contar con un mecanismo de almacenamiento mediante archivos JSON, que permita guardar, consultar y actualizar la información de los diferentes módulos de Tekno Comercial.

Se deberán implementar las siguientes operaciones:

1. **Guardar información:** almacenar los registros de empleados, productos, ventas e inventario en archivos JSON.
2. **Leer información:** recuperar los datos almacenados al iniciar el programa o cuando algún módulo los necesite.
3. **Actualizar información:** modificar los registros existentes y guardar los cambios correspondientes.
4. **Conservar información:** mantener los datos disponibles aunque el programa se cierre y vuelva a ejecutarse.
5. **Verificar archivos:** comprobar si los archivos JSON existen antes de intentar leerlos.
6. **Crear archivos iniciales:** crear los archivos necesarios cuando todavía no existan, utilizando una estructura inicial vacía.
7. **Validar información:** controlar los errores que puedan producirse cuando un archivo esté vacío, tenga un formato incorrecto o no pueda leerse.
8. **Mantener la integridad de los datos:** evitar que una operación de guardado elimine accidentalmente información existente.

**Archivos de almacenamiento propuestos:**

- `empleados.json`: almacenará la información de los empleados.
- `productos.json`: almacenará los productos registrados.
- `ventas.json`: almacenará el historial de ventas confirmadas.
- `inventario.json`: almacenará las existencias y el historial de movimientos.

**Reglas y validaciones:**

- Utilizar el formato JSON para almacenar la información.
- Mantener una estructura organizada y consistente en cada archivo.
- No sobrescribir los registros existentes al agregar información nueva.
- Comprobar que los datos recuperados tengan el formato esperado.
- Manejar adecuadamente los errores de lectura y escritura.
- Guardar los cambios después de cada operación confirmada.
- Mantener relacionados los registros de ventas y los movimientos de inventario.
- Informar al usuario cuando ocurra un problema al guardar o recuperar información.

**Resultado esperado:**

El sistema deberá permitir que los diferentes módulos compartan información y trabajen con datos almacenados de manera persistente, organizada y confiable.

## 6. Requerimientos no funcionales

Los requerimientos no funcionales establecen las características de calidad, seguridad, facilidad de uso y funcionamiento que deberá cumplir el sistema Tekno Comercial.

### 6.1. Facilidad de uso

- El sistema deberá contar con menús claros, ordenados y fáciles de comprender.
- Las opciones deberán mostrar instrucciones para orientar al usuario.
- Los mensajes de error deberán explicar qué problema ocurrió y cómo corregirlo.
- La navegación entre los módulos deberá ser sencilla.
- El usuario deberá poder regresar al menú principal sin cerrar el programa.

### 6.2. Rendimiento

- El sistema deberá ejecutar las operaciones de registro, consulta, modificación y búsqueda sin demoras innecesarias.
- Los cálculos de ventas, inventario y reportes deberán realizarse correctamente.
- El programa deberá procesar los datos almacenados sin afectar el funcionamiento de los demás módulos.

### 6.3. Seguridad e integridad de la información

- El sistema deberá validar los datos ingresados antes de almacenarlos.
- Se deberán evitar modificaciones accidentales de la información.
- Los archivos JSON deberán conservar una estructura organizada.
- Las operaciones confirmadas deberán guardarse correctamente.
- El sistema deberá manejar los errores de lectura y escritura de archivos sin provocar la pérdida accidental de información.

### 6.4. Mantenibilidad

- El código deberá estar organizado en módulos y funciones.
- Se utilizarán nombres claros para variables, funciones y archivos.
- Se incluirán comentarios cuando sean necesarios para facilitar la comprensión.
- Los módulos deberán tener responsabilidades definidas para facilitar futuras modificaciones.

### 6.5. Compatibilidad

- El sistema deberá desarrollarse utilizando Python.
- El programa deberá poder ejecutarse desde Visual Studio Code en Windows.
- Se deberá indicar la versión de Python y los pasos necesarios para ejecutar el proyecto.
- El sistema deberá poder descargarse desde GitHub y ejecutarse en otra computadora que tenga instalado Python.

### 6.6. Disponibilidad y persistencia

- La información deberá conservarse después de cerrar el programa.
- Al iniciar nuevamente el sistema, se deberán recuperar los datos almacenados.
- El programa deberá informar cuando no pueda acceder a los archivos necesarios.
- Los archivos de datos deberán mantenerse organizados dentro de la carpeta correspondiente del proyecto.

### 6.7. Organización y control de versiones

- El proyecto deberá mantener una estructura de carpetas organizada.
- El código fuente y la documentación deberán almacenarse en un repositorio público de GitHub.
- Se deberán registrar los avances mediante commits.
- Los dos integrantes deberán participar en el desarrollo y documentar sus aportaciones.
- Se deberán utilizar ramas y solicitudes de integración (Pull Requests) para organizar los cambios.

## 7. Reglas de negocio

Las reglas de negocio establecen las condiciones que deberá cumplir el sistema Tekno Comercial para garantizar que las operaciones comerciales se realicen de manera correcta y organizada.

### 7.1. Reglas para empleados

1. Cada empleado deberá tener un código único.
2. No se permitirá registrar dos empleados con el mismo código.
3. El nombre y el puesto del empleado serán datos obligatorios.
4. El salario deberá ser un valor numérico mayor o igual a cero.
5. Solamente se podrán modificar los datos de empleados que estén registrados.
6. Las modificaciones deberán guardarse en el archivo correspondiente.

### 7.2. Reglas para productos

1. Cada producto deberá tener un código único.
2. No se permitirá registrar productos con códigos duplicados.
3. Todo producto deberá contar con nombre, categoría, precio de venta, cantidad disponible y existencia mínima.
4. El precio de venta deberá ser mayor que cero.
5. Las cantidades de productos deberán ser números enteros iguales o mayores que cero.
6. Los productos desactivados no podrán utilizarse en nuevas ventas.
7. Los productos con historial de movimientos o ventas deberán conservar sus registros.

### 7.3. Reglas para ventas

1. Una venta deberá incluir al menos un producto.
2. Solamente se podrán vender productos registrados y activos.
3. La cantidad solicitada deberá ser mayor que cero.
4. No se permitirá vender más unidades de las disponibles en el inventario.
5. Cada venta confirmada deberá tener un número único y consecutivo.
6. El IVA aplicado a las ventas será del 12 %.
7. El total de la venta deberá calcularse sumando el subtotal general y el IVA.
8. Las existencias solamente se descontarán cuando la venta sea confirmada.
9. Las ventas confirmadas deberán conservarse en el historial.
10. Los precios utilizados en una venta deberán corresponder a los precios registrados al momento de realizarla.

### 7.4. Reglas para inventario

1. Las entradas de productos aumentarán las existencias.
2. Las salidas por ajustes disminuirán las existencias.
3. Las ventas confirmadas generarán automáticamente una salida de inventario.
4. No se permitirá registrar salidas superiores a las existencias disponibles.
5. Cada movimiento deberá tener una fecha, un producto, un tipo de movimiento y una cantidad.
6. Los productos deberán generar una alerta cuando sus existencias sean iguales o inferiores a su cantidad mínima.
7. Los movimientos realizados deberán conservarse en el historial.

### 7.5. Reglas para reportes

1. Los reportes deberán generarse utilizando los datos almacenados.
2. El producto más vendido se determinará según la cantidad total de unidades vendidas.
3. El producto con mayor y menor existencia se identificará según las cantidades disponibles.
4. El promedio de ventas se calculará utilizando las ventas confirmadas.
5. El valor del inventario se calculará multiplicando el precio de venta por la cantidad disponible de cada producto y sumando los resultados.
6. El salario promedio se calculará utilizando los salarios de los empleados registrados.
7. Los reportes no deberán modificar los datos almacenados.
8. Cuando no existan registros suficientes, el sistema deberá informar al usuario.

### 7.6. Reglas generales del sistema

1. El sistema deberá iniciar mostrando el menú principal.
2. Cada módulo deberá contar con opciones organizadas.
3. Después de realizar una operación, el usuario deberá poder regresar al menú correspondiente.
4. El programa deberá validar las opciones seleccionadas por el usuario.
5. Los datos deberán guardarse en archivos JSON.
6. El sistema deberá permitir salir del programa mediante una opción del menú principal.
7. Antes de finalizar, las operaciones confirmadas deberán estar guardadas correctamente.

## 8. Entradas, procesos y salidas del sistema

El sistema Tekno Comercial recibirá información del usuario, realizará operaciones de procesamiento y mostrará resultados de acuerdo con las funciones de cada módulo.

### 8.1. Módulo de gestión de empleados

**Entradas:**
- Código del empleado.
- Nombre completo.
- Puesto.
- Salario.
- Código del empleado que se desea buscar o modificar.
- Nuevos datos generales o nuevo salario.

**Procesos:**
- Validar que los campos obligatorios estén completos.
- Verificar que el código del empleado no esté registrado.
- Guardar los datos del empleado.
- Buscar empleados mediante su código.
- Modificar los datos generales o el salario.
- Calcular el salario promedio.
- Identificar al empleado con el salario más alto.

**Salidas:**
- Confirmación del registro.
- Información del empleado consultado.
- Confirmación de las modificaciones.
- Resultado del salario promedio.
- Información del empleado con el salario más alto.
- Mensajes de error cuando los datos no sean válidos.

### 8.2. Módulo de gestión de productos

**Entradas:**
- Código del producto.
- Nombre.
- Categoría.
- Precio de venta.
- Cantidad disponible.
- Existencia mínima.
- Código del producto que se desea buscar, modificar o desactivar.

**Procesos:**
- Validar los datos ingresados.
- Comprobar que el código del producto sea único.
- Registrar nuevos productos.
- Consultar y buscar productos.
- Modificar la información permitida.
- Desactivar productos.
- Guardar los cambios realizados.

**Salidas:**
- Confirmación del registro.
- Lista de productos.
- Información del producto consultado.
- Confirmación de las modificaciones o desactivaciones.
- Mensajes de validación y error.

### 8.3. Módulo de gestión de ventas

**Entradas:**
- Código del producto.
- Cantidad que se desea vender.
- Confirmación o cancelación de la venta.

**Procesos:**
- Verificar que el producto exista y esté activo.
- Comprobar que haya existencias suficientes.
- Calcular el subtotal de cada producto.
- Calcular el subtotal general.
- Calcular el IVA del 12 %.
- Calcular el total de la venta.
- Generar un número único de venta.
- Guardar la venta confirmada.
- Actualizar las existencias del inventario.
- Registrar los movimientos correspondientes.

**Salidas:**
- Detalle de los productos vendidos.
- Subtotal de cada producto.
- Subtotal general.
- IVA del 12 %.
- Total de la venta.
- Número de venta.
- Confirmación de la operación.
- Mensajes de error cuando no sea posible completar la venta.

### 8.4. Módulo de control de inventario

**Entradas:**
- Código del producto.
- Tipo de movimiento.
- Cantidad de unidades.
- Descripción o motivo del movimiento.
- Fecha del movimiento.

**Procesos:**
- Consultar las existencias disponibles.
- Validar que el producto exista.
- Registrar entradas y salidas.
- Comprobar que las salidas no superen las existencias.
- Actualizar las cantidades disponibles.
- Detectar productos con existencias iguales o inferiores al mínimo.
- Registrar el historial de movimientos.

**Salidas:**
- Existencias actualizadas.
- Confirmación del movimiento.
- Lista de productos con bajo inventario.
- Historial de entradas y salidas.
- Mensajes de error o validación.

### 8.5. Módulo de generación de reportes

**Entradas:**
- Solicitud del tipo de reporte.
- Período de consulta, cuando corresponda.
- Información almacenada en los archivos JSON.

**Procesos:**
- Leer los registros almacenados.
- Calcular cantidades, promedios y totales.
- Identificar productos con mayor o menor existencia.
- Identificar el producto más vendido.
- Identificar la venta de mayor importe.
- Calcular ingresos y promedio de ventas.
- Calcular el valor total del inventario.
- Identificar al empleado con el salario más alto.
- Calcular el salario promedio.

**Salidas:**
- Reportes de productos.
- Reportes de inventario.
- Reportes de ventas.
- Reportes de empleados.
- Resultados estadísticos y financieros.
- Mensajes cuando no existan datos suficientes.

### 8.6. Módulo de administración de archivos

**Entradas:**
- Datos nuevos o modificados de los diferentes módulos.
- Solicitudes de lectura y consulta de información.
- Archivos JSON almacenados.

**Procesos:**
- Crear archivos cuando no existan.
- Leer y recuperar información.
- Guardar nuevos registros.
- Actualizar los datos existentes.
- Validar la estructura de la información.
- Manejar errores de lectura y escritura.

**Salidas:**
- Información recuperada.
- Archivos JSON actualizados.
- Confirmación de guardado.
- Mensajes de error cuando ocurra algún problema.

## 9. Validaciones y manejo de errores

El sistema Tekno Comercial deberá incorporar validaciones en todos sus módulos para evitar el ingreso de información incorrecta y garantizar el funcionamiento adecuado de las operaciones.

Cuando ocurra un error, el sistema deberá mostrar un mensaje claro al usuario, permitir corregir la información y continuar funcionando sin cerrarse inesperadamente.

### 9.1. Validaciones de datos generales

- No permitir campos obligatorios vacíos.
- Validar que los datos numéricos contengan valores válidos.
- No permitir valores negativos cuando las operaciones no los admitan.
- Validar que las opciones seleccionadas en los menús existan.
- Solicitar nuevamente la información cuando el usuario ingrese datos incorrectos.
- Evitar que un error de ingreso de datos interrumpa el funcionamiento del programa.

### 9.2. Validaciones de empleados

- Comprobar que el código del empleado no esté duplicado.
- Verificar que el empleado exista antes de buscarlo o modificarlo.
- Validar que el nombre y el puesto no estén vacíos.
- Comprobar que el salario sea numérico y mayor o igual a cero.
- Mostrar un mensaje cuando no existan empleados registrados.

### 9.3. Validaciones de productos

- Comprobar que el código del producto sea único.
- Validar que el nombre y la categoría no estén vacíos.
- Comprobar que el precio sea numérico y mayor que cero.
- Validar que las cantidades sean números enteros iguales o mayores que cero.
- Verificar que el producto exista antes de modificarlo o desactivarlo.
- Impedir que se utilicen productos desactivados en nuevas ventas.

### 9.4. Validaciones de ventas

- Verificar que se seleccione al menos un producto.
- Comprobar que los productos existan y estén activos.
- Validar que las cantidades sean números enteros mayores que cero.
- Comprobar que las existencias sean suficientes.
- Evitar números de venta duplicados.
- Verificar que los cálculos del subtotal, IVA y total sean correctos.
- No modificar el inventario cuando una venta sea cancelada.
- Guardar y actualizar la información solamente cuando la venta sea confirmada correctamente.

### 9.5. Validaciones de inventario

- Comprobar que el producto exista antes de registrar un movimiento.
- Validar que las cantidades sean números enteros mayores que cero.
- Impedir salidas superiores a las existencias disponibles.
- Verificar que el tipo de movimiento seleccionado sea válido.
- Comprobar que cada movimiento tenga una descripción o motivo cuando corresponda.
- Evitar que las existencias sean negativas.

### 9.6. Validaciones de reportes

- Comprobar que existan registros antes de realizar cálculos.
- Evitar divisiones entre cero al calcular promedios.
- Mostrar mensajes cuando no existan ventas, productos o empleados.
- Verificar que los datos utilizados para generar los reportes sean válidos.
- No modificar los archivos originales durante la generación de reportes.

### 9.7. Manejo de errores en archivos JSON

- Comprobar que los archivos existan antes de intentar leerlos.
- Crear los archivos necesarios cuando todavía no existan.
- Manejar errores cuando un archivo JSON tenga un formato incorrecto.
- Controlar los problemas que puedan ocurrir durante la lectura o escritura.
- Evitar sobrescribir información válida cuando ocurra un error.
- Informar al usuario cuando no sea posible guardar o recuperar información.
- Mantener una estructura de datos válida para facilitar su recuperación.

### 9.8. Mensajes de error y recuperación

El sistema deberá mostrar mensajes claros y permitir que el usuario pueda corregir los datos ingresados.

Algunos ejemplos de mensajes que podrá mostrar son:

- "Error: el campo no puede estar vacío."
- "Error: el código ingresado ya se encuentra registrado."
- "Error: el salario debe ser un número mayor o igual a cero."
- "Error: el producto no existe."
- "Error: la cantidad solicitada supera las existencias disponibles."
- "Error: seleccione una opción válida del menú."
- "Error: no fue posible leer el archivo de datos."
- "Operación realizada correctamente."

Después de mostrar un mensaje, el sistema deberá permitir continuar con la operación o regresar al menú correspondiente, según sea necesario.

## 10. Requerimientos de interfaz y estructura de los menús

El sistema Tekno Comercial contará con una interfaz de consola que permitirá al usuario interactuar mediante menús, opciones numeradas y mensajes informativos.

La interfaz deberá ser sencilla, ordenada y fácil de utilizar.

### 10.1. Menú principal

Al iniciar el programa, se deberá mostrar el menú principal con las siguientes opciones:

1. Gestión de empleados.
2. Gestión de productos.
3. Gestión de ventas.
4. Control de inventario.
5. Generación de reportes.
6. Salir del sistema.

El usuario deberá seleccionar una opción para ingresar al módulo correspondiente.

### 10.2. Submenú de gestión de empleados

Deberá presentar las siguientes opciones:

1. Registrar empleado.
2. Mostrar empleados.
3. Buscar empleado.
4. Modificar datos generales.
5. Modificar salario.
6. Consultar salario promedio.
7. Consultar empleado con salario más alto.
8. Regresar al menú principal.

### 10.3. Submenú de gestión de productos

Deberá presentar las siguientes opciones:

1. Registrar producto.
2. Mostrar productos.
3. Buscar producto.
4. Modificar producto.
5. Desactivar producto.
6. Regresar al menú principal.

### 10.4. Submenú de gestión de ventas

Deberá presentar las siguientes opciones:

1. Registrar nueva venta.
2. Consultar historial de ventas.
3. Consultar detalle de una venta.
4. Regresar al menú principal.

Durante el registro de una venta, el sistema deberá permitir agregar varios productos, indicar sus cantidades, consultar los importes y confirmar o cancelar la operación.

### 10.5. Submenú de control de inventario

Deberá presentar las siguientes opciones:

1. Consultar inventario.
2. Registrar entrada de productos.
3. Registrar salida por ajuste.
4. Consultar productos con bajo inventario.
5. Consultar historial de movimientos.
6. Consultar movimientos por producto.
7. Regresar al menú principal.

### 10.6. Submenú de generación de reportes

Deberá presentar las siguientes opciones:

1. Reporte general de productos.
2. Reporte de productos con mayor y menor existencia.
3. Reporte de productos con bajo inventario.
4. Reporte del valor total del inventario.
5. Reporte del historial de ventas.
6. Reporte de ingresos por ventas.
7. Reporte del producto más vendido.
8. Reporte de la venta con mayor importe.
9. Reporte del promedio de ventas.
10. Reporte del empleado con salario más alto.
11. Reporte del salario promedio.
12. Regresar al menú principal.

### 10.7. Características generales de los menús

- Cada menú deberá mostrar un título que identifique el módulo correspondiente.
- Las opciones deberán aparecer numeradas y ordenadas.
- El sistema deberá validar las opciones seleccionadas.
- Cuando el usuario ingrese una opción incorrecta, deberá mostrar un mensaje de error y solicitar nuevamente una opción válida.
- Después de completar una operación, el usuario deberá poder regresar al submenú correspondiente.
- Todos los submenús deberán contar con una opción para regresar al menú principal.
- La opción de salida deberá estar disponible desde el menú principal.
- Antes de cerrar el programa, se deberá mostrar un mensaje de despedida.
- Los menús deberán mantenerse activos hasta que el usuario seleccione la opción de regresar o salir, según corresponda.

## 11. Estructura y organización de los datos

El sistema Tekno Comercial utilizará archivos JSON para almacenar y organizar la información generada por los módulos de empleados, productos, ventas e inventario.

Cada archivo tendrá una estructura definida para facilitar el registro, la consulta, la modificación y la recuperación de los datos.

### 11.1. Archivo de empleados

**Nombre del archivo:** `empleados.json`

Almacenará la información de los empleados registrados.

Cada empleado tendrá los siguientes datos:

- Código del empleado.
- Nombre completo.
- Puesto.
- Salario.

El código del empleado será único y permitirá identificar cada registro.

### 11.2. Archivo de productos

**Nombre del archivo:** `productos.json`

Almacenará la información de los productos disponibles en la empresa.

Cada producto tendrá los siguientes datos:

- Código del producto.
- Nombre.
- Categoría.
- Precio de venta.
- Cantidad disponible.
- Existencia mínima.
- Estado del producto: activo o inactivo.

El código del producto será único y permitirá relacionar los productos con las ventas y los movimientos de inventario.

### 11.3. Archivo de ventas

**Nombre del archivo:** `ventas.json`

Almacenará el historial de las ventas confirmadas.

Cada venta tendrá los siguientes datos:

- Número único de venta.
- Fecha y hora de la venta.
- Lista de productos vendidos.
- Código de cada producto.
- Nombre del producto al momento de la venta.
- Precio unitario aplicado.
- Cantidad vendida.
- Subtotal por producto.
- Subtotal general.
- Porcentaje de IVA aplicado.
- Valor del IVA.
- Total de la venta.

El número de venta será único y consecutivo. La información de los productos y sus precios se conservará en cada venta para mantener el historial, aunque posteriormente se modifique un producto.

### 11.4. Archivo de inventario

**Nombre del archivo:** `inventario.json`

Almacenará el historial de los movimientos realizados en el inventario.

Cada movimiento tendrá los siguientes datos:

- Identificador único del movimiento.
- Código del producto.
- Tipo de movimiento: entrada, salida por ajuste o salida por venta.
- Cantidad de unidades.
- Fecha y hora del movimiento.
- Descripción o motivo.
- Número de venta, cuando corresponda.

Las existencias actuales se consultarán en el archivo `productos.json`, mientras que `inventario.json` conservará el historial de entradas y salidas.

### 11.5. Relación entre los archivos JSON

Los archivos estarán relacionados mediante los códigos de empleados, códigos de productos y números de venta.

- `empleados.json` almacenará la información de los empleados.
- `productos.json` almacenará los datos y las existencias actuales de los productos.
- `ventas.json` conservará el historial de ventas confirmadas.
- `inventario.json` conservará el historial de movimientos de productos.

Cuando se confirme una venta, el sistema deberá guardar la información de la venta, actualizar las existencias de los productos y registrar los movimientos correspondientes en el inventario.

### 11.6. Organización y conservación de los datos

- Los archivos JSON estarán ubicados dentro de la carpeta `data`.
- Se mantendrá una estructura uniforme para cada tipo de registro.
- Los códigos y números identificadores deberán ser únicos.
- Los datos deberán conservarse después de cerrar el programa.
- Se deberán validar los registros antes de guardarlos.
- Los cambios deberán mantenerse sincronizados entre los módulos relacionados.
- Se evitará la pérdida accidental de información durante las operaciones de lectura y escritura.

## 12. Procesos principales del sistema

El sistema Tekno Comercial contará con diferentes procesos que permitirán administrar la información de los empleados, productos, ventas e inventario.

Cada proceso deberá seguir una secuencia de pasos que garantice el cumplimiento de las reglas de negocio y las validaciones establecidas.

### 12.1. Proceso de registro de empleados

1. El usuario ingresará al módulo de gestión de empleados.
2. Seleccionará la opción de registrar empleado.
3. El sistema solicitará el código, nombre completo, puesto y salario.
4. El sistema verificará que los campos obligatorios estén completos.
5. Comprobará que el código no se encuentre registrado.
6. Validará que el salario sea numérico y mayor o igual a cero.
7. Si los datos son correctos, registrará al empleado.
8. Guardará la información en `empleados.json`.
9. Mostrará un mensaje de confirmación.

### 12.2. Proceso de registro de productos

1. El usuario ingresará al módulo de gestión de productos.
2. Seleccionará la opción de registrar producto.
3. El sistema solicitará el código, nombre, categoría, precio de venta, cantidad disponible y existencia mínima.
4. Verificará que los campos obligatorios estén completos.
5. Comprobará que el código del producto no esté duplicado.
6. Validará el precio y las cantidades ingresadas.
7. Si los datos son correctos, registrará el producto.
8. Guardará la información en `productos.json`.
9. Mostrará un mensaje de confirmación.

### 12.3. Proceso de modificación de productos

1. El usuario ingresará al módulo de gestión de productos.
2. Seleccionará la opción de modificar producto.
3. El sistema solicitará el código del producto.
4. Buscará el producto en `productos.json`.
5. Si el producto existe, mostrará su información actual.
6. El usuario seleccionará el dato que desea modificar.
7. El sistema validará la nueva información.
8. Si los datos son correctos, actualizará el registro.
9. Guardará los cambios en `productos.json`.
10. Mostrará un mensaje de confirmación.

### 12.4. Proceso de registro de ventas

1. El usuario ingresará al módulo de ventas.
2. Seleccionará la opción de registrar nueva venta.
3. El sistema permitirá seleccionar uno o varios productos.
4. El usuario indicará la cantidad de cada producto.
5. El sistema comprobará que los productos existan y estén activos.
6. Verificará que las cantidades solicitadas estén disponibles.
7. Calculará el subtotal de cada producto.
8. Sumará los subtotales para obtener el subtotal general.
9. Calculará el IVA del 12 %.
10. Calculará el total de la venta.
11. Mostrará el detalle y solicitará la confirmación del usuario.
12. Si la venta es cancelada, no modificará las existencias.
13. Si la venta es confirmada, generará un número único y consecutivo.
14. Guardará la venta en `ventas.json`.
15. Actualizará las existencias en `productos.json`.
16. Registrará las salidas correspondientes en `inventario.json`.
17. Mostrará el comprobante o resumen de la venta.

### 12.5. Proceso de actualización del inventario

1. El usuario ingresará al módulo de control de inventario.
2. Seleccionará registrar entrada o salida por ajuste.
3. El sistema solicitará el código del producto.
4. Buscará el producto en `productos.json`.
5. Verificará que el producto exista y esté activo.
6. Solicitará la cantidad y el motivo del movimiento.
7. Validará que la cantidad sea un número entero mayor que cero.
8. Si es una salida, comprobará que existan unidades suficientes.
9. Actualizará las existencias del producto.
10. Guardará los cambios en `productos.json`.
11. Registrará el movimiento en `inventario.json`.
12. Mostrará las existencias actualizadas y un mensaje de confirmación.

### 12.6. Proceso de consulta de inventario

1. El usuario ingresará al módulo de control de inventario.
2. Seleccionará consultar inventario.
3. El sistema recuperará los productos almacenados.
4. Mostrará el código, nombre, cantidad disponible y existencia mínima.
5. Comparará las existencias actuales con las cantidades mínimas.
6. Identificará los productos que necesiten reposición.
7. Mostrará una alerta para los productos con bajo inventario.

### 12.7. Proceso de generación de reportes

1. El usuario ingresará al módulo de reportes.
2. Seleccionará el tipo de reporte que desea consultar.
3. El sistema leerá la información de los archivos JSON correspondientes.
4. Verificará que existan datos suficientes.
5. Realizará los cálculos necesarios.
6. Organizará los resultados.
7. Mostrará el reporte solicitado.
8. Permitirá regresar al menú de reportes.

### 12.8. Proceso de lectura y escritura de archivos JSON

**Lectura de información:**

1. El sistema identificará el archivo que necesita consultar.
2. Comprobará si el archivo existe.
3. Si no existe, creará el archivo con una estructura inicial vacía.
4. Si existe, intentará leer su contenido.
5. Verificará que la información tenga un formato válido.
6. Entregará los datos al módulo que los solicitó.

**Escritura de información:**

1. El módulo enviará los datos que deben guardarse.
2. El sistema verificará la información recibida.
3. Preparará los datos en formato JSON.
4. Guardará los cambios en el archivo correspondiente.
5. Comprobará que la operación se complete correctamente.
6. Informará al usuario cuando ocurra un error durante el almacenamiento.

## 13. Requerimientos de pruebas del sistema

El sistema Tekno Comercial deberá someterse a diferentes pruebas para comprobar que sus módulos funcionen correctamente, que los datos se procesen de manera adecuada y que se cumplan las reglas de negocio establecidas.

Las pruebas permitirán identificar errores, corregirlos y verificar que el sistema sea confiable antes de su entrega final.

### 13.1. Pruebas de registro de empleados

Se realizarán pruebas para comprobar que el sistema permita registrar empleados correctamente.

- Registrar un empleado con todos los datos válidos.
- Intentar registrar un empleado utilizando un código que ya exista.
- Intentar registrar un empleado sin completar los campos obligatorios.
- Ingresar un salario negativo.
- Ingresar letras en el campo del salario.
- Comprobar que los empleados registrados queden guardados en `empleados.json`.

### 13.2. Pruebas de gestión de productos

Se comprobará que el módulo de productos permita registrar, consultar, modificar y desactivar productos.

- Registrar un producto con información válida.
- Intentar registrar un producto con un código duplicado.
- Intentar ingresar un precio igual o menor que cero.
- Ingresar una cantidad negativa.
- Ingresar letras en los campos numéricos.
- Buscar un producto existente.
- Buscar un producto que no esté registrado.
- Modificar correctamente los datos de un producto.
- Desactivar un producto y comprobar que no pueda utilizarse en una nueva venta.
- Verificar que los cambios se guarden en `productos.json`.

### 13.3. Pruebas del módulo de ventas

Se comprobará que las ventas se registren y calculen correctamente.

- Registrar una venta con un producto existente y cantidad disponible.
- Registrar una venta con varios productos.
- Intentar vender un producto inexistente.
- Intentar vender un producto desactivado.
- Intentar vender una cantidad igual a cero o negativa.
- Intentar vender más unidades de las disponibles.
- Comprobar el cálculo del subtotal por producto.
- Comprobar el cálculo del subtotal general.
- Comprobar el cálculo del IVA del 12 %.
- Comprobar el cálculo del total de la venta.
- Cancelar una venta y verificar que no se modifique el inventario.
- Confirmar una venta y comprobar que se actualicen las existencias.
- Verificar que la venta quede guardada en `ventas.json`.

### 13.4. Pruebas del módulo de inventario

Se comprobará que las entradas y salidas de productos se registren correctamente.

- Registrar una entrada de productos válida.
- Registrar una salida por ajuste con existencias suficientes.
- Intentar registrar una cantidad igual a cero o negativa.
- Intentar retirar más unidades de las disponibles.
- Intentar modificar el inventario de un producto inexistente.
- Comprobar que las existencias se actualicen correctamente.
- Verificar que cada movimiento quede registrado en `inventario.json`.
- Comprobar que se muestre una alerta cuando un producto alcance o quede por debajo de su existencia mínima.

### 13.5. Pruebas del módulo de reportes

Se comprobará que los reportes presenten información correcta y actualizada.

- Consultar el listado de productos.
- Consultar productos con existencias bajas.
- Comprobar el producto con mayor existencia.
- Comprobar el producto con menor existencia.
- Verificar el valor total del inventario.
- Consultar el historial de ventas.
- Comprobar el total de ingresos por ventas.
- Identificar el producto con mayor cantidad de unidades vendidas.
- Identificar la venta de mayor valor.
- Comprobar el promedio de ventas.
- Identificar al empleado con el salario más alto.
- Comprobar el promedio de salarios.

### 13.6. Pruebas de archivos JSON

Se comprobará que el sistema pueda guardar, leer y actualizar la información correctamente.

- Comprobar que los archivos JSON se creen cuando no existan.
- Guardar información nueva y verificar que permanezca almacenada.
- Leer información previamente guardada.
- Modificar registros y comprobar que los cambios se conserven.
- Comprobar el comportamiento del sistema cuando un archivo esté vacío.
- Comprobar el comportamiento cuando un archivo contenga información con formato incorrecto.
- Verificar que los errores de lectura o escritura se comuniquen sin cerrar inesperadamente el programa.

### 13.7. Pruebas del menú principal y submenús

Se comprobará que la navegación del sistema funcione correctamente.

- Seleccionar cada opción válida del menú principal.
- Seleccionar cada opción disponible en los submenús.
- Ingresar letras cuando se soliciten opciones numéricas.
- Ingresar opciones que no existan.
- Comprobar que el sistema permita regresar a los menús anteriores.
- Comprobar que el programa finalice correctamente al seleccionar la opción de salir.

### 13.8. Registro de resultados de las pruebas

Cada prueba realizada deberá documentarse para conservar evidencia del funcionamiento del sistema.

Se registrarán los siguientes datos:

- Nombre de la prueba.
- Módulo evaluado.
- Datos de entrada.
- Resultado esperado.
- Resultado obtenido.
- Estado de la prueba: aprobada o no aprobada.
- Observaciones y correcciones realizadas.
- Evidencia mediante capturas de pantalla cuando corresponda.

Los resultados se organizarán en la carpeta `docs/pruebas/` y las capturas de pantalla se conservarán en `evidencias/`.

### 13.9. Criterios de aceptación

El sistema se considerará preparado para su entrega cuando:

- Los módulos principales funcionen correctamente.
- Las operaciones respeten las reglas de negocio.
- Los datos se guarden y recuperen correctamente desde los archivos JSON.
- Los cálculos de ventas e inventario sean correctos.
- Las validaciones impidan el ingreso de datos incorrectos.
- Los errores se comuniquen mediante mensajes comprensibles.
- Los menús permitan navegar y salir correctamente.
- Las pruebas realizadas estén documentadas.
- Los errores identificados hayan sido corregidos o registrados.
- El proyecto pueda ejecutarse en otro equipo siguiendo las instrucciones del manual de usuario.

## 14. Documentación y entregables del proyecto

El proyecto Tekno Comercial contará con documentación que permita comprender su funcionamiento, organización, desarrollo y utilización.

Los documentos y archivos deberán mantenerse organizados dentro de las carpetas del proyecto y formar parte del repositorio de GitHub.

### 14.1. Documentación de análisis

Se elaborarán documentos que describan el funcionamiento y los requisitos del sistema.

Se incluirán:

- Planificación del proyecto.
- Requerimientos funcionales y no funcionales.
- Reglas de negocio.
- Procesos principales.
- Entradas, procesos y salidas.
- Validaciones y manejo de errores.

### 14.2. Diagramas de flujo

Se elaborarán diagramas de flujo para representar gráficamente los procesos principales.

Se incluirán diagramas de:

- Registro de empleados.
- Registro y modificación de productos.
- Consulta de productos.
- Registro de ventas.
- Actualización del inventario.
- Lectura y escritura de archivos JSON.
- Generación de reportes.

Los diagramas se realizarán utilizando diagrams.net y se guardarán en `docs/diagramas/`.

### 14.3. Manual técnico

Se elaborará un manual técnico dirigido a las personas encargadas de comprender, revisar o dar mantenimiento al sistema.

Incluirá:

- Descripción general del proyecto.
- Tecnologías utilizadas.
- Requisitos para ejecutar el programa.
- Estructura de carpetas y archivos.
- Descripción de los módulos de Python.
- Explicación del almacenamiento mediante JSON.
- Instrucciones para ejecutar el sistema.
- Consideraciones para realizar modificaciones y mantenimiento.

### 14.4. Manual de usuario

Se elaborará un manual de usuario dirigido a las personas que utilizarán Tekno Comercial.

Incluirá:

- Descripción del sistema.
- Requisitos básicos para utilizarlo.
- Instrucciones para iniciar el programa.
- Explicación del menú principal.
- Uso del módulo de empleados.
- Uso del módulo de productos.
- Uso del módulo de ventas.
- Uso del módulo de inventario.
- Consulta de reportes.
- Ejemplos de operaciones.
- Mensajes de error y recomendaciones de uso.

El manual deberá utilizar un lenguaje sencillo y comprensible para personas sin conocimientos de programación.

### 14.5. Documentación de pruebas

Se conservará un registro de las pruebas realizadas durante el desarrollo.

Incluirá:

- Casos de prueba.
- Datos utilizados.
- Resultados esperados.
- Resultados obtenidos.
- Estado de cada prueba.
- Errores encontrados y correcciones.
- Capturas de pantalla como evidencia.

### 14.6. Código fuente y archivos de datos

El proyecto incluirá:

- Archivos de código fuente de Python.
- Archivos JSON utilizados para almacenar información.
- Archivo README.md con la descripción e instrucciones del proyecto.
- Archivo .gitignore para excluir archivos que no deban publicarse.
- Pruebas del funcionamiento de los módulos.

### 14.7. Evidencias del desarrollo

Se conservarán evidencias que permitan demostrar el avance y la participación de los dos integrantes.

Se incluirán:

- Capturas del desarrollo del sistema.
- Capturas de las pruebas realizadas.
- Evidencias de los diagramas elaborados.
- Historial de cambios en GitHub.
- Ramas y solicitudes de integración cuando correspondan.
- Participación de ambos integrantes en el repositorio.

### 14.8. Entrega final del proyecto

La entrega final estará organizada en un repositorio público de GitHub.

El repositorio contendrá el código fuente, los archivos JSON necesarios, la documentación, los diagramas, las pruebas y las evidencias del proyecto.

También se incluirá una versión final identificada mediante una etiqueta o lanzamiento (release), junto con las instrucciones necesarias para descargar y ejecutar el sistema en otro equipo.

La presentación final demostrará el funcionamiento de los módulos principales de Tekno Comercial.

## 15. Control de versiones y trabajo colaborativo

El desarrollo del sistema Tekno Comercial utilizará Git y GitHub para administrar las versiones del proyecto, registrar los cambios realizados y facilitar la colaboración entre los dos integrantes.

### 15.1. Uso de Git

Git se utilizará como sistema de control de versiones para:

- Registrar los cambios realizados en los archivos.
- Conservar el historial de desarrollo.
- Identificar las modificaciones realizadas.
- Recuperar versiones anteriores cuando sea necesario.
- Facilitar la integración del trabajo de ambos integrantes.

### 15.2. Uso de GitHub

GitHub será la plataforma utilizada para almacenar y compartir el proyecto.

El repositorio deberá ser público y contener:

- Código fuente del sistema.
- Archivos de datos JSON.
- Documentación del proyecto.
- Diagramas de flujo.
- Manual técnico y manual de usuario.
- Pruebas y evidencias.
- Archivo README.md.
- Archivo .gitignore.

### 15.3. Organización del trabajo de los integrantes

Los dos integrantes participarán activamente en el desarrollo del proyecto.

**Integrante 1:**
- Desarrollo del módulo de productos.
- Desarrollo del módulo de ventas.
- Participación en las pruebas.
- Documentación de sus actividades.

**Integrante 2:**
- Desarrollo del módulo de inventario.
- Desarrollo del módulo de reportes.
- Participación en las pruebas.
- Documentación de sus actividades.

**Trabajo compartido:**
- Diseño y planificación del sistema.
- Desarrollo del módulo de empleados.
- Integración de los módulos.
- Revisión y corrección de errores.
- Elaboración de manuales y diagramas.
- Administración del repositorio de GitHub.
- Preparación de la presentación final.

### 15.4. Registro de cambios y commits

Se realizarán al menos ocho commits significativos durante el desarrollo.

Cada commit deberá describir claramente el cambio realizado.

Los commits podrán corresponder a actividades como:

- Creación de la estructura del proyecto.
- Incorporación de la documentación.
- Desarrollo del módulo de productos.
- Desarrollo del módulo de empleados.
- Desarrollo del módulo de ventas.
- Desarrollo del módulo de inventario.
- Desarrollo del módulo de reportes.
- Corrección de errores y pruebas.
- Integración y preparación de la versión final.

Los cambios deberán registrarse de manera progresiva y no solamente al finalizar el proyecto.

### 15.5. Uso de ramas y solicitudes de integración

Se utilizarán ramas para organizar el desarrollo de las diferentes funcionalidades.

Cuando un integrante termine una modificación, podrá crear una solicitud de integración (Pull Request) para revisar los cambios antes de incorporarlos a la rama principal.

Se verificará que los cambios no afecten el funcionamiento de otros módulos.

### 15.6. Uso de Issues

Se utilizarán Issues de GitHub para organizar y dar seguimiento a las actividades del proyecto.

Se deberán registrar como mínimo:

- Un Issue para reportar un error o problema encontrado.
- Un Issue para proponer una tarea nueva o una mejora del sistema.

Cada Issue deberá tener una descripción clara de la actividad o problema.

### 15.7. Versión final del proyecto

Cuando el sistema esté terminado y revisado, se creará una versión final mediante una etiqueta o lanzamiento (Release) en GitHub.

Esta versión permitirá identificar la entrega definitiva del proyecto.

### 15.8. Evidencia de participación

El historial del repositorio deberá demostrar la participación de ambos integrantes mediante commits, ramas, revisiones, solicitudes de integración e Issues.

Cada integrante deberá contribuir de manera real al desarrollo y documentación del sistema.

## 16. Instalación, ejecución y funcionamiento del sistema

El sistema Tekno Comercial deberá estar preparado para instalarse y ejecutarse en una computadora que cumpla con los requisitos establecidos.

Se buscará que su instalación y utilización sean sencillas, incluso para una persona que no haya participado en el desarrollo del proyecto.

### 16.1. Requisitos del sistema

Para ejecutar Tekno Comercial se necesitará:

- Una computadora con sistema operativo Windows.
- Python instalado y configurado correctamente.
- Una versión de Python compatible con el proyecto. Durante el desarrollo se utilizará Python 3.14.7.
- Los archivos del proyecto descargados desde el repositorio de GitHub.
- Un editor de código como Visual Studio Code para realizar tareas de revisión o mantenimiento.

### 16.2. Descarga del proyecto

El proyecto estará disponible en un repositorio público de GitHub.

La persona que necesite utilizarlo podrá:

1. Ingresar al repositorio de Tekno Comercial.
2. Descargar el proyecto completo.
3. Extraer los archivos si se descargaron en formato ZIP.
4. Abrir la carpeta del proyecto en la computadora.

### 16.3. Preparación para la ejecución

Antes de iniciar el programa se deberá:

1. Comprobar que Python esté instalado.
2. Verificar que los archivos del proyecto estén completos.
3. Comprobar que exista la carpeta `data/` para almacenar la información.
4. Verificar que los archivos JSON necesarios puedan crearse o leerse.
5. Comprobar que la computadora tenga permisos para guardar y modificar los archivos del proyecto.

### 16.4. Inicio del sistema

El programa se ejecutará desde el archivo principal `main.py`, ubicado dentro de la carpeta `src/`.

El usuario deberá abrir una terminal en la carpeta principal del proyecto y ejecutar el archivo principal mediante Python.

El sistema mostrará el menú principal de Tekno Comercial y permitirá acceder a los diferentes módulos.

### 16.5. Funcionamiento general

Una vez iniciado el programa:

- Se mostrará el menú principal.
- El usuario seleccionará el módulo que desea utilizar.
- El sistema mostrará las opciones correspondientes.
- Se solicitarán los datos necesarios para cada operación.
- Se realizarán las validaciones y cálculos correspondientes.
- La información se almacenará en los archivos JSON.
- El usuario podrá regresar a los menús anteriores.
- El programa finalizará cuando se seleccione la opción de salir.

### 16.6. Almacenamiento y conservación de información

Los datos del sistema se almacenarán en archivos JSON dentro de la carpeta `data/`.

La información deberá conservarse después de cerrar el programa, de manera que pueda recuperarse cuando se vuelva a ejecutar.

Se deberá evitar eliminar o reemplazar accidentalmente los archivos que contienen información importante.

### 16.7. Compatibilidad con otros equipos

El sistema deberá poder ejecutarse en otra computadora que cumpla con los requisitos establecidos.

Para comprobarlo, se realizará una prueba de instalación y ejecución utilizando una copia descargada desde GitHub.

Se verificará que:

- El programa pueda iniciarse correctamente.
- Los módulos principales estén disponibles.
- Los archivos JSON puedan crearse y modificarse.
- La información se conserve después de cerrar y abrir el programa.
- Las instrucciones del manual de usuario sean suficientes para ejecutar el sistema.
