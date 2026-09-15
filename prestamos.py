"""
prestamos.py
Gestión de préstamos de equipos.
Historia de usuario cubierta: HU04.
"""

from datetime import datetime
from archivos import cargar_datos, guardar_datos
from equipos import buscar_equipo, actualizar_estado_equipo
from estudiantes import buscar_estudiante

ARCHIVO = "prestamos.json"


def _siguiente_id(prestamos):
    """Genera un id consecutivo tipo PR001, PR002, ..."""
    maximo = 0
    for p in prestamos:
        idp = p.get("id", "")
        if idp.startswith("PR"):
            try:
                numero = int(idp.replace("PR", ""))
                maximo = max(maximo, numero)
            except ValueError:
                continue
    return f"PR{maximo + 1:03d}"


def registrar_prestamo(codigo_equipo, documento_estudiante):
    """
    HU04 - Registra el préstamo de un equipo a un estudiante.
    Valida que el estudiante exista, que el equipo exista y que esté disponible.
    Al registrar el préstamo, cambia el estado del equipo a 'Prestado'.
    """
    equipo = buscar_equipo(codigo_equipo)
    if equipo is None:
        return False, "El equipo indicado no existe."

    if equipo.get("estado") != "Disponible":
        return False, "El equipo no está disponible para préstamo."

    estudiante = buscar_estudiante(documento_estudiante)
    if estudiante is None:
        return False, "El estudiante indicado no está registrado."

    prestamos = cargar_datos(ARCHIVO)
    nuevo = {
        "id": _siguiente_id(prestamos),
        "codigo_equipo": equipo["codigo"],
        "documento_estudiante": estudiante["documento"],
        "nombre_estudiante": estudiante["nombre"],
        "fecha_prestamo": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "estado": "Activo",
    }
    prestamos.append(nuevo)
    guardar_datos(ARCHIVO, prestamos)

    actualizar_estado_equipo(equipo["codigo"], "Prestado")
    return True, f"Préstamo registrado con id {nuevo['id']}."


def listar_prestamos():
    """Retorna todos los préstamos registrados (útil para revisar el archivo de datos)."""
    return cargar_datos(ARCHIVO)
