from Conta import Conta

class Corrente(Conta):
    def __init__(self, numero, cpf, contador_talao=0, saldo=0.0, ativo=True):
        super().__init__(numero, cpf, saldo, ativo)
        self.contador_talao = contador_talao


    def pedir_talao(self):
        if self.contador_talao < 3:
            self.debito(30)
            self.contador_talao += 1
        else:
            print("Limite de talões atingido.")


    def debito(self, valor):
        self._debito(valor)


    def extrato(self):
        print("Extrato Corrente:")
        print(f"Saldo: R${self.get_saldo():.2f}")
        print(f"Talões disponíveis: {3 - self.contador_talao}")
