# Mini Gestor de Estudiantes

Proyecto desarrollado para la materia **Programación Orientada a Objetos**, Ingeniería en Desarrollo de Software, UCNL.

> **Nota sobre el lenguaje:** la guía de la actividad menciona Java o PHP como opciones, pero el proyecto fue realizado en **Python**.

## ¿Qué hace el proyecto?

Es una aplicación de consola que permite administrar una lista de estudiantes: agregarlos, listarlos, buscarlos por matrícula, actualizar su promedio y eliminarlos. Los datos se guardan en un archivo JSON para que no se pierdan al cerrar el programa.

## Actividades cubiertas

| Actividad | Concepto principal |
|---|---|
| Actividad Formativa 2 | Clases, objetos, métodos y constructores |
| Actividad Formativa 3 | Herencia: subclases `EstudianteBecado` y `EstudianteForaneo` |

## Estructura del proyecto

```
gestor-estudiantes/
│
├── estudiante.py              # Clase base Estudiante
├── estudiante_becado.py       # Subclase EstudianteBecado (hereda de Estudiante)
├── estudiante_foraneo.py      # Subclase EstudianteForaneo (hereda de Estudiante)
├── gestor_estudiantes.py      # Clase GestorEstudiantes
├── main.py                    # Programa principal
├── .gitignore
└── README.md
```

## Clases del proyecto

### `Estudiante` (clase base)

Representa a un estudiante con sus datos básicos.

**Atributos:** `matricula`, `nombre`, `carrera`, `promedio`

**Métodos:** `__init__()`, `actualizar_promedio()`, `to_dict()`, `from_dict()`, `__str__()`

---

### `EstudianteBecado` (hereda de `Estudiante`)

Extiende la clase base con información sobre la beca del estudiante.

**Atributos propios:** `tipo_beca`  
**Constante de clase:** `PROMEDIO_MINIMO = 80.0`

**Métodos propios:** `mantiene_beca()` — regresa `True` si el promedio supera el mínimo requerido.

---

### `EstudianteForaneo` (hereda de `Estudiante`)

Extiende la clase base con información sobre el origen y alojamiento del estudiante.

**Atributos propios:** `ciudad_origen`, `alojamiento`

**Métodos propios:** `resumen_alojamiento()` — regresa un texto con el lugar de origen y dónde vive.

---

### `GestorEstudiantes`

Administra la colección de estudiantes (de cualquier tipo) y la persistencia en JSON. Al cargar los datos, usa el campo `tipo` de cada registro para saber qué clase instanciar.

## Herencia aplicada

```
Estudiante  (clase base)
├── EstudianteBecado
└── EstudianteForaneo
```

Las subclases llaman a `super().__init__()` para reutilizar el constructor de `Estudiante`, y sobreescriben `to_dict()`, `from_dict()` y `__str__()` para manejar sus campos adicionales.

## Cómo ejecutarlo

Se necesita **Python 3** instalado. No requiere librerías externas.

```bash
python3 main.py
```

Al agregar un estudiante, el programa pregunta el tipo:

```
¿Que tipo de estudiante quieres agregar?
  1. Regular
  2. Becado
  3. Foraneo
```

## Conceptos de POO aplicados

| Concepto | Dónde se aplica |
|---|---|
| Clase y atributos | `Estudiante`, `EstudianteBecado`, `EstudianteForaneo`, `GestorEstudiantes` |
| Constructor | `__init__()` en todas las clases; las subclases llaman a `super().__init__()` |
| Instanciación de objetos | `main.py` instancia el tipo correcto según la elección del usuario |
| Métodos | Definidos en la clase base y extendidos o sobreescritos en las subclases |
| Herencia | `EstudianteBecado` y `EstudianteForaneo` heredan de `Estudiante` |
| Reutilización de código | Las subclases reutilizan atributos y métodos de la clase base sin reescribirlos |

## Rama de desarrollo (Actividad 3)

Los cambios de herencia se subieron en la rama `feature/herencia`:

```bash
git checkout -b feature/herencia
git add .
git commit -m "Agrega herencia: EstudianteBecado y EstudianteForaneo"
git push -u origin feature/herencia
```

## Autor

Israel Florido Montero — Ingeniería en Desarrollo de Software, UCNL.
