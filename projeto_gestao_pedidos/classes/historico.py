# import ..classes/

# Classe Historico
class Historico:
    # Construtor
    def __init__(self, pedido):
        self.__pedido = []

    # Getters & Setters
    def get_pedido(self):  # mostrando o pedido
        return self.__pedido

    def set_pedido(self, pedido):  # alterando o pedido
        self.__pedido = pedido

    # Outros Métodos
    # def inserir_pedido(self, pedido):

    # def calcular_faturamento(self):
