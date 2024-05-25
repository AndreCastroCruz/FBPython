class Conta:
    def __init__(self, numero, cpf, saldo=0.0, ativo=True):
        self.numero = numero
        self.cpf = cpf
        self._saldo = saldo
        self.ativo = ativo


    def get_saldo(self):
        return self._saldo


    def ativar(self):
        self.ativo = True


    def _debito(self, valor):
        if valor < 0:
            print("Não é possível debitar um valor negativo.")
        if valor > 0:
            if self._saldo >= valor:
                self._saldo -= valor
            else:
                print("Saldo insuficiente.")


    def credito(self, valor):
        if valor < 0:
            print("Não é possível creditar um valor negativo.")
        self._saldo += valor


    def debito(self, valor):
        self._debito(valor)


    def extrato(self):
        print("Extrato da Conta:")
        print(f"Saldo: R${self.get_saldo():.2f}")




