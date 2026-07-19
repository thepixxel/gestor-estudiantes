"""
Programa principal del Mini Gestor de Estudiantes.

Aqui es donde se instancian los objetos y se prueban los metodos de
las clases. Desde la actividad 3, el menu permite crear tres tipos de
estudiantes: regular, becado y foraneo, cada uno instanciado
desde su clase correspondiente.
"""

from estudiante import Estudiante
from estudiante_becado import EstudianteBecado
from estudiante_foraneo import EstudianteForaneo
from gestor_estudiantes import GestorEstudiantes


def mostrar_menu():
    print("\n--- MINI GESTOR DE ESTUDIANTES ---")
    print("1. Agregar estudiante")
    print("2. Listar estudiantes")
    print("3. Buscar estudiante")
    print("4. Actualizar promedio")
    print("5. Eliminar estudiante")
    print("6. Salir")


def agregar_estudiante(gestor):
    print("\n¿Que tipo de estudiante quieres agregar?")
    print("  1. Regular")
    print("  2. Becado")
    print("  3. Foraneo")
    tipo = input("Tipo: ")

    if tipo not in ("1", "2", "3"):
        print("Tipo no valido.")
        return

    print("\nIngresa los datos del estudiante:")
    matricula = input("Matricula: ")
    nombre = input("Nombre: ")
    carrera = input("Carrera: ")
    promedio = float(input("Promedio (0-100): "))

    if tipo == "1":
        # Se instancia la clase base directamente.
        nuevo_estudiante = Estudiante(matricula, nombre, carrera, promedio)

    elif tipo == "2":
        # Se instancia la subclase EstudianteBecado, que hereda de Estudiante
        # y ademas recibe el tipo de beca como dato extra.
        tipo_beca = input("Tipo de beca (academica / deportiva / economica): ")
        nuevo_estudiante = EstudianteBecado(matricula, nombre, carrera, promedio, tipo_beca)

    elif tipo == "3":
        # Se instancia la subclase EstudianteForaneo, que hereda de Estudiante
        # y ademas recibe ciudad de origen y tipo de alojamiento.
        ciudad_origen = input("Ciudad de origen: ")
        alojamiento = input("Alojamiento (ej. casa de huespedes, departamento): ")
        nuevo_estudiante = EstudianteForaneo(
            matricula, nombre, carrera, promedio, ciudad_origen, alojamiento
        )

    if gestor.agregar_estudiante(nuevo_estudiante):
        print("Estudiante agregado correctamente.")


def buscar_estudiante(gestor):
    matricula = input("\nMatricula a buscar: ")
    estudiante = gestor.buscar_estudiante(matricula)

    if estudiante:
        print("Estudiante encontrado:")
        print(estudiante)
        # Si el objeto es un EstudianteBecado podemos llamar a su metodo
        # exclusivo para saber el estado de su beca.
        if isinstance(estudiante, EstudianteBecado):
            estado = "activa" if estudiante.mantiene_beca() else "en riesgo"
            print(f"  Estado de beca: {estado} (minimo requerido: {EstudianteBecado.PROMEDIO_MINIMO})")
        # Si es foraneo, mostramos el resumen de alojamiento.
        elif isinstance(estudiante, EstudianteForaneo):
            print(f"  {estudiante.resumen_alojamiento()}")
    else:
        print("No se encontro ningun estudiante con esa matricula.")


def actualizar_promedio(gestor):
    matricula = input("\nMatricula del estudiante a actualizar: ")
    nuevo_promedio = float(input("Nuevo promedio (0-100): "))
    if gestor.actualizar_promedio(matricula, nuevo_promedio):
        print("Promedio actualizado.")


def eliminar_estudiante(gestor):
    matricula = input("\nMatricula del estudiante a eliminar: ")
    if gestor.eliminar_estudiante(matricula):
        print("Estudiante eliminado correctamente.")


def main():
    # Se crea un solo objeto GestorEstudiantes que se va a usar durante
    # toda la ejecucion del programa. Este objeto carga automaticamente
    # los datos guardados previamente en el archivo JSON.
    gestor = GestorEstudiantes()

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            agregar_estudiante(gestor)
        elif opcion == "2":
            print()
            gestor.listar_estudiantes()
        elif opcion == "3":
            buscar_estudiante(gestor)
        elif opcion == "4":
            actualizar_promedio(gestor)
        elif opcion == "5":
            eliminar_estudiante(gestor)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida, intenta de nuevo.")


if __name__ == "__main__":
    main()
