import os
import sys
from discos import Disco
from discos import ColeccionDiscos
from manejo_archivo import ManejoArchivoBytes


class MenuDiscos:
    """Opciones básicas para trabajar con discos."""
    
    def __init__(self):
        self.coleccion = ColeccionDiscos()
        self.archivador = ManejoArchivoBytes(self.coleccion)

    def menu(self):
        """Presenta las opciones del programa."""
        try:
            self.archivador.leer_datos()
        except (OSError):
            print("Error al leer en el archivo.")
            sys.exit(0)
        
        while True:
            print("\nMenú:")
            print("1- Crear un disco")
            print("2- Consultar un disco")
            print("3- Consultar duración total discos")
            print("4- Ver todos los discos")
            print("0- Salir")

            opcion = input("Ingrese su opción: ")
            
            if opcion == "1":
                self.crear_disco()
            elif opcion == "2":
                self.consultar_disco()
            elif opcion == "3":
                self.consultar_duracion_total()
            elif opcion == "4":
                self.mostrar_todos_discos()
            elif opcion == "0":
                self.guardar_datos()
                break
            else:
                print("Opción no válida, debe ser entre 0 y 4.")
    
    def crear_disco(self):
        """Pide al usuario los datos para crear un disco y guardarlo en la colección."""
        titulo = input("Título del disco: ")
        duracion = float(input("Duración en minutos: "))
        disco = Disco(titulo, duracion)
        self.coleccion.adicionar_disco(disco)
        print("Disco creado.")

    def consultar_disco(self):
        """Busca un disco por su título y muestra su información."""
        titulo = input("Título del disco a buscar: ")
        disco = self.coleccion.consultar_disco(titulo)
        if disco:
            print(disco)
        else:
            print("No se encuentra ese disco.")

    def mostrar_todos_discos(self):
        """Muestra la información de todos los discos registrados."""
        discos = self.coleccion.get_discos()
        if not discos:
            print("No hay discos registrados.")
        else:
            for disco in discos:
                print(disco)

    def consultar_duracion_total(self):
        """Consulta y muestra la duración de todos los discos."""
        print(f"La duración total de los discos es: {self.coleccion.get_duracion_total()} minutos.")
    
    def guardar_datos(self):
        try:
            self.archivador.escribir_datos()
            print("Datos guardados.")
        except (OSError):
            print("Error al escribir en el archivo.")
            sys.exit(0)


if __name__ == "__main__":
    menu_discos = MenuDiscos()
    menu_discos.menu()

