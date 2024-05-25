import pymysql


conexao = pymysql.connect(
    host="localhost",
    user="root",
    password="fbradesco",
    database="castrosbank"
)

cursor = conexao.cursor()

