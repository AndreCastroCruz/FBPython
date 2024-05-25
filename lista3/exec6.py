'''
Faça um programa que pegue um número do teclado e calcule a soma de todos os números  de 1 até ele. Ex.: o usuário entra 7, o programa vai mostrar 28, pois  1+2+3+4+5+6+7=28.
'''

import os
os.system("cls")

numero = int(input("Digite um número: "))

soma = 0
contador = 1

while contador <= numero:
    soma += contador
    contador += 1

print("A soma de todos os números de 1 até", numero, "é:", soma)
