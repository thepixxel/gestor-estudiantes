"""
Programa principal del Mini Gestor de Estudiantes.

Aqui es donde se instancian los objetos y se prueban los metodos de
las clases Estudiante y GestorEstudiantes. El programa muestra un menu
en la terminal para que el usuario pueda agregar, listar, buscar,
actualizar y eliminar estudiantes.
"""

from estudiante import Estudiante
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
    print("\nIngresa los datos del nuevo estudiante:")
    matricula = input("Matricula: ")
    nombre = input("Nombre: ")
    carrera = input("Carrera: ")
    promedio = float(input("Promedio (0-100): "))

    # Aqui se instancia un nuevo objeto de la clase Estudiante con los
    # datos que acaba de escribir el usuario.
    nuevo_estudiante = Estudiante(matricula, nombre, carrera, promedio)

    if gestor.agregar_estudiante(nuevo_estudiante):
        print("Estudiante agregado correctamente.")


def buscar_estudiante(gestor):
    matricula = input("\nMatricula a buscar: ")
    estudiante = gestor.buscar_estudiante(matricula)

    if estudiante:
        print("Estudiante encontrado:")
        print(estudiante)
    else:
        print("No se encontro ningun estudiante con esa matricula.")


def actualizar_promedio(gestor):
    matricula = input("\nMatricula del estudiante a actualizar: ")
    nuevo_promedio = float(input("Nuevo promedio (0-100): "))
    gestor.actualizar_promedio(matricula, nuevo_promedio)


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
