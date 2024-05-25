import os
os.system("cls")

import math

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

R = (A+B)**2
S = math.pow((B+C), 2.0)
D = (R+S)/2

print(f"O valor de D = {D:.2f}")

