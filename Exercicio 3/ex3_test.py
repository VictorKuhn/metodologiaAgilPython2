import unittest
from ex3 import converter_massa_lunar, converter_distancia_marte

class TestConversorErro(unittest.TestCase):

    def test_erro_massa_lunar(self):
        with self.assertRaises(ValueError):
            converter_massa_lunar(-6)

    def test_erro_distancia_marte(self):
        with self.assertRaises(ValueError):
            converter_distancia_marte(-1000)

if __name__ == "__main__":
    unittest.main()