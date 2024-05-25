from Conta import Conta

class Empresa(Conta):
    def __init__(self, numero, cpf, emprestimo_empresa=10000, saldo=0.0, ativo=True):
        super().__init__(numero, cpf, saldo, ativo)
        self.emprestimo_empresa = emprestimo_empresa


    def pedir_emprestimo(self, valor):
        if self.emprestimo_empresa >= valor:
            self.credito(valor)
            self.emprestimo_empresa -= valor
        else:
            print("Empréstimo indisponível do valor solicitado.")


    def debito(self, valor):
        self._debito(valor)


    def extrato(self):
        print("Extrato Empresa:")
        print(f"Saldo: R${self.get_saldo():.2f}")
        print(f"Empréstimo disponível: R${self.emprestimo_empresa:.2f}")