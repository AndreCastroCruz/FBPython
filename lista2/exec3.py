'''
Desenvolva um programa em que:
Leia 4 (quatro) números;
Calcule o quadrado de cada um;
Se o valor resultante do quadrado do terceiro for >= 1000, imprima-o e finalize;
Caso contrário, imprima os valores lidos e seus respectivos quadrados.

'''

import os
os.system('cls')
import math

num1 = int(input("Digite o 1º número: "))
quad1 = math.pow(num1, 2)

num2 = int(input("Digite o 2º número: "))
quad2 = math.pow(num2, 2)

num3 = int(input("Digite o 3º número: "))
quad3 = math.pow(num3, 2)

if quad3 >= 1000:
    print(f"O quadrado do terceiro número é {quad3}")
else:
    num4 = int(input("Digite o 4º número: "))
    quad4 = math.pow(num4, 2)
    print("Os números e seus respectivos quadrados são:")
    print(f"Número {num1} - Quadrado: {quad1}")
    print(f"Número {num2} - Quadrado: {quad2}")
    print(f"Número {num3} - Quadrado: {quad3}")
    print(f"Número {num4} - Quadrado: {quad4}")

print("Fim de programa")