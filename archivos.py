"""
archivos.py
Módulo de utilidades para la persistencia de datos en archivos JSON.
Centraliza la lectura y escritura para que el resto de módulos
no tengan que preocuparse por el manejo de errores de archivos.
"""

import json
import os

CARPETA_DATOS = "datos"


def _ruta(nombre_archivo):
    """Construye la ruta completa de un archivo dentro de la carpeta datos/."""
    return os.path.join(CARPETA_DATOS, nombre_archivo)


def cargar_datos(nombre_archivo):
    """
    Carga una lista de datos desde un archivo JSON.
    Si el archivo no existe o está vacío/corrupto, retorna una lista vacía
    en lugar de lanzar una excepción, para que el programa no se caiga.
    """
    ruta = _ruta(nombre_archivo)
    if not os.path.exists(ruta):
        return []

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read().strip()
            if not contenido:
                return []
            return json.loads(contenido)
    except (json.JSONDecodeError, OSError) as error:
        print(f"⚠️  No se pudo leer '{nombre_archivo}' correctamente ({error}).")
        print("   Se continuará con una lista vacía para evitar perder el programa.")
        return []


def guardar_datos(nombre_archivo, datos):
    """
    Guarda una lista de datos (dicts) en un archivo JSON, creando la carpeta
    datos/ si no existe todavía.
    """
    os.makedirs(CARPETA_DATOS, exist_ok=True)
    ruta = _ruta(nombre_archivo)
    try:
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
        return True
    except OSError as error:
        print(f"⚠️  Error al guardar '{nombre_archivo}': {error}")
        return False
