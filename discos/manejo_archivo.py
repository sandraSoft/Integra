import os
import pickle

class ManejoArchivoBytes:
    """Escribir y leer datos de un archivo."""
    
    ARCHIVO = "discos/misDiscos.dat"

    def __init__(self, coleccion):
        self.coleccion = coleccion

    def escribir_datos(self):
        """Escribe los datos de todos los discos en un archivo."""
        with open(self.ARCHIVO, "wb") as archivo:
            pickle.dump(self.coleccion.discos, archivo)

    def leer_datos(self):
        """Leer de un archivo los datos de varios discos."""
        if os.path.exists(self.ARCHIVO) and os.path.getsize(self.ARCHIVO) > 0:
            with open(self.ARCHIVO, "rb") as archivo:
                self.coleccion.discos = pickle.load(archivo)
