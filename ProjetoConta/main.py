from Conta import Conta
from poupanca import Poupanca
from corrente import Corrente
from especial import Especial
from empresa import Empresa
from estudantil import Estudantil




def main():
    while True:
        exibir_menu()
        opcao = input("Digite o código da opção desejada: ")
        if opcao == "6":
            print("Você saiu do banco!")
            break
        tipo_conta = int(opcao)
        conta = criar_conta(tipo_conta)
        if conta:
            while True:
                print("Saldo atual: R$", conta.get_saldo())
                realizar_movimento(conta)
                conta.extrato()


                if tipo_conta == 1:
                    data_atual = int(input("Digite o dia de hoje: "))
                    conta.correcao(data_atual)
                elif tipo_conta == 2:
                    if conta.contador_talao < 3:
                        solicitar_talao = input("Deseja solicitar um talão de cheques (S/N)? ").upper()
                        if solicitar_talao == "S":
                            conta.pedir_talao()
                elif tipo_conta == 3:
                    if conta.get_saldo() < 0:
                        usar_limite = input("Deseja usar o limite especial (S/N)? ").upper()
                        if usar_limite == "S":
                            valor_limite = float(input("Quanto do limite deseja utilizar? R$ "))
                            conta.usar_limite(valor_limite)
                elif tipo_conta == 4:
                    solicitar_emprestimo = input("Deseja solicitar um empréstimo (S/N)? ").upper()
                    if solicitar_emprestimo == "S":
                            valor_emprestimo = float(input("Valor do empréstimo: R$ "))
                            conta.pedir_emprestimo(valor_emprestimo)
                elif tipo_conta == 5:
                    solicitar_limite_estudantil = input("Deseja utilizar o limite estudantil (S/N)? ").upper()
                    if solicitar_limite_estudantil == "S":
                        valor_limite_estudantil = float(input("Valor a usar do limite estudantil: R$ "))
                        conta.usar_estudantil(valor_limite_estudantil)


                continuar = input("Continuar S/N: ").upper()
                if continuar != "S":
                    break
        else:
            print("Opção inválida.")


def exibir_menu():
    print("-" * 50)
    print("[CASTRO'S BANK]")
    print("[Onde sua segurança financeira é prioridade]")
    print("-" * 50)
    print("1 - Conta Poupança")
    print("2 - Conta Corrente")
    print("3 - Conta Especial")
    print("4 - Conta Empresa")
    print("5 - Conta Estudantil")
    print("6 - Sair")
    print("-" * 50)




def criar_conta(tipo_conta):
    numero = input("Digite o número da conta: ")
    cpf = input("Digite o CPF do titular (apenas numeros): ")
    if tipo_conta == 1:
        return Poupanca(numero, cpf)
    elif tipo_conta == 2:
        return Corrente(numero, cpf)
    elif tipo_conta == 3:
        return Especial(numero, cpf)
    elif tipo_conta == 4:
        return Empresa(numero, cpf)
    elif tipo_conta == 5:
        return Estudantil(numero, cpf)
    else:
        return None




def realizar_movimento(conta):
    tipo_movimento = input("MOVIMENTO - D-débito ou C-Crédito: ").upper()
    valor_movimento = float(input("Valor movimento: R$ "))
    try:
        if tipo_movimento == "D":
            conta.debito(valor_movimento)
        elif tipo_movimento == "C":
            conta.credito(valor_movimento)
        else:
            print("Opção inválida.")
    except:
        print("Erro:")



    
main()