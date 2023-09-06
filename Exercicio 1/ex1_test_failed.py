import unittest
from ex1 import gerar_array

class TestGeradorErro(unittest.TestCase):

    def test_erro_1(self):
        with self.assertRaises(TypeError):
            gerar_array("10000")

    def test_erro_2(self):
        with self.assertRaises(ValueError):
            gerar_array(-100)

    def test_erro_3(self):
        with self.assertRaises(ValueError):
            gerar_array(20001)

if __name__ == "__main__":
    unittest.main()
