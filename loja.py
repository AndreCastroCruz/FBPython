import os
os.system("cls")

import time

#Montagem da Lista
lista = []

aluno = {
    'matricula':1,
    'nome':'Epaminondas',
    'nascimento': 2000,
    'turma':'tecnico'
}

aluno2 = {
    'matricula':2,
    'nome':'Marias',
    'nascimento': 2001,
    'turma':'tecnico'
}

lista.append(aluno)
lista.append(aluno2)

# print(lista)

for nomes in lista:
    for chave in nomes:
        print(f"{chave} : {nomes[chave]}")