import pandas as pd
import matplotlib.pyplot as plt
import os


# pd.set_option("display.max_columns", None)

#lendo a base de dados em um objeto
df = pd.read_csv("Feminicidio.csv")

#Montagem imagem de Osasco
# cidade_df = df[df['MUNICIPIO_CIRCUNSCRICAO']=='Osasco']
# raca_df = cidade_df.groupby('COR_PELE').size().reset_index(name="QTDE")
# raca_df = raca_df.sort_values(by='COR_PELE',ascending=True)


cidades = [
    'Santo André',
    'São Bernardo do Campo',
    'São Caetano do Sul',
    'Diadema',
    'Mauá',
    'Ribeirão Pires',
    'Rio Grande da Serra'
]
cidades_df = df[df['MUNICIPIO_CIRCUNSCRICAO'].isin(cidades)]

os.system("cls")
vitimas = cidades_df[['MUNICIPIO_CIRCUNSCRICAO','VITIMAS']].groupby('MUNICIPIO_CIRCUNSCRICAO').sum()\
    .sort_values(by="VITIMAS",ascending=False)


raca_df = cidades_df.groupby('COR_PELE').size().reset_index(name="QTDE")

print(vitimas)
print('-'*50)
print(raca_df)
print('-'*50)



# cidade_df = df[df['MUNICIPIO_CIRCUNSCRICAO']=='Osasco']


# print(raca_df)

# print(cidades_df)
