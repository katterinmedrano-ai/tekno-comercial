import sys
from pathlib import Path
import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout

RUTA_PROYECTO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RUTA_PROYECTO / "src"))

import reportes


class PruebasReportes(unittest.TestCase):

    def setUp(self):
        self.productos = [
            {
                "codigo": "P001",
                "nombre": "Teclado",
                "categoria": "Accesorios",
                "precio": 150.0,
                "existencias": 10,
                "existencia_minima": 3,
                "estado": "activo"
            },
            {
                "codigo": "P002",
                "nombre": "Mouse",
                "categoria": "Accesorios",
                "precio": 80.0,
                "existencias": 2,
                "existencia_minima": 5,
                "estado": "activo"
            }
        ]

        self.ventas = [
            {
                "numero": "V001",
                "fecha": "2026-11-04",
                "detalles": [
                    {
                        "codigo": "P001",
                        "nombre": "Teclado",
                        "cantidad": 2,
                        "precio": 150.0,
                        "subtotal": 300.0
                    }
                ],
                "subtotal": 300.0,
                "iva": 36.0,
                "total": 336.0,
                "estado": "confirmada"
            },
            {
                "numero": "V002",
                "fecha": "2026-11-04",
                "detalles": [],
                "subtotal": 100.0,
                "iva": 12.0,
                "total": 112.0,
                "estado": "anulada"
            }
        ]

        self.empleados = [
            {
                "codigo": "E001",
                "nombre": "Ana",
                "salario": 3000.0,
                "estado": "activo"
            },
            {
                "codigo": "E002",
                "nombre": "Luis",
                "salario": 2500.0,
                "estado": "inactivo"
            }
        ]

    def test_reporte_productos(self):
        with patch.object(
            reportes, "leer_archivo",
            return_value=self.productos
        ):
            salida = StringIO()

            with redirect_stdout(salida):
                reportes.reporte_productos()

            self.assertIn("Teclado", salida.getvalue())
            self.assertIn("Mouse", salida.getvalue())

    def test_reporte_bajo_stock(self):
        with patch.object(
            reportes, "leer_archivo",
            return_value=self.productos
        ):
            salida = StringIO()

            with redirect_stdout(salida):
                reportes.reporte_bajo_stock()

            self.assertIn("Mouse", salida.getvalue())
            self.assertNotIn("Teclado", salida.getvalue())

    def test_reporte_valor_inventario(self):
        with patch.object(
            reportes, "leer_archivo",
            return_value=self.productos
        ):
            salida = StringIO()

            with redirect_stdout(salida):
                reportes.reporte_valor_inventario()

            self.assertIn("1660.0", salida.getvalue())

    def test_reporte_ventas_excluye_anuladas(self):
        with patch.object(
            reportes, "leer_archivo",
            side_effect=[self.ventas, self.productos]
        ):
            salida = StringIO()

            with redirect_stdout(salida):
                reportes.reporte_ventas()

            self.assertIn("336.0", salida.getvalue())
            self.assertNotIn("112.0", salida.getvalue())

    def test_reporte_empleados(self):
        with patch.object(
            reportes, "leer_archivo",
            return_value=self.empleados
        ):
            salida = StringIO()

            with redirect_stdout(salida):
                reportes.reporte_empleados()

            self.assertIn("Ana", salida.getvalue())
            self.assertNotIn("Luis", salida.getvalue())


if __name__ == "__main__":
    unittest.main()