import re
from archivos import cargar_datos, guardar_datos

ARCHIVO = "estudiantes.json"


def _correo_valido(correo):
    patron = r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, correo) is not None


def registrar_estudiante(documento, nombre, correo, programa):
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
    return cargar_datos(ARCHIVO)


def buscar_estudiante(documento):
    estudiantes = cargar_datos(ARCHIVO)
    for est in estudiantes:
        if est.get("documento") == documento.strip():
            return est
    return None
