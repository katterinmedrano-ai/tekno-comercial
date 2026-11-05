import sys
from pathlib import Path
import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout

RUTA_PROYECTO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RUTA_PROYECTO / "src"))

import empleados


class PruebasEmpleados(unittest.TestCase):

    def setUp(self):
        self.lista_empleados = [
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

    def test_promedio_salarios(self):
        with patch.object(
            empleados, "leer_archivo",
            return_value=self.lista_empleados
        ):
            salida = StringIO()

            with redirect_stdout(salida):
                empleados.promedio_salarios()

            self.assertIn("3000", salida.getvalue())

    def test_mostrar_empleados(self):
        with patch.object(
            empleados, "leer_archivo",
            return_value=self.lista_empleados
        ):
            salida = StringIO()

            with redirect_stdout(salida):
                empleados.mostrar_empleados()

            self.assertIn("Ana", salida.getvalue())
            self.assertIn("Luis", salida.getvalue())

    def test_buscar_empleado(self):
        with patch.object(
            empleados, "leer_archivo",
            return_value=self.lista_empleados
        ):
            with patch("builtins.input", return_value="E001"):
                salida = StringIO()

                with redirect_stdout(salida):
                    empleados.buscar_empleado()

                self.assertIn("Ana", salida.getvalue())

    def test_no_modificar_salario_empleado_inactivo(self):
        with patch.object(
            empleados, "leer_archivo",
            return_value=self.lista_empleados
        ):
            with patch.object(empleados, "guardar_archivo") as guardar:
                with patch(
                    "builtins.input",
                    side_effect=["E002", "3500"]
                ):
                    salida = StringIO()

                    with redirect_stdout(salida):
                        empleados.modificar_salario()

                    self.assertIn(
                        "inactivo",
                        salida.getvalue().lower()
                    )

                    guardar.assert_not_called()

    def test_no_reactivar_empleado_activo(self):
        with patch.object(
            empleados, "leer_archivo",
            return_value=self.lista_empleados
        ):
            with patch.object(empleados, "guardar_archivo") as guardar:
                with patch("builtins.input", return_value="E001"):
                    salida = StringIO()

                    with redirect_stdout(salida):
                        empleados.reactivar_empleado()

                    self.assertIn(
                        "activo",
                        salida.getvalue().lower()
                    )

                    guardar.assert_not_called()


if __name__ == "__main__":
    unittest.main()
