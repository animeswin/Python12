class Veiculo:
    def movimentar(self):
        print("Veículo está em movimento.")

class Carro(Veiculo):
    def movimentar(self):
        print("Carro está dirigindo.")

class Moto(Veiculo):
    def movimentar(self):
        print("Moto está acelerando.")

veiculo = Veiculo()
carro = Carro()
moto = Moto()

veiculo.movimentar()
carro.movimentar()
moto.movimentar()