from Conta import Conta

class Estudantil(Conta):
    def __init__(self, numero, cpf, limite_estudantil=5000, saldo=0.0, ativo=True):
        super().__init__(numero, cpf, saldo, ativo)
        self.limite_estudantil = limite_estudantil


    def usar_estudantil(self, valor):
        if self.limite_estudantil >= valor:
            self.credito(valor)
            self.limite_estudantil -= valor
        else:
            print("Limite estudantil insuficiente.")


    def debito(self, valor):
        if valor < 0:
            print("Não é possível debitar um valor negativo.")
        if self._saldo >= valor:
            self._debito(valor)
        elif self._saldo + self.limite_estudantil >= valor:
            self.usar_estudantil(valor - self._saldo)
            self._debito(valor)
        else:
            print("Saldo e limite estudantil insuficientes.")


    def extrato(self):
        print("Extrato Estudantil:")
        print(f"Saldo: R${self.get_saldo():.2f}")
        print(f"Limite estudantil disponível: R${self.limite_estudantil:.2f}")
