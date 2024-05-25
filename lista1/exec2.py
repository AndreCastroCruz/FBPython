dias = int(input("Digite sua idade em dias: "))

idade_anos = dias//365
idade_meses = (dias%365)//30
idade_dias = (dias%365)%30

print(f"Sua idade em anos é: {idade_anos}")
print(f"Sua idade em meses é: {idade_meses}")
print(f"Sua idade em dias é: {idade_dias}")