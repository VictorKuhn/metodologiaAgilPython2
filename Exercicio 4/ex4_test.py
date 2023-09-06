import unittest
from ex4 import BibliotecaFiccaoCientifica

class TestBibliotecaSucesso(unittest.TestCase):

    def setUp(self):
        self.biblioteca = BibliotecaFiccaoCientifica()

    def test_adicionar_livro(self):
        self.biblioteca.adicionar_livro("Duna")
        self.assertEqual(self.biblioteca.listar_livros(), ["Duna"])

    def test_remover_livro(self):
        self.biblioteca.adicionar_livro("Neuromancer")
        self.biblioteca.remover_livro("Neuromancer")
        self.assertEqual(self.biblioteca.listar_livros(), [])

    def test_listar_livros(self):
        self.biblioteca.adicionar_livro("Fundação")
        self.biblioteca.adicionar_livro("Solaris")
        self.assertEqual(self.biblioteca.listar_livros(), ["Fundação", "Solaris"])

if __name__ == "__main__":
    unittest.main()
