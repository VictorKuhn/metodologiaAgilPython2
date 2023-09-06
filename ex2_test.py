import unittest
from ex2 import gerar_array, ordenar_array

class TestGeradorOrdenacaoSucesso(unittest.TestCase):

    def test_tamanho_do_array(self):
        array = gerar_array()
        self.assertEqual(len(array), 20000)

    def test_valores_no_intervalo(self):
        array = gerar_array()
        for valor in array:
            self.assertTrue(-999999 <= valor <= 999999)

    def test_tipo_dos_valores(self):
        array = gerar_array()
        for valor in array:
            self.assertIsInstance(valor, int)

    def test_ordenacao(self):
        array = gerar_array()
        array_ordenado = ordenar_array(array)
        self.assertEqual(array_ordenado, sorted(array))

if __name__ == "__main__":
    unittest.main()
