import os
os.system("cls")

lista = []

produto = {
    "Descrição":"TV SMARTE",
    "Valor": 3000.50,
    "Estoque": 10
}


produto["Valor"]=2000.75
# print(produto)
lista.append(produto)
# print(lista)

produto = {
    "Descrição":"GELADEIRA",
    "Valor": 5000.50,
    "Estoque": 10
}

lista.append(produto)
print(lista)

lista[1]["Valor"]=4000.50
print("ajuste o valor")
print(lista)
