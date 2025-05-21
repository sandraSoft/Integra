'''Módulo de pruebas para la clase Restaurante'''
import unittest
from unittest.mock import MagicMock
from restaurante import Restaurante, Pedido

# TestRestaurante es una clase de prueba unitaria para la clase Restaurante.
class TestRestaurante(unittest.TestCase):
    """Pruebas unitarias para la clase Restaurante."""
    def setUp(self):
        # Mock menu with obtener_plato method
        self.menu = MagicMock()
        self.restaurante = Restaurante(self.menu)

    def test_crear_pedido(self):
        pedido = self.restaurante.crear_pedido()
        self.assertIn(pedido, self.restaurante.pedidos)
        self.assertIsInstance(pedido, Pedido)

    def test_agregar_plato_a_pedido_exitoso(self):
        pedido = self.restaurante.crear_pedido()
        plato_mock = MagicMock()
        self.menu.obtener_plato.return_value = plato_mock

        resultado = self.restaurante.agregar_plato_a_pedido(pedido, "Pizza")
        self.assertTrue(resultado)
        self.assertIn(plato_mock, pedido.platos)
        self.menu.obtener_plato.assert_called_with("Pizza")

    def test_agregar_plato_a_pedido_fallido(self):
        pedido = self.restaurante.crear_pedido()
        self.menu.obtener_plato.return_value = None

        resultado = self.restaurante.agregar_plato_a_pedido(pedido, "NoExiste")
        self.assertFalse(resultado)
        self.assertEqual(len(pedido.platos), 0)
        self.menu.obtener_plato.assert_called_with("NoExiste")

if __name__ == "__main__":
    unittest.main()
