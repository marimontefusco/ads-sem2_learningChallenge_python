## Classe Pedido
class Pedido:
    # Construtor
    def __init__(self, cliente, altura, largura, frase, cor_placa, cor_letra, valor_fixo_material, valor_fixo_letra, valor_total_float):
        self.cliente = cliente
        self.altura = altura
        self.largura = largura
        self.fase = frase
        self.cor_palca = cor_placa
        self.cor_letra = cor_letra
        self.__valor_fixo_material = valor_fixo_material  # atributo privado
        self.__valor_fixo_letra = valor_fixo_letra  # atributo privado
        self.__valor_total_float = valor_total_float  # atributo privado

    # Getters & Setters
    def get_valor_fixo_material(self):
        

    # Outros Métodos
    def get_valor_total(self, area, custo_material, custo_desenho, valor_placa):
        
        
