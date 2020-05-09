import abc # biblioteca para permitir que classes e métodos sejam abstratos
import interface_veiculo

class Veiculo(interface_veiculo.InterfaceVeiculo,abc.ABC):
    """ A classe Carro é utilizada para instanciar novos carros no programa
        É uma classe abstrata devido à utilização do método ABC da biblioteca abc"""
    def __init__(self, cor, tipo_combustivel, potencia):
        self._cor = cor
        self.__tipo_combustivel = tipo_combustivel
        self.__potencia = potencia
        self._qtd_combustivel = 0
        self._is_ligado = False
        self.__velocidade = 0

    def __del__(self):
        print('O objeto foi removido da memória.')

    #@abc.abstractmethod # em classes abstradas, métodos abstrados devem ser sobrescritos nas classes-filhas
    #def pintar(self,cor):
    #    self._cor = cor

    @property
    def cor(self):
        return self._cor

    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def qtd_combustivel(self):
        return self._qtd_combustivel
    
    def abastecer(self, qtd_combustivel):
        """ O método abastecer recebe como parâmentro a quantidade de combustível e incrementa no atributo qtd_combustivel do objeto Carro"""
        if self._is_ligado:
            print('O veículo precisa estar desligado para ser abastecido.')
        else:
            self._qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self._is_ligado:
            print('O veículo já está ligado.')
        else:
            self._is_ligado = True
            print('O veículo foi ligado.')

    def desligar(self):
        if self._is_ligado==False:
            print('O veículo já está desligado.')
        else:
            self._is_ligado = False
            self.__velocidade = 0
            print('O veículo foi desligado.')

    def acelerar(self, velocidade=10):
        if self._is_ligado:
            self.__velocidade += velocidade
        else:
            print('O veículo precisa estar ligado para ser acelerado.')