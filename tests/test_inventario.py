import sys
from pathlib import Path
import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout

RUTA_PROYECTO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RUTA_PROYECTO / "src"))

import inventario


class PruebasInventario(unittest.TestCase):

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
                "existencias": 5,
                "existencia_minima": 2,
                "estado": "inactivo"
            }
        ]

        self.movimientos = []

    def leer_simulado(self, nombre):
        if nombre == "productos.json":
            return self.productos

        return self.movimientos

    def test_consultar_inventario(self):
        with patch.object(
            inventario, "leer_archivo",
            side_effect=self.leer_simulado
        ):
            salida = StringIO()

            with redirect_stdout(salida):
                inventario.consultar_inventario()

            self.assertIn("Teclado", salida.getvalue())

    def test_registrar_entrada(self):
        with patch.object(
            inventario, "leer_archivo",
            side_effect=self.leer_simulado
        ):
            with patch.object(inventario, "guardar_archivo"):
                with patch("builtins.input", side_effect=["P001", "5"]):
                    salida = StringIO()

                    with redirect_stdout(salida):
                        inventario.registrar_entrada()

                    self.assertIn(
                        "Entrada registrada correctamente",
                        salida.getvalue()
                    )

    def test_registrar_salida(self):
        with patch.object(
            inventario, "leer_archivo",
            side_effect=self.leer_simulado
        ):
            with patch.object(inventario, "guardar_archivo"):
                with patch("builtins.input", side_effect=["P001", "3"]):
                    salida = StringIO()

                    with redirect_stdout(salida):
                        inventario.registrar_salida()

                    self.assertIn(
                        "Salida registrada correctamente",
                        salida.getvalue()
                    )

    def test_no_permitir_movimiento_producto_inactivo(self):
        with patch.object(
            inventario, "leer_archivo",
            side_effect=self.leer_simulado
        ):
            with patch.object(
                inventario, "guardar_archivo"
            ) as guardar:
                with patch("builtins.input", side_effect=["P002", "2"]):
                    salida = StringIO()

                    with redirect_stdout(salida):
                        inventario.registrar_entrada()

                    self.assertIn(
                        "inactivo",
                        salida.getvalue().lower()
                    )

                    guardar.assert_not_called()

    def test_mostrar_movimientos(self):
        self.movimientos = [
            {
                "fecha": "2026-11-04",
                "codigo_producto": "P001",
                "tipo": "entrada",
                "cantidad": 5,
                "descripcion": "Compra de productos"
            }
        ]

        with patch.object(
            inventario, "leer_archivo",
            side_effect=self.leer_simulado
        ):
            salida = StringIO()

            with redirect_stdout(salida):
                inventario.mostrar_movimientos()

            self.assertIn("P001", salida.getvalue())


if __name__ == "__main__":
    unittest.main()