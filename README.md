# Mini Gestor de Estudiantes

Proyecto desarrollado para la actividad **Actividad Formativa 2 - Desarrollo de una Aplicación Simple en Línea**, de la materia **Programación Orientada a Objetos**, Ingeniería en Desarrollo de Software, UCNL.

> **Nota sobre el lenguaje:** la guía de la actividad menciona Java o PHP como opciones, pero el proyecto fue realizado en **Python** con autorización del profesor de la materia.

## ¿Qué hace el proyecto?

Es una aplicación de consola muy simple que permite administrar una lista de estudiantes: agregarlos, listarlos, buscarlos por matrícula, actualizar su promedio y eliminarlos. Los datos se guardan en un archivo JSON, así que no se pierden cada vez que se cierra el programa.

El objetivo principal es practicar los conceptos básicos de Programación Orientada a Objetos:

- Declaración de clases y atributos.
- Constructores (`__init__`).
- Instanciación de objetos.
- Implementación y uso de métodos.

## Estructura del proyecto

```
gestor-estudiantes/
│
├── estudiante.py            # Clase Estudiante
├── gestor_estudiantes.py     # Clase GestorEstudiantes
├── main.py                   # Programa principal (menú e interacción con el usuario)
├── .gitignore
└── README.md
```

## Clases del proyecto

### `Estudiante` (estudiante.py)

Representa a un solo estudiante. Guarda sus datos básicos como atributos y tiene métodos para actualizar el promedio y para convertirse en diccionario (útil para guardar y leer el JSON).

**Atributos:**
- `matricula`
- `nombre`
- `carrera`
- `promedio`

**Métodos principales:**
- `__init__()` – constructor, recibe los datos del estudiante.
- `actualizar_promedio()` – cambia el promedio, validando que esté entre 0 y 100.
- `to_dict()` / `from_dict()` – convierten el objeto a diccionario y viceversa.
- `__str__()` – define cómo se muestra el estudiante al imprimirlo.

### `GestorEstudiantes` (gestor_estudiantes.py)

Administra la colección completa de estudiantes. Es la clase encargada de la lógica del sistema (agregar, buscar, eliminar) y de guardar/cargar la información en el archivo JSON.

**Métodos principales:**
- `__init__()` – constructor, recibe la ruta del archivo donde se guardan los datos y carga lo que ya exista.
- `agregar_estudiante()`
- `eliminar_estudiante()`
- `buscar_estudiante()`
- `actualizar_promedio()`
- `listar_estudiantes()`
- `guardar_datos()` / `cargar_datos()` – manejan la persistencia en JSON.

### `main.py`

Es el punto de entrada del programa. Aquí se instancia el objeto `GestorEstudiantes` y se muestra un menú en la terminal para que el usuario pueda probar todos los métodos de las clases.

## Cómo ejecutarlo localmente

Se necesita tener **Python 3** instalado (no se requieren librerías externas, solo la librería estándar).

```bash
python3 main.py
```

Al ejecutarlo aparecerá un menú como este:

```
--- MINI GESTOR DE ESTUDIANTES ---
1. Agregar estudiante
2. Listar estudiantes
3. Buscar estudiante
4. Actualizar promedio
5. Eliminar estudiante
6. Salir
```

La primera vez que se agrega un estudiante, el programa crea automáticamente una carpeta `datos/` con un archivo `estudiantes.json` donde se guarda la información.

## Conceptos de POO aplicados

| Concepto | Dónde se aplica |
|---|---|
| Clase y atributos | `Estudiante` y `GestorEstudiantes` |
| Constructor | `__init__()` en ambas clases |
| Instanciación de objetos | Se crean objetos `Estudiante` en `main.py` y un objeto `GestorEstudiantes` que los administra |
| Métodos | Todos los comportamientos del sistema (agregar, buscar, actualizar, eliminar, guardar) |

## Autor

Israel Florido Montero — Ingeniería en Desarrollo de Software, UCNL.
