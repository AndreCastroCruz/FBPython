import os
os.system("cls")

segundos_totais = int(input("Duração do evento em segundos: "))

horas = segundos_totais//3600
minutos = (segundos_totais%3600)//60
segundos = (segundos_totais%3600)%60

print(f"Horas: {horas}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundos}")



