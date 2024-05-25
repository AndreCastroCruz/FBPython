# Elabore um programa que leia as variáveis C e N, respectivamente código e número de horas trabalhadas de um operário. E calcule o salário sabendo-se que ele ganha R$ 10,00 por hora. Quando o número de horas exceder a 50 calcule o excesso de pagamento armazenando-o na variável E, caso contrário zerar tal variável. A hora excedente de trabalho vale R$ 20,00. No final do processamento imprimir o salário total e o salário excedente.

import os
os.system("cls")


C = ""
N = 0
E = 0
salario = 0.00
VALOR_HORA = 10.00
HORA_EXCEDENTE = 20.00
LIMITE_HORAS = 50
salario_total = 0.00
salario_excedente = 0.00

C = input("Digite o código: ")
N = int(input("Numero de horas: "))

if N <= LIMITE_HORAS:
    salario = N * VALOR_HORA
else:
    E = N - LIMITE_HORAS
    salario_excedente = E * HORA_EXCEDENTE
    salario_total = (LIMITE_HORAS * VALOR_HORA)+salario_excedente

print(f"Horas excedentes {E}")
print(f"Salario excedente: {salario_excedente}")
print(f"Salario total {salario_total}")