import veiculo

class Moto(veiculo.Veiculo):
    def __init__(self, cor, tipo_combustivel, potencia, qtd_passageiros):
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtd_passageiros = qtd_passageiros

    def abastecer(self, qtd_combustivel):
        if self._is_ligado:
            print('O veículo precisa estar desligado para ser abastecido.')
        else:
            if self._qtd_combustivel<30:
                self._qtd_combustivel += qtd_combustivel
                print('A moto foi abastecida.')
            else:
                print('O combustível da moto está cheio.')

    def pintar(self, cor):
        self._cor = cor
        print(f'A moto foi pintada com a cor {cor}.')