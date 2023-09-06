import unittest
from ex4 import BibliotecaFiccaoCientifica

class TestBibliotecaErro(unittest.TestCase):

    def setUp(self):
        self.biblioteca = BibliotecaFiccaoCientifica()

    def test_erro_remover_livro_inexistente(self):
        with self.assertRaises(ValueError) as context:
            self.biblioteca.remover_livro("1984")

        self.assertEqual(str(context.exception), "O livro '1984' não está na biblioteca.")

    def test_erro_adicionar_livro_vazio(self):
        with self.assertRaises(ValueError) as context:
            self.biblioteca.adicionar_livro("")

        self.assertEqual(str(context.exception), "O título do livro não pode estar vazio.")

    def test_erro_adicionar_livro_existente(self):
        self.biblioteca.adicionar_livro("Duna")
        with self.assertRaises(ValueError) as context:
            self.biblioteca.adicionar_livro("Duna")

        self.assertEqual(str(context.exception), "O livro 'Duna' já está na biblioteca.")

if __name__ == "__main__":
    unittest.main()
