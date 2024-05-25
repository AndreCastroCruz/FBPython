#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de tomate maior que o estabelecido pelo regulamento do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável P (peso de tomates) e verifique se há excesso. Se houver, gravar na variável E (Excesso) e na variável M o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.
import os
os.system("cls")

M = 0
E = 0
P = float(input("Quantos quilos de tomate: "))

if P > 50.0:
   E = P-50.0
   M = 4.0*E
   print("Peso maior que 50.")
   print(f"Excesso de: {E}")
   print(f"Multa de: {M}")
elif P == 0:
   print("Peso igual a zero.")
elif P < 0:
   print("Peso negativo.")
else:
   print("Peso dentro do limite.")
   print(f"Excesso de: {E}")
   print(f"Multa de: {M}")
   


