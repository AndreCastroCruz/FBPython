import os
os.system("cls")

lista=[]
op = ''
valor = 0
while True:
    op = input("[i]nserir\n[l]istar\n[a]pagar\n[s]air\nDigite a letra da sua opção: ").lower()
    if op=='s':
        break
    elif op == 'i':
        try:
            valor = int(input('Digite um numero inteiro positivo : '))
            if valor < 0:
                print("Valor negativo, impossivel realizar!!!")
            else:
                lista.append(valor)
        except:
            print("Digite um valor valido")
    elif op == 'l':
        for indice, numero in enumerate(lista):
            print(f"{indice} - {numero}")
    elif op == 'a':
        try:
            valor = int(input('Digite o indice do valor a ser excluido : '))
            if valor >= 0:
                del lista[valor]
            else:
                print("Valor de indice invalido")
        except:
            print("Valor informado de indice invalido!!!")
    else:
        print("Opção invalida!!!")


