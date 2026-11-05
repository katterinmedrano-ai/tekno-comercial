import sys
from pathlib import Path
import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout

RUTA_PROYECTO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RUTA_PROYECTO / "src"))

import ventas


class PruebasVentas(unittest.TestCase):

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
            }
        ]

        self.lista_ventas = []

        self.movimientos = []

    def leer_simulado(self, nombre):
        if nombre == "productos.json":
            return self.productos

        if nombre == "ventas.json":
            return self.lista_ventas

        return self.movimientos

    def test_generar_numero_venta(self):
        resultado = ventas.generar_numero_venta(self.lista_ventas)

        self.assertEqual(resultado, "V001")

    def test_generar_numero_venta_con_historial(self):
        self.lista_ventas = [
            {"numero": "V001"},
            {"numero": "V002"}
        ]

        resultado = ventas.generar_numero_venta(self.lista_ventas)

        self.assertEqual(resultado, "V003")

    def test_mostrar_ventas_sin_registros(self):
        with patch.object(
            ventas, "leer_archivo",
            side_effect=self.leer_simulado
        ):
            salida = StringIO()

            with redirect_stdout(salida):
                ventas.mostrar_ventas()

            self.assertIn("No hay ventas", salida.getvalue())

    def test_registrar_venta_sin_productos(self):
        with patch.object(
            ventas, "leer_archivo",
            side_effect=self.leer_simulado
        ):
            with patch.object(
                ventas, "guardar_cambios_venta"
            ) as guardar:
                with patch("builtins.input", return_value="FIN"):
                    salida = StringIO()

                    with redirect_stdout(salida):
                        ventas.registrar_venta()

                    self.assertIn("venta", salida.getvalue().lower())
                    guardar.assert_not_called()

    def test_anular_venta_inexistente(self):
        with patch.object(
            ventas, "leer_archivo",
            side_effect=self.leer_simulado
        ):
            with patch.object(
                ventas, "guardar_cambios_venta"
            ) as guardar:
                with patch("builtins.input", return_value="V999"):
                    salida = StringIO()

                    with redirect_stdout(salida):
                        ventas.anular_venta()

                    self.assertIn("venta", salida.getvalue().lower())
                    guardar.assert_not_called()


if __name__ == "__main__":
    unittest.main()