import veiculo

class Carro(veiculo.Veiculo):
    def __init__(self, cor, tipo_combustivel, potencia, qtd_portas):
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtd_portas = qtd_portas

    def abastecer(self, qtd_combustivel):
        if self._is_ligado:
            print('O veículo precisa estar desligado para ser abastecido.')
        else:
            self._qtd_combustivel += qtd_combustivel
            print('O carro foi abastecido.')

    def pintar(self, cor):
        self._cor = cor
        print(f'O carro foi pintado com a cor {cor}.')
