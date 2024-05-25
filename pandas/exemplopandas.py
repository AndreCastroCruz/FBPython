import pandas as pd
import os

def cabeca():
    os.system("cls")
    print("-"*20,end='')
    print("Arquivo Vendas",end='')
    print("-"*20)


vendas_df = pd.read_excel("Vendas.xlsx")
pd.set_option('display.max_columns',None) #mostra todas as colunas

#Faturamento por loja
cabeca()
print(vendas_df)
print(vendas_df['ID Loja'])

