'''
A Secretaria de Meio Ambiente que controla o índice de poluição mantém 3 grupos de indústrias que são altamente poluentes do meio ambiente. O índice de poluição aceitável varia de 0,05 até 0,25. Se o índice sobe para 0,3 as indústrias do 1º grupo são intimadas a suspenderem suas atividades, se o índice crescer para 0,4 as indústrias do 1º e 2º grupo são intimadas a suspenderem suas atividades, se o índice atingir 0,5 todos os grupos devem ser notificados a paralisarem suas atividades. Faça um programa que leia o índice de poluição medido e emita a notificação adequada aos diferentes grupos de empresas.

'''

import os
os.system("cls")

indice_pol = float(input("Digite o índice de poluição medido: "))

if indice_pol >= 0.5:
    print("Todos os grupos devem paralisar suas atividades.")
elif indice_pol >= 0.4:
    print("Os grupos 1 e 2 devem paralisar suas atividades.")
elif indice_pol >= 0.3:
    print("O grupo 1 deve paralisar suas atividades.")
elif indice_pol >= 0.25:
    print("Índice dentro do aceitável. Nenhuma ação necessária.")
elif indice_pol >= 0.05:
    print("Índice de poluição baixo.")
else:
    print("Índice de poluição fora do intervalo aceitável.")
