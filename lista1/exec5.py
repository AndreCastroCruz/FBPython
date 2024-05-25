import os
os.system("cls")

peso1 = 0.2
peso2 = 0.3
peso3 = 0.5

nota1 = int(input("Informe a nota 1: "))
nota2 = int(input("Informe a nota 2: "))
nota3 = int(input("Informe a nota 3: "))

media = (nota1*peso1+nota2*peso2+nota3*peso3)

print(f"Sua media é: {media}")