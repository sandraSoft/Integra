class Disco:
    """Un disco o canción que se puede escuchar en un reproductor."""
    
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion

    def __str__(self):
        return f"Disco {self.titulo} que dura: {self.duracion} minutos"


class ColeccionDiscos:
    """Todos los discos que tiene la persona."""
    
    def __init__(self):
        self.discos = []

    def adicionar_disco(self, disco):
        """Guardar un disco en la colección."""
        self.discos.append(disco)

    def consultar_disco(self, titulo):
        """Busca un disco en la colección por su título."""
        for disco in self.discos:
            if disco.titulo == titulo:
                return disco
        return None

    def get_duracion_total(self):
        """Calcula el tiempo total de los discos de la colección."""
        return sum(disco.duracion for disco in self.discos)

    def get_discos(self):
        return self.discos
        