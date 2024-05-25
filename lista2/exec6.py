'''
6) Elabore um programa que dada a idade de um nadador classifique-o em uma das seguintes categorias:
Infantil A = 5 a 7 anos
Infantil B = 8 a 11 anos
Juvenil A = 12 a 13 anos
Juvenil B = 14 a 17 anos
Adultos = Maiores de 18 anos

'''

import os
os.system("cls")

while True:
    try:
        idade = int(input("Digite a idade: "))
        if idade < 5:
            print("Não atendemos nesta faixa etaria!!!")
        elif idade < 8:
            print("Infantil A")
        elif idade < 12:
            print("Infantil B")
        elif idade < 14:
            print("Juvenil A")
        elif idade < 18:
            print("Juvenil B")
        else:
            print("Adulto")
    except:
        print("Você não digitou uma idade valida!")
        
    op = input("Continu S/N: ").upper()
    if op == 'N':
        break

print("Fim do programa")

