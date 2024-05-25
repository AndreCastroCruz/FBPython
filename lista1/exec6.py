import os
os.system("cls")
import math

x1 = int(input("Digite o valor de x1: "))
y1 = int(input("Digite o valor de y1: "))
x2 = int(input("Digite o valor de x2: "))
y2 = int(input("Digite o valor de y2: "))

d1 =pow((x2-x1),2)+pow((y2-y1),2)

d = math.sqrt(d1)

print(f"A distância é: {d:.2f}")