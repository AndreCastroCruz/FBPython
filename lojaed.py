import os
os.system("cls")
import time

def limpatela():
    os.system("cls")


def linha(tamanho):
    print("-"*tamanho) 

lista = []



while True:
    limpatela()
    linha(60)
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Alterar")
    print("4 - Apagar")
    print("5 - Comprar")
    print("6 - Sair")

    op = input("Digite o numero da opção: ")
    linha(60)

    if op == "1":
        while True:
            limpatela()
            linha(60)
            nome = input("Nome do Produto: ").upper()
            valor = float(input("Valor do Produto: R$ "))
            lista.append({
                "DESCRIÇÃO":nome,
                "VALOR":valor,
                "ESTOQUE":10
            })
            saida = input("Continua S/N: ").upper()
            if saida == "N":
                break
    
    elif op == "2":
        while True:
            if not lista:
                print("Lista vazia, cadastre os produtos") 
            else:
                while True:
                    for produto in lista:
                        print(produto)
                    saida = input("Continua S/N: ").upper()
                    if saida == "N":
                        break
            time.sleep(2)
            
    elif op == "3":
        ...
    elif op == "4":
        ...
    elif op == "5":
        ...
    elif op == "6":
        ...
        
    