from Conta import Conta

class Poupanca(Conta):
    def __init__(self, numero, cpf, dia_aniversario=9, saldo=0.0, ativo=True):
        super().__init__(numero, cpf, saldo, ativo)
        self.dia_aniversario = dia_aniversario


    def correcao(self, data_atual):
        if data_atual == self.dia_aniversario:
            self.credito(self.get_saldo() * 0.05)


    def debito(self, valor):
        self._debito(valor)


    def extrato(self):
        print("Extrato Poupança:")
        print(f"Saldo: R${self.get_saldo():.2f}")