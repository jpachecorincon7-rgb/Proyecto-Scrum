from archivos import cargar_datos, guardar_datos

ARCHIVO = "equipos.json"
ESTADOS_VALIDOS = ("Disponible", "Prestado")


def _siguiente_codigo(equipos):
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
    equipos = cargar_datos(ARCHIVO)
    if solo_disponibles:
        return [eq for eq in equipos if eq.get("estado") == "Disponible"]
    return equipos


def buscar_equipo(codigo):
    equipos = cargar_datos(ARCHIVO)
    for eq in equipos:
        if eq.get("codigo", "").upper() == codigo.strip().upper():
            return eq
    return None


def actualizar_estado_equipo(codigo, nuevo_estado):
    if nuevo_estado not in ESTADOS_VALIDOS:
        return False, "Estado no válido."

    equipos = cargar_datos(ARCHIVO)
    for eq in equipos:
        if eq.get("codigo", "").upper() == codigo.strip().upper():
            eq["estado"] = nuevo_estado
            guardar_datos(ARCHIVO, equipos)
            return True, "Estado actualizado."
    return False, "Equipo no encontrado."
