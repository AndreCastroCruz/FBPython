numero = int(input("Digite um numero positivo: "))

if numero < 0:
    print("Vc digitou um numero negativo")
elif numero ==0:
    print("Vc digitou zero, zero é neutro")
elif (numero % 2 == 0):
    print("O numero é par")
else:
    print("O numero é impar")


