## Classe Cliente
class Cliente:
    # Construtor
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco # vinculado ao obj da classe Endereco
