"""
Este archivo contiene la clase GestorEstudiantes.

Esta clase es la que realmente administra a los estudiantes: permite
agregarlos, eliminarlos, buscarlos, listarlos y actualizar su promedio.
Tambien se encarga de guardar y cargar la informacion desde un archivo
JSON, para que los datos no se pierdan cada vez que cerramos el programa.

Desde la actividad 3 tambien sabe diferenciar entre tipos de estudiante
al cargar el JSON, para reconstruir el objeto correcto en cada caso.
"""

import json
import os

from estudiante import Estudiante
from estudiante_becado import EstudianteBecado
from estudiante_foraneo import EstudianteForaneo


class GestorEstudiantes:
    """Administra una coleccion de objetos Estudiante y sus subclases."""

    def __init__(self, ruta_archivo="datos/estudiantes.json"):
        # Guardamos en que archivo vamos a leer/escribir los datos y
        # preparamos una lista vacia donde van a vivir los objetos
        # Estudiante mientras el programa esta corriendo.
        self.ruta_archivo = ruta_archivo
        self.estudiantes = []
        self.cargar_datos()

    def agregar_estudiante(self, estudiante):
        """Agrega un nuevo estudiante, evitando matriculas repetidas."""
        if self.buscar_estudiante(estudiante.matricula):
            print(f"Ya existe un estudiante con la matricula {estudiante.matricula}.")
            return False

        self.estudiantes.append(estudiante)
        self.guardar_datos()
        return True

    def eliminar_estudiante(self, matricula):
        """Elimina al estudiante que tenga la matricula indicada."""
        estudiante = self.buscar_estudiante(matricula)

        if estudiante is None:
            print(f"No se encontro ningun estudiante con la matricula {matricula}.")
            return False

        self.estudiantes.remove(estudiante)
        self.guardar_datos()
        return True

    def buscar_estudiante(self, matricula):
        """Busca un estudiante por matricula y regresa el objeto si lo encuentra."""
        for estudiante in self.estudiantes:
            if estudiante.matricula == matricula:
                return estudiante
        return None

    def actualizar_promedio(self, matricula, nuevo_promedio):
        """Busca a un estudiante y le actualiza el promedio usando su propio metodo."""
        estudiante = self.buscar_estudiante(matricula)

        if estudiante is None:
            print(f"No se encontro ningun estudiante con la matricula {matricula}.")
            return False

        actualizado = estudiante.actualizar_promedio(nuevo_promedio)
        if actualizado:
            self.guardar_datos()
        else:
            print("El promedio debe estar entre 0 y 100.")

        return actualizado

    def listar_estudiantes(self):
        """Muestra en pantalla a todos los estudiantes registrados."""
        if not self.estudiantes:
            print("Todavia no hay estudiantes registrados.")
            return

        for estudiante in self.estudiantes:
            print(estudiante)

    def guardar_datos(self):
        """Convierte la lista de objetos en diccionarios y los guarda en JSON."""
        carpeta = os.path.dirname(self.ruta_archivo)
        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta)

        datos = [estudiante.to_dict() for estudiante in self.estudiantes]

        with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def cargar_datos(self):
        """
        Carga los estudiantes desde el archivo JSON, reconstruyendo
        el tipo correcto de objeto segun el campo 'tipo' de cada registro.

        Esto es posible gracias a la herencia: todos los tipos comparten
        la misma interfaz (metodos y atributos base), pero cada uno sabe
        como construirse a si mismo con sus propios datos adicionales.
        """
        if not os.path.exists(self.ruta_archivo):
            # Si es la primera vez que se ejecuta el programa, el archivo
            # todavia no existe, asi que simplemente empezamos con una
            # lista vacia en lugar de marcar un error.
            return

        with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
            try:
                datos = json.load(archivo)
            except json.JSONDecodeError:
                # Si el archivo esta vacio o dañado, mejor empezamos
                # de cero en lugar de que el programa se caiga.
                datos = []

        self.estudiantes = []
        for item in datos:
            # Revisamos el campo "tipo" para saber que clase instanciar.
            # Si no tiene tipo (registros viejos), lo tratamos como regular.
            tipo = item.get("tipo", "regular")
            if tipo == "becado":
                self.estudiantes.append(EstudianteBecado.from_dict(item))
            elif tipo == "foraneo":
                self.estudiantes.append(EstudianteForaneo.from_dict(item))
            else:
                self.estudiantes.append(Estudiante.from_dict(item))
