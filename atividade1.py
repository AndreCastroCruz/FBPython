import os
os.system("cls")

op = ""
lista = []
def linha(tamanho):
    print("-"*tamanho)



while op != "4":
    print("Selecione uma opção(Apenas Números): ")  
    print("1 - Inserir \n2 - Listar \n3 - Apagar \n4 - Sair")
    op = input("Escolha uma opção: ")

    if op == "1":
        numero = int(input("Digite o número: "))
        lista.append(numero)
    elif op == "2":
        if len(lista) == 0:
            print("Lista sem itens")
            linha(60)
        else:
            linha(60)
    
        
    


