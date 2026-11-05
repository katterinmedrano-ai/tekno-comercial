import sys
from pathlib import Path
import unittest
import json
import tempfile

RUTA_PROYECTO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RUTA_PROYECTO / "src"))

import archivos


class PruebasArchivos(unittest.TestCase):

    def setUp(self):
        self.directorio_temporal = tempfile.TemporaryDirectory()

        self.ruta_original = archivos.RUTA_DATA

        archivos.RUTA_DATA = Path(
            self.directorio_temporal.name
        )

    def tearDown(self):
        archivos.RUTA_DATA = self.ruta_original
        self.directorio_temporal.cleanup()

    def test_leer_archivo_existente(self):
        datos = [
            {
                "codigo": "P001",
                "nombre": "Teclado"
            }
        ]

        ruta = archivos.RUTA_DATA / "productos.json"

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo)

        resultado = archivos.leer_archivo("productos.json")

        self.assertEqual(resultado, datos)

    def test_guardar_archivo(self):
        datos = [
            {
                "codigo": "P001",
                "nombre": "Teclado"
            }
        ]

        archivos.guardar_archivo("productos.json", datos)

        resultado = archivos.leer_archivo("productos.json")

        self.assertEqual(resultado, datos)

    def test_crear_archivo_inexistente(self):
        resultado = archivos.leer_archivo("empleados.json")

        self.assertEqual(resultado, [])

    def test_rechazar_archivo_no_permitido(self):
        with self.assertRaises(ValueError):
            archivos.leer_archivo("otro.json")

    def test_rechazar_datos_que_no_sean_lista(self):
        with self.assertRaises(ValueError):
            archivos.guardar_archivo(
                "productos.json",
                {"codigo": "P001"}
            )

    def test_rechazar_json_invalido(self):
        ruta = archivos.RUTA_DATA / "productos.json"

        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write("{contenido incorrecto")

        with self.assertRaises(ValueError):
            archivos.leer_archivo("productos.json")


if __name__ == "__main__":
    unittest.main()