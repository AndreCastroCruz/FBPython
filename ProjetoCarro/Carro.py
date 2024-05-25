class CarroPequeno:

    def __init__(self,  marca, cor, motor, velocidade=0, ligado=False):
        self.marca = marca
        self.cor = cor
        self.motor = motor
        self.velocidade = velocidade
        self.ligado = ligado

    def ligar(self):
        self.ligado = True
        print("Carro ligado")

    def acelerar(self):
        if self.ligado:
            if self.velocidade < 190:
                print("Velocidade atual: ", self.velocidade)
                print("Acelerando...")
                self.velocidade = self.velocidade + 10
                print("Velocidade atual: ", self.velocidade)
        else:
            print("Primeiro ligue o carro")

    def frear(self):
        if self.ligado:
            if self.velocidade >= 10:
                print("Velocidade atual: ", self.velocidade)
                print("Freiando...")
                self.velocidade = self.velocidade - 10
                print("Velocidade atual: ", self.velocidade)
            else:
                print("Carro Parado")
        else:
            print("Carro Desligado")



class Moto:
    def __init__(self, marca, cilindrada, velocidade=0, ligado=False) -> None:
        self.__marca = marca
        self.__cilindrada = cilindrada
        self.__velocidade = velocidade
        self.__ligado = ligado

class CarroGrande:
    def __init__(self,  marca, cor, motor, eixos, velocidade=0, ligado=False):
        self.marca = marca
        self.cor = cor
        self.motor = motor
        self.eixos = eixos
        self.velocidade = velocidade
        self.ligado = ligado


