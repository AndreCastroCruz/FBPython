import os
os.system("cls")

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))
d = int(input("Informe o valor de D: "))
e = int(input("Informe o valor de E: "))
f = int(input("Informe o valor de f: "))

x = (c*e)-(b*f)/(a*e)-(b*d)
y = (a*f)-(c*d)/(a*e)-(b*d)

print(f"O valor de X é: {x}")
print(f"O valor de Y é: {y}")


