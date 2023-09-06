import unittest
from ex2 import gerar_array, ordenar_array

class TestGeradorOrdenacaoErro(unittest.TestCase):

    def test_erro_1(self):
        with self.assertRaises(TypeError):
            ordenar_array("10000")

    def test_erro_2(self):
        with self.assertRaises(ValueError):
            ordenar_array([-100])

    def test_erro_3(self):
        with self.assertRaises(ValueError):
            ordenar_array([20001])

if __name__ == "__main__":
    unittest.main()
