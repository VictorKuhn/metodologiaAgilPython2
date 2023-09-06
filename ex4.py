class BibliotecaFiccaoCientifica:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo):
        self.livros.append(titulo)

    def remover_livro(self, titulo):
        if titulo in self.livros:
            self.livros.remove(titulo)
        else:
            raise ValueError(f"O livro '{titulo}' não está na biblioteca.")

    def listar_livros(self):
        return self.livros