# Registro de la primera ejecución de pruebas fallida

**Proyecto:** Tekno Comercial  
**Fecha:** 04 de noviembre de 2026  
**Comando ejecutado:**

```bash
python -m unittest discover -s tests -v
```

## 1. Descripción de la primera ejecución

Durante la primera ejecución de las pruebas automatizadas se detectaron cuatro resultados incorrectos: dos pruebas fallidas (*FAIL*) y dos pruebas con errores (*ERROR*).

De un total de 32 pruebas ejecutadas, 28 finalizaron correctamente y 4 presentaron inconvenientes.

## 2. Errores identificados

| Prueba | Resultado | Descripción |
|---|---|---|
| `test_registrar_entrada` | FAIL | No se obtuvo el mensaje esperado de registro correcto de entrada. |
| `test_registrar_salida` | FAIL | No se obtuvo el mensaje esperado de registro correcto de salida. |
| `test_anular_venta_inexistente` | ERROR | Se produjo un `KeyError: 'numero'` debido a que los datos simulados se entregaban en un orden incorrecto. |
| `test_registrar_venta_sin_productos` | ERROR | Se produjo un `StopIteration` porque la prueba no proporcionaba todos los datos de entrada que el proceso esperaba. |

## 3. Causas identificadas

- **Pruebas de inventario:** la simulación de lectura de archivos no contemplaba todas las lecturas realizadas durante el proceso de registro.
- **Anulación de ventas:** los datos simulados no correspondían al archivo que el módulo intentaba consultar.
- **Registro de ventas:** faltaba proporcionar la opción `FIN` para indicar que no se agregarían más productos.

## 4. Correcciones realizadas

Se actualizaron los archivos de pruebas `test_inventario.py` y `test_ventas.py`.

Las correcciones consistieron en:

1. Mejorar la simulación de lectura de archivos según el nombre del archivo solicitado.
2. Corregir la información simulada utilizada en la prueba de anulación de ventas.
3. Completar los datos de entrada necesarios para probar el registro de una venta sin productos.
4. Ajustar las pruebas para verificar los resultados esperados sin modificar innecesariamente la información real almacenada en los archivos JSON.

## 5. Resultado posterior a las correcciones

Después de realizar los ajustes, se ejecutó nuevamente el comando:

```bash
python -m unittest discover -s tests -v
```

El resultado fue:

```text
Ran 32 tests in 0.049s

OK
```

**Conclusión:** La primera ejecución permitió identificar y corregir inconvenientes en las pruebas automatizadas. En la segunda ejecución, las 32 pruebas finalizaron correctamente, sin fallos ni errores reportados.


# Resultados de las pruebas del sistema

**Proyecto:** Tekno Comercial  
**Fecha:** 4 de noviembre de 2026

## Ejecución de pruebas automatizadas

Se ejecutó el siguiente comando en la terminal:

python -m unittest discover -s tests -v

## Resultado

- Pruebas ejecutadas: 32
- Pruebas aprobadas: 32
- Pruebas fallidas: 0
- Errores: 0

**Estado final: OK**

Todas las pruebas automatizadas ejecutadas finalizaron correctamente.

## Reflexión sobre el proceso de pruebas

Durante el desarrollo de Tekno Comercial comprendimos que no siempre se obtiene un resultado correcto en el primer intento. La primera ejecución de las pruebas automatizadas permitió identificar cuatro inconvenientes que debían corregirse.

En lugar de ignorar los errores o dar por terminado el trabajo, revisamos las causas, realizamos los ajustes necesarios y ejecutamos nuevamente las pruebas.

Finalmente, conseguimos que las 32 pruebas finalizaran correctamente.

Este proceso nos permitió comprender que los errores forman parte del desarrollo de software y que identificarlos, corregirlos y comprobar las soluciones es fundamental para mejorar la calidad del sistema.

**Nuestro aprendizaje:** no se trata de que todo salga bien a la primera, sino de tener la disposición de revisar, aprender, corregir y continuar hasta alcanzar el resultado esperado.
