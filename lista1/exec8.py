custo_fabrica = float(input("Informe custo fabrica carro: R$ "))
percentagem_distribuidor = custo_fabrica * 0.28
impostos = custo_fabrica * 0.45
custo_consumidor = custo_fabrica+percentagem_distribuidor+impostos

print(f"Percentagem do distribuidor: R$ {percentagem_distribuidor:.2f}")
print(f"Impostos: R$ {impostos:.2f}")
print(f"Custo ao consumidor: R$ {custo_consumidor:.2f}")