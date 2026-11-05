import sys
from pathlib import Path
import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout

RUTA_PROYECTO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RUTA_PROYECTO / "src"))

import productos


class PruebasProductos(unittest.TestCase):

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

    def test_contar_productos(self):
        with patch.object(
            productos, "leer_archivo",
            return_value=self.productos
        ):
            salida = StringIO()

            with redirect_stdout(salida):
                productos.contar_productos()

            self.assertIn("Total de productos: 2", salida.getvalue())
            self.assertIn("Productos activos: 2", salida.getvalue())

    def test_existe_producto(self):
        with patch.object(
            productos, "leer_archivo",
            return_value=self.productos
        ):
            self.assertTrue(productos.existe_producto("P001"))
            self.assertFalse(productos.existe_producto("P999"))

    def test_valor_total_inventario(self):
        with patch.object(
            productos, "leer_archivo",
            return_value=self.productos
        ):
            salida = StringIO()

            with redirect_stdout(salida):
                productos.valor_total_inventario()

            self.assertIn("1660.0", salida.getvalue())

    def test_productos_bajo_stock(self):
        with patch.object(
            productos, "leer_archivo",
            return_value=self.productos
        ):
            salida = StringIO()

            with redirect_stdout(salida):
                productos.mostrar_productos_bajo_stock()

            self.assertIn("Mouse", salida.getvalue())
            self.assertNotIn("Teclado", salida.getvalue())

    def test_buscar_producto(self):
        with patch.object(
            productos, "leer_archivo",
            return_value=self.productos
        ):
            with patch("builtins.input", return_value="P001"):
                salida = StringIO()

                with redirect_stdout(salida):
                    productos.buscar_producto()

                self.assertIn("Teclado", salida.getvalue())

    def test_listar_categorias(self):
        with patch.object(
            productos, "leer_archivo",
            return_value=self.productos
        ):
            salida = StringIO()

            with redirect_stdout(salida):
                productos.listar_categorias()

            self.assertIn("Accesorios", salida.getvalue())


if __name__ == "__main__":
    unittest.main()