import os
os.system("cls")

produtos = []

def cadastrar_produto():
    descricao = input("Digite a descrição do produto: ")
    valor = float(input("Digite o valor do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))
    produto = {"descricao": descricao, "valor": valor, "estoque": estoque}
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for i, produto in enumerate(produtos, 1):
            print(f"\n{i}. Descrição: {produto['descricao']}, Valor: R${produto['valor']:.2f}, Estoque: {produto['estoque']}")

def apagar_produto():
    if not produtos:
        print("\nNenhum produto cadastrado.")
    else:
        listar_produtos()
        indice = int(input("Digite o número do produto que deseja apagar: "))
        if 1 <= indice <= len(produtos):
            del produtos[indice - 1]
            print("Produto apagado com sucesso!")
        else:
            print("Índice inválido.")

while True:
    print("\n==== Menu ====")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Apagar produto")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()    
    elif opcao == "3":
        apagar_produto()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")