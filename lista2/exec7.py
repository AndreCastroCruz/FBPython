'''
 Receber valores de base e altura de um triângulo e verificar se são valores válidos (positivos maiores que zero). Em caso afirmativo, calcular a área do triângulo.

'''

import os
os.system("cls")


base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

if base < 0:
    print("O valor da base é negativo.")
elif base == 0:
    print("O valor da base é igual a zero.")
elif altura < 0:
    print("O valor da altura é negativo.")
elif altura == 0:
    print("O valor da altura é igual a 0.")
else:
    area = (base*altura)/2
    print(f"A area do triangulo é {area}")

print("Fim de programa")