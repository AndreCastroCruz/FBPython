import pandas as pd
import os

#pd.set_option("display.max_columns",None)#mostra todas as colunas

fem_df = pd.read_csv("Feminicidio.csv")

# print(fem_df)


#quantidade anual
anual = fem_df[['ANO_ESTATISTICA','VITIMAS']].groupby('ANO_ESTATISTICA').sum()
print(anual)

pele = fem_df[['COR_PELE','VITIMAS']].groupby('COR_PELE').sum()
print(pele)

profissao = fem_df[['PROFISSAO','VITIMAS']].groupby('PROFISSAO').sum()
print(profissao)

sexo = fem_df[['SEXO_PESSOA','VITIMAS']].groupby('SEXO_PESSOA').sum()
print(sexo)

idade = fem_df[['IDADE_PESSOA','VITIMAS']].groupby('IDADE_PESSOA').sum()
print(idade)


