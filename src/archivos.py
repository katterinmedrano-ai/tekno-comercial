import json
from pathlib import Path

RUTA_DATA = Path(__file__).resolve().parent.parent / "data"

ARCHIVOS = [
    "productos.json",
    "empleados.json",
    "ventas.json",
    "inventario.json"
]

def validar_archivo(nombre_archivo):

    if nombre_archivo not in ARCHIVOS:
        raise ValueError("El archivo no está permitido.")

def leer_archivo(nombre_archivo):

    validar_archivo(nombre_archivo)

    RUTA_DATA.mkdir(parents=True, exist_ok=True)

    ruta = RUTA_DATA / nombre_archivo

    if not ruta.exists():
        guardar_archivo(nombre_archivo, [])
        return []

    try:

        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

    except json.JSONDecodeError as error:
        raise ValueError(
            f"El archivo {nombre_archivo} contiene JSON inválido."
        ) from error

    if not isinstance(datos, list):
        raise ValueError(
            f"La estructura de {nombre_archivo} debe ser una lista."
        )

    return datos

def guardar_archivo(nombre_archivo, datos):

    validar_archivo(nombre_archivo)

    if not isinstance(datos, list):
        raise ValueError("Los datos deben estar organizados en una lista.")

    RUTA_DATA.mkdir(parents=True, exist_ok=True)

    ruta = RUTA_DATA / nombre_archivo
    ruta_temporal = RUTA_DATA / (nombre_archivo + ".tmp")

    try:

        with open(ruta_temporal, "w", encoding="utf-8") as archivo:
            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        ruta_temporal.replace(ruta)

    except Exception:

        if ruta_temporal.exists():
            ruta_temporal.unlink()

        raise
