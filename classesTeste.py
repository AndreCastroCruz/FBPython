class Produto:
    def __init__(self,codigo,nome,valor,id=0,estoque=0):
        self.id = id
        self.codigo = codigo
        self.nome = nome
        self.valor = valor
        self.estoque = estoque
        
    def incluir(self,valor):
        self.estoque = self.estoque + valor

    def retirar(self,valor):
        if valor <= 0:
            print("impossivel realizar")
        elif valor > self.estoque:
            print("Sem estoque disponivel")
        else:
            self.estoque = self.estoque - valor

    
    def __str__(self):
        return f"Id : {self.id} - cod : {self.codigo} nome : {self.nome} - valor R$: {self.valor} - estoque: {self.estoque}"
