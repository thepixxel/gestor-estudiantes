"""
Subclase EstudianteForaneo.

Al igual que EstudianteBecado, hereda de Estudiante y reutiliza todos
sus atributos y metodos sin necesidad de reescribirlos. Aqui solo
agregamos lo que caracteriza a un estudiante que viene de fuera:
su ciudad de origen y donde esta viviendo mientras estudia.
"""

from estudiante import Estudiante


class EstudianteForaneo(Estudiante):
    """Estudiante que proviene de una ciudad diferente a donde se ubica la universidad."""

    def __init__(self, matricula, nombre, carrera, promedio=0.0, ciudad_origen="", alojamiento=""):
        # Igual que en EstudianteBecado, primero llamamos al constructor
        # del padre para inicializar los atributos comunes.
        super().__init__(matricula, nombre, carrera, promedio)
        # Y luego inicializamos lo que es propio de esta subclase.
        self.ciudad_origen = ciudad_origen
        self.alojamiento = alojamiento

    def resumen_alojamiento(self):
        """Regresa un texto breve con la informacion de donde vive el estudiante."""
        return (
            f"{self.nombre} viene de {self.ciudad_origen} "
            f"y actualmente vive en {self.alojamiento}."
        )

    def to_dict(self):
        """
        Extiende el to_dict de la clase base con los datos del estudiante foraneo.

        Misma estrategia que en EstudianteBecado: llamamos a super().to_dict()
        para no duplicar campos, y luego agregamos los nuestros.
        """
        datos = super().to_dict()
        datos["tipo"] = "foraneo"
        datos["ciudad_origen"] = self.ciudad_origen
        datos["alojamiento"] = self.alojamiento
        return datos

    @classmethod
    def from_dict(cls, datos):
        """Reconstruye un objeto EstudianteForaneo desde un diccionario."""
        return cls(
            matricula=datos["matricula"],
            nombre=datos["nombre"],
            carrera=datos["carrera"],
            promedio=datos.get("promedio", 0.0),
            ciudad_origen=datos.get("ciudad_origen", ""),
            alojamiento=datos.get("alojamiento", ""),
        )

    def __str__(self):
        return (
            f"[{self.matricula}] {self.nombre} - {self.carrera} "
            f"- Promedio: {self.promedio} | "
            f"De: {self.ciudad_origen} | Alojamiento: {self.alojamiento}"
        )
