"""
Subclase EstudianteBecado.

Hereda de Estudiante, lo que significa que ya trae de casa todo lo que
la clase base tiene: matricula, nombre, carrera, promedio y sus metodos.
Nosotros solo agregamos lo que es exclusivo de un estudiante becado:
el tipo de beca que tiene y la logica para saber si la mantiene o no.
"""

from estudiante import Estudiante


class EstudianteBecado(Estudiante):
    """Estudiante que cuenta con una beca dentro del sistema."""

    # Este es el promedio minimo para conservar la beca. Lo ponemos como
    # atributo de clase (no de instancia) porque aplica igual para todos
    # los becados, sin importar a quien estemos revisando.
    PROMEDIO_MINIMO = 80.0

    def __init__(self, matricula, nombre, carrera, promedio=0.0, tipo_beca="academica"):
        # Llamamos al constructor de Estudiante para no repetir el codigo
        # que ya existe ahi. super() nos da acceso a la clase padre.
        super().__init__(matricula, nombre, carrera, promedio)
        # Solo agregamos lo que es nuevo en esta subclase.
        self.tipo_beca = tipo_beca

    def mantiene_beca(self):
        """Regresa True si el promedio es suficiente para conservar la beca."""
        return self.promedio >= self.PROMEDIO_MINIMO

    def to_dict(self):
        """
        Extiende el to_dict de la clase base agregando los campos de la beca.

        Llamamos a super().to_dict() para no reescribir los campos comunes,
        y luego simplemente agregamos o sobreescribimos lo que necesitamos.
        """
        datos = super().to_dict()
        datos["tipo"] = "becado"
        datos["tipo_beca"] = self.tipo_beca
        return datos

    @classmethod
    def from_dict(cls, datos):
        """Reconstruye un objeto EstudianteBecado desde un diccionario."""
        return cls(
            matricula=datos["matricula"],
            nombre=datos["nombre"],
            carrera=datos["carrera"],
            promedio=datos.get("promedio", 0.0),
            tipo_beca=datos.get("tipo_beca", "academica"),
        )

    def __str__(self):
        # Reutilizamos el formato del padre y le agregamos la info de la beca.
        # El estado nos dice rapido si el estudiante esta bien o en riesgo.
        estado = "activa" if self.mantiene_beca() else "en riesgo"
        return (
            f"[{self.matricula}] {self.nombre} - {self.carrera} "
            f"- Promedio: {self.promedio} | Beca {self.tipo_beca} ({estado})"
        )
