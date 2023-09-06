import unittest
from ex3 import converter_massa_lunar, converter_distancia_marte

class TestConversorSucesso(unittest.TestCase):

    def test_converter_massa_lunar(self):
        self.assertEqual(converter_massa_lunar(12), 2)

    def test_converter_distancia_marte(self):
        self.assertEqual(converter_distancia_marte(1000), 2656.763925729442)

if __name__ == "__main__":
    unittest.main()