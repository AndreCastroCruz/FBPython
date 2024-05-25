'''
Obtenha um número digitado pelo usuário e repita a operação de multiplicar ele por três  (imprimindo o novo valor) até que ele seja maior do que 100. Ex.: se o usuário digita 5,  deveremos observar na tela a seguinte sequência: 5 15 45 135.

'''


import os
os.system("cls")

numero = int(input("Digite um número: "))

while numero <= 100:
    print(numero, end=" ")
    numero *= 3

print(numero) 
