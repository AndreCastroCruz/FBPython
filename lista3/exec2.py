'''
Desenvolver um programa que efetue a soma de todos os números ímpares que são  múltiplos de três e que se encontram no conjunto dos números de 1 até 500.
'''

soma = 0

for num in range(1, 501): 
    if num % 2 != 0 and num % 3 == 0:
        soma += num 

print("A soma dos números ímpares múltiplos de três de 1 até 500 é:", soma)