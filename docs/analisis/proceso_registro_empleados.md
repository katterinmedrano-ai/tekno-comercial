# Análisis del proceso: Registro de empleados

## 1. Nombre del proceso

Registro de empleados.

## 2. Objetivo

Permitir que el usuario registre nuevos empleados en el sistema Tekno Comercial, almacenando sus datos personales y laborales de manera organizada y permanente mediante un archivo JSON.

## 3. Descripción del proceso

El proceso comienza cuando el usuario ingresa al módulo de gestión de empleados y selecciona la opción de registrar un nuevo empleado.

El sistema solicita los datos necesarios: código del empleado, nombre completo, puesto y salario.

Posteriormente, verifica que los campos obligatorios estén completos, que el código no esté registrado anteriormente y que el salario sea un valor numérico mayor o igual a cero.

Si los datos son correctos, el sistema registra al empleado y guarda su información en el archivo `empleados.json`.

Finalmente, muestra un mensaje indicando que el registro se realizó correctamente.

Si ocurre algún error, el sistema informa al usuario y permite corregir los datos.

## 4. Datos de entrada

El sistema solicitará los siguientes datos:

| Dato | Descripción |
|---|---|
| Código | Identificador único del empleado. |
| Nombre completo | Nombre y apellidos del empleado. |
| Puesto | Cargo que desempeña en la empresa. |
| Salario | Cantidad de dinero que recibe el empleado. |

## 5. Procesamiento

El sistema realizará las siguientes operaciones:

1. Solicitar los datos del empleado.
2. Comprobar que los campos obligatorios no estén vacíos.
3. Verificar que el código no exista en los registros actuales.
4. Comprobar que el salario sea numérico.
5. Verificar que el salario sea mayor o igual a cero.
6. Preparar los datos del empleado.
7. Incorporar el nuevo registro a la información existente.
8. Guardar los datos actualizados en `empleados.json`.

## 6. Datos de salida

Cuando el proceso finalice correctamente, el sistema deberá:

- Mostrar un mensaje de registro exitoso.
- Conservar los datos del empleado en `empleados.json`.
- Permitir que el empleado aparezca posteriormente en las consultas y reportes.

Si ocurre un error, deberá mostrar un mensaje que explique el problema.

## 7. Reglas de negocio

- Cada empleado debe tener un código único.
- No se permiten códigos duplicados.
- El nombre completo es obligatorio.
- El puesto es obligatorio.
- El salario debe ser numérico.
- El salario no puede ser negativo.
- Se permite registrar un salario igual a cero.
- La información registrada debe conservarse después de cerrar el programa.

## 8. Validaciones y manejo de errores

| Situación | Respuesta del sistema |
|---|---|
| Código duplicado | Informar que el empleado ya está registrado. |
| Nombre vacío | Solicitar nuevamente el nombre. |
| Puesto vacío | Solicitar nuevamente el puesto. |
| Salario negativo | Rechazar el valor e informar el motivo. |
| Salario con letras | Informar que debe ingresar un valor numérico. |
| Datos correctos | Guardar el empleado y confirmar el registro. |
| Archivo JSON inexistente | Crear el archivo con una estructura inicial válida. |
| Error al guardar | Informar que no fue posible guardar los datos. |

## 9. Secuencia general del proceso

1. Inicio.
2. Ingresar al módulo de empleados.
3. Seleccionar registrar empleado.
4. Solicitar los datos.
5. Validar los campos obligatorios.
6. Comprobar que el código sea único.
7. Validar el salario.
8. Si existe algún error, mostrar el mensaje correspondiente y solicitar la corrección.
9. Si los datos son correctos, guardar el empleado.
10. Mostrar confirmación.
11. Fin.

## 10. Archivo relacionado

El archivo utilizado para almacenar la información será:

`data/empleados.json`

Este archivo conservará los registros de los empleados y permitirá consultarlos posteriormente.
