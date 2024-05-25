'''
Faça um programa que mostre uma contagem na tela de 233 a 456, só que contando de 3 em 3 quando estiver entre 300 e 400 e de 5 em 5 quando não estiver.
'''

import os
os.system("cls")

numero = 233

while numero <= 456:
    print(numero, end="\n")
    
    if 300 <= numero <= 400:  
        numero += 3
    else:  
        numero += 5
print("Fim de programa!!!!!")