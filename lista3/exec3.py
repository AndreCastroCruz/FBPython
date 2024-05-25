'''
Elaborar um programa que efetue a leitura sucessiva de valores numéricos e apresente no final o total do somatório, a média e o total de valores lidos. O programa deve fazer as leituras dos valores enquanto o usuário estiver fornecendo valores positivos. Ou seja, o programa deve parar quando o usuário fornecer um valor negativo.

'''


soma = 0
quantidade = 0

while True:
    valor = float(input("Digite um valor positivo (ou um valor negativo para parar): "))
    
    if valor < 0:
        break  
    
    soma += valor
    quantidade += 1

if quantidade == 0:
    print("Nenhum valor positivo foi fornecido.")
else:
    media = soma / quantidade
    print("Total do somatório:", soma)
    print("Média dos valores:", media)
    print("Total de valores lidos:", quantidade)