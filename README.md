# Sistema de Préstamo de Equipos Tecnológicos

Desarrollado en Python aplicando el marco de trabajo **Scrum**, como parte de la actividad evaluativa del curso *Scrum y Metodologías Ágiles*.

**Institución:** Colegio San Marín
**Equipo:** Juan David, Christian y Daniela

## Alcance de este Sprint

Del Product Backlog original (8 historias de usuario), el equipo seleccionó las siguientes 4 para este Sprint:

- **HU01** — Registrar equipos tecnológicos
- **HU02** — Consultar equipos registrados y su disponibilidad
- **HU03** — Registrar estudiantes
- **HU04** — Registrar el préstamo de un equipo a un estudiante

Las historias HU05 (devolución), HU06 (consultar préstamos activos), HU07 (historial) y HU08 (eliminar equipo) quedan fuera del alcance de este Sprint.

**Nota sobre la duración:** el instrumento sugiere un Sprint de 1 semana, pero el docente indicó realizar el Sprint en 1 día. La planificación, historias seleccionadas y evidencias fueron ajustadas a ese tiempo real.

## Estructura del proyecto

```
proyecto/
├── main.py           # Menú de consola, punto de entrada del programa
├── equipos.py        # Registrar y listar equipos (HU01, HU02)
├── estudiantes.py    # Registrar y listar estudiantes (HU03)
├── prestamos.py      # Registrar préstamo (HU04)
├── archivos.py       # Utilidades de lectura/escritura en JSON
└── datos/
    ├── equipos.json
    ├── estudiantes.json
    └── prestamos.json

## Historias de usuario cubiertas

| Historia | Descripción | Módulo |
|---|---|---|
| HU01 | Registrar equipos tecnológicos | `equipos.py` |
| HU02 | Consultar equipos y su disponibilidad | `equipos.py` |
| HU03 | Registrar estudiantes | `estudiantes.py` |
| HU04 | Registrar préstamo de un equipo | `prestamos.py` |

## Validaciones implementadas

- No se permite registrar un equipo con campos vacíos.
- No se permite registrar un estudiante con documento duplicado, no numérico o correo con formato inválido.
- No se permite prestar un equipo que no existe o que no está disponible.
- No se permite registrar un préstamo si el estudiante no está registrado.

## Persistencia

Los datos se almacenan en archivos JSON dentro de la carpeta `datos/`, por lo que la información se conserva entre ejecuciones del programa.

## Equipo de desarrollo

Proyecto desarrollado en el marco de un Sprint de Scrum de una semana. Consultar las actas de Sprint Planning, Daily Scrum, Sprint Review y Retrospectiva en las carpetas correspondientes del repositorio de entrega.
