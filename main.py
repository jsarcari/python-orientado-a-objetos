import carro, moto, veiculo

uno_vermelho = moto.Moto('vermelho', 'Flex', 1.0, 4)
print(uno_vermelho.cor)
uno_vermelho.abastecer(60)
uno_vermelho.ligar()
uno_vermelho.acelerar()
print(f'Combustível: {uno_vermelho.qtd_combustivel}L')
print(f'Velocidade: {uno_vermelho.velocidade}km/h')
uno_vermelho.desligar()
uno_vermelho.abastecer(50)
uno_vermelho.ligar()
uno_vermelho.acelerar(40)
print(f'Combustível: {uno_vermelho.qtd_combustivel}L')
print(f'Velocidade: {uno_vermelho.velocidade}km/h')
uno_vermelho.pintar('azul')

moto_verde = moto.Moto('verde','Gasolina',1.0,2)

#Duck-typing:
if isinstance(moto_verde, veiculo.Veiculo):
    print('A classe é um veículo')
else:
    print('A classe não é um veículo')