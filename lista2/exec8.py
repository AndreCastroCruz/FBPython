'''
Construa um programa para ler uma variável numérica N e imprimi-la somente se a mesma for maior que 100, caso contrário imprimi-la com o valor zero.
'''


import os
os.system("cls")

N = int(input("Digite um número: "))

if N > 100:
    print("O número é maior que 100:", N)
else:
    N = 0
    print("O número é menor ou igual a 100: ", N)
