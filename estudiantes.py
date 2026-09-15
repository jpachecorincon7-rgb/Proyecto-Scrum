"""
estudiantes.py
Gestión del registro de estudiantes.
Historia de usuario cubierta: HU03.
"""

import re
from archivos import cargar_datos, guardar_datos

ARCHIVO = "estudiantes.json"


def _correo_valido(correo):
    """Validación simple de formato de correo electrónico."""
    patron = r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, correo) is not None


def registrar_estudiante(documento, nombre, correo, programa):
    """
    HU03 - Registra un estudiante para poder asociarlo a préstamos.
    Valida que el documento sea único y que los campos no estén vacíos.
    """
    documento = documento.strip()
    nombre = nombre.strip()
    correo = correo.strip()
    programa = programa.strip()

    if not documento or not nombre or not correo or not programa:
        return False, "Todos los campos son obligatorios."

    if not documento.isdigit():
        return False, "El documento debe contener solo números."

    if not _correo_valido(correo):
        return False, "El correo electrónico no tiene un formato válido."

    estudiantes = cargar_datos(ARCHIVO)
    for est in estudiantes:
        if est.get("documento") == documento:
            return False, "Ya existe un estudiante registrado con ese documento."

    nuevo = {
        "documento": documento,
        "nombre": nombre,
        "correo": correo,
        "programa": programa,
    }
    estudiantes.append(nuevo)
    guardar_datos(ARCHIVO, estudiantes)
    return True, f"Estudiante {nombre} registrado correctamente."


def listar_estudiantes():
    """Retorna la lista completa de estudiantes registrados."""
    return cargar_datos(ARCHIVO)


def buscar_estudiante(documento):
    """Busca un estudiante por documento. Retorna el diccionario o None si no existe."""
    estudiantes = cargar_datos(ARCHIVO)
    for est in estudiantes:
        if est.get("documento") == documento.strip():
            return est
    return None
