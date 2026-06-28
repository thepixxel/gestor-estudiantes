"""
Este archivo contiene la clase Estudiante.

La idea es representar a un estudiante con la informacion basica que
normalmente se pediria en un sistema escolar: matricula, nombre, carrera
y promedio. Cada vez que creamos un objeto Estudiante, estamos
instanciando esta clase con datos especificos.
"""


class Estudiante:
    """Representa a un estudiante dentro del sistema."""

    def __init__(self, matricula, nombre, carrera, promedio=0.0):
        # El constructor se ejecuta automaticamente al crear el objeto.
        # Aqui solo guardamos los datos que recibimos en los atributos
        # del objeto, para poder usarlos despues en los demas metodos.
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.promedio = promedio

    def actualizar_promedio(self, nuevo_promedio):
        """Cambia el promedio del estudiante, validando que sea un valor valido."""
        if 0 <= nuevo_promedio <= 100:
            self.promedio = nuevo_promedio
            return True
        # Si el promedio no esta en el rango esperado, no lo guardamos
        # y avisamos al metodo que lo llamo que algo salio mal.
        return False

    def to_dict(self):
        """
        Convierte el objeto en un diccionario.

        Esto nos sirve para poder guardar la informacion del estudiante
        en un archivo JSON, ya que JSON no entiende objetos de Python,
        solo entiende estructuras simples como diccionarios y listas.
        """
        return {
            "matricula": self.matricula,
            "nombre": self.nombre,
            "carrera": self.carrera,
            "promedio": self.promedio,
        }

    @classmethod
    def from_dict(cls, datos):
        """
        Crea un objeto Estudiante a partir de un diccionario.

        Es lo contrario de to_dict: lo usamos cuando leemos el archivo
        JSON y necesitamos volver a construir los objetos Estudiante
        con la informacion que ya estaba guardada.
        """
        return cls(
            matricula=datos["matricula"],
            nombre=datos["nombre"],
            carrera=datos["carrera"],
            promedio=datos.get("promedio", 0.0),
        )

    def __str__(self):
        # Este metodo define como se ve el objeto cuando lo imprimimos
        # con print(). Sin esto, Python mostraria algo como
        # "<Estudiante object at 0x...>", que no dice nada util.
        return (
            f"[{self.matricula}] {self.nombre} - {self.carrera} "
            f"- Promedio: {self.promedio}"
        )
