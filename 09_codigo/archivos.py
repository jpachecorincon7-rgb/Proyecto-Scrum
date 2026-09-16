import json
import os
CARPETA_DATOS = "datos"
def _ruta(nombre_archivo):
    return os.path.join(CARPETA_DATOS, nombre_archivo)


def cargar_datos(nombre_archivo):
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
    os.makedirs(CARPETA_DATOS, exist_ok=True)
    ruta = _ruta(nombre_archivo)
    try:
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)
        return True
    except OSError as error:
        print(f"⚠️  Error al guardar '{nombre_archivo}': {error}")
        return False
