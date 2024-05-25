from Conta import Conta

class Especial(Conta):
    def __init__(self, numero, cpf, limite=1000, saldo=0.0, ativo=True):
        super().__init__(numero, cpf, saldo, ativo)
        self.limite = limite


    def usar_limite(self, valor):
        if self.limite >= valor:
            self.credito(valor)
            self.limite -= valor
        else:
            print("Limite insuficiente.")


    def debito(self, valor):
        if valor < 0:
            print("Não é possível debitar um valor negativo.")
        if self._saldo >= valor:
            self._debito(valor)
        elif self._saldo + self.limite >= valor:
            self.usar_limite(valor - self._saldo)
            self._debito(valor)
        else:
           print("Saldo e limite insuficientes.")


    def extrato(self):
        print("Extrato Especial:")
        print(f"Saldo: R${self.get_saldo():.2f}")
        print(f"Limite disponível: R${self.limite:.2f}")