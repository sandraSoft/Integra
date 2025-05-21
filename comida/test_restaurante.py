import unittest
from unittest.mock import MagicMock
import menu

class TestRestaurante(unittest.TestCase):
    """Pruebas unitarias para el módulo menu."""
    
    def setUp(self):
        """Configura un mock de Plato."""
        self.plato1 = Plato('Arroz chino', 13000)
        self.plato2 = Plato('Arroz paisa', 17000)
        self.mock_menu = MagicMock()
        self.mock_pedido = MagicMock()
        self.restaurante = Restaurante(self.mock_menu)


    def test_agregar_plato_a_pedido_exitoso(self):
        """Debe retornar True cuando se agrega exitosamente un plato al pedido."""
        self.mock_menu.obtener_plato.return_value = self.plato1

        resultado = self.restaurante.agregar_plato_a_pedido(self.mock_pedido, self.plato1.nombre)
        self.assertTrue(resultado)
        # Falta verificar que se llamó a self.mock_pedido.agregar_plato con "assertCall" (?)

    def test_agregar_plato_a_pedido_ya_existente(self):
        """Debe retornar False cuando el plato a agregar ya existe en el pedido."""
        self.mock_menu.obtener_plato.return_value = self.plato1
        self.mock_pedido.agregar_plato.return_value = False

        resultado = self.restaurante.agregar_plato_a_pedido(self.mock_pedido, self.plato1.nombre)
        self.assertFalse(resultado)


if __name__ == "__main__":
    unittest.main()