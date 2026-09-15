"""
equipos.py
Gestión del inventario de equipos tecnológicos.
Historias de usuario cubiertas: HU01, HU02.
"""

from archivos import cargar_datos, guardar_datos

ARCHIVO = "equipos.json"
ESTADOS_VALIDOS = ("Disponible", "Prestado")


def _siguiente_codigo(equipos):
    """
    Genera un código consecutivo tipo EQ001, EQ002, ...
    a partir del código numérico más alto ya registrado.
    """
    maximo = 0
    for eq in equipos:
        codigo = eq.get("codigo", "")
        if codigo.startswith("EQ"):
            try:
                numero = int(codigo.replace("EQ", ""))
                maximo = max(maximo, numero)
            except ValueError:
                continue
    return f"EQ{maximo + 1:03d}"


def registrar_equipo(tipo, marca, modelo, estado="Disponible"):
    """
    HU01 - Registra un nuevo equipo tecnológico en el inventario.
    Valida que los campos no estén vacíos. El código se genera automáticamente.
    Retorna (True, mensaje) o (False, mensaje) según el resultado.
    """
    tipo = tipo.strip()
    marca = marca.strip()
    modelo = modelo.strip()

    if not tipo or not marca or not modelo:
        return False, "Tipo, marca y modelo son obligatorios."

    if estado not in ESTADOS_VALIDOS:
        estado = "Disponible"

    equipos = cargar_datos(ARCHIVO)
    nuevo = {
        "codigo": _siguiente_codigo(equipos),
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "estado": estado,
    }
    equipos.append(nuevo)
    guardar_datos(ARCHIVO, equipos)
    return True, f"Equipo registrado con código {nuevo['codigo']}."


def listar_equipos(solo_disponibles=False):
    """
    HU02 - Retorna la lista de equipos registrados.
    Si solo_disponibles es True, filtra únicamente los que están en estado Disponible.
    """
    equipos = cargar_datos(ARCHIVO)
    if solo_disponibles:
        return [eq for eq in equipos if eq.get("estado") == "Disponible"]
    return equipos


def buscar_equipo(codigo):
    """Busca un equipo por su código. Retorna el diccionario o None si no existe."""
    equipos = cargar_datos(ARCHIVO)
    for eq in equipos:
        if eq.get("codigo", "").upper() == codigo.strip().upper():
            return eq
    return None


def actualizar_estado_equipo(codigo, nuevo_estado):
    """
    Actualiza el estado de un equipo (Disponible / Prestado).
    Usado internamente por el módulo de préstamos.
    """
    if nuevo_estado not in ESTADOS_VALIDOS:
        return False, "Estado no válido."

    equipos = cargar_datos(ARCHIVO)
    for eq in equipos:
        if eq.get("codigo", "").upper() == codigo.strip().upper():
            eq["estado"] = nuevo_estado
            guardar_datos(ARCHIVO, equipos)
            return True, "Estado actualizado."
    return False, "Equipo no encontrado."
