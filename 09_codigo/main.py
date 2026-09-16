import equipos
import estudiantes
import prestamos


def pausar():
    input("\nPresiona Enter para continuar...")


def menu_principal():
    print("\n" + "=" * 55)
    print("SISTEMA DE PRÉSTAMO DE EQUIPOS TECNOLÓGICOS".center(55))
    print("Colegio San Marín".center(55))
    print("=" * 55)
    print("1. Registrar equipo          (HU01)")
    print("2. Listar equipos            (HU02)")
    print("3. Registrar estudiante      (HU03)")
    print("4. Registrar préstamo        (HU04)")
    print("0. Salir")
    print("=" * 55)


# ---------- Opciones de equipos ----------

def opcion_registrar_equipo():
    print("\n--- Registrar equipo (HU01) ---")
    tipo = input("Tipo (portátil, monitor, tableta, etc.): ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ok, mensaje = equipos.registrar_equipo(tipo, marca, modelo)
    print(("✅ " if ok else "❌ ") + mensaje)


def opcion_listar_equipos():
    print("\n--- Listado de equipos (HU02) ---")
    lista = equipos.listar_equipos()
    if not lista:
        print("No hay equipos registrados todavía.")
        return
    for eq in lista:
        print(f"[{eq['codigo']}] {eq['tipo']} - {eq['marca']} {eq['modelo']} "
              f"| Estado: {eq['estado']}")


# ---------- Opciones de estudiantes ----------

def opcion_registrar_estudiante():
    print("\n--- Registrar estudiante (HU03) ---")
    documento = input("Documento: ")
    nombre = input("Nombre completo: ")
    correo = input("Correo: ")
    programa = input("Programa académico: ")
    ok, mensaje = estudiantes.registrar_estudiante(documento, nombre, correo, programa)
    print(("✅ " if ok else "❌ ") + mensaje)


# ---------- Opciones de préstamos ----------

def opcion_registrar_prestamo():
    print("\n--- Registrar préstamo (HU04) ---")
    opcion_listar_equipos()
    codigo = input("\nCódigo del equipo a prestar: ")
    documento = input("Documento del estudiante: ")
    ok, mensaje = prestamos.registrar_prestamo(codigo, documento)
    print(("✅ " if ok else "❌ ") + mensaje)


def main():
    opciones = {
        "1": opcion_registrar_equipo,
        "2": opcion_listar_equipos,
        "3": opcion_registrar_estudiante,
        "4": opcion_registrar_prestamo,
    }

    while True:
        menu_principal()
        eleccion = input("Selecciona una opción: ").strip()

        if eleccion == "0":
            print("\n¡Hasta luego!")
            break

        accion = opciones.get(eleccion)
        if accion:
            try:
                accion()
            except Exception as error:
                print(f"⚠️  Ocurrió un error inesperado: {error}")
            pausar()
        else:
            print("Opción no válida, intenta de nuevo.")
            pausar()


if __name__ == "__main__":
    main()
