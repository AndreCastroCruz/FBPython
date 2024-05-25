import pymysql
import os
from classesTeste import Produto
import time

def limpaTela():
    os.system("cls")


limpaTela()
#criar banco de dados
con = pymysql.connect(
    host='localhost',
    user='root',
    password='fbradesco',
    database='castroloja'
   )

with con:
    with con.cursor() as cursor:
        TABLE_NAME = "produto"
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}("
                       "ID INT AUTO_INCREMENT PRIMARY KEY ,"
                       "CODIGO VARCHAR(10) NOT NULL ,"
                       "NOME VARCHAR(50) NOT NULL ,"
                       "VALOR DOUBLE(10,2) ,"
                       "ESTOQUE INT NOT NULL"
        ")")
        con.commit()
        with con.cursor() as cursor:
            while True:
                limpaTela()
                print("1 - Cadastro")
                print("2 - Alterar")
                print("3 - Listar")
                print("4 - Excluir")
                print("5 - Movimentar")
                print("6 - Sair")
                op = input("Escolha o numero da sua opção: ")
                if op=='6':
                    time.sleep(2)
                    print("Até breve...")
                    break
                elif op == '1':
                    print("-"*20)
                    print("CADASTRAMENTO")
                    codigo = input("Digite o código: ")
                    nome = input("Digite o Nome produto:")
                    valor = float(input("Digite o valor do produto: R$ "))
                    item = Produto(codigo,nome,valor)
                    cursor.execute(f"INSERT INTO PRODUTO (CODIGO,NOME,VALOR,ESTOQUE) "\
                    "VALUES (%s,%s,%s,%s)",(item.codigo,item.nome,item.valor,item.estoque))
                    con.commit()
                    print("PRODUTO CADASTRADO")
                    time.sleep(2)

                elif op =='2':
                    print("-"*20)
                    print("ALTERAÇÃO")
                    codigo = input("Digite o código do produto a ser alterado: ")
                    nome = input("Informe o novo nome do produto: ")
                    valor = float(input("Digite o novo valor do produto: "))
                    item = Produto(codigo,nome,valor)
                    cursor.execute(f"UPDATE PRODUTO SET NOME=%s, VALOR=%s WHERE CODIGO=%s",(item.nome,item.valor,item.codigo))
                    con.commit()
                    time.sleep(1)

                elif op=='3':
                    print("-"*20)
                    print("LISTAGEM")
                    cursor.execute(f"SELECT * FROM PRODUTO")
                    resposta = cursor.fetchall()
                    for linha in resposta:
                        print(linha)
                    time.sleep(3)
                
                elif op=='4':
                    print("-"*20)
                    print("EXCLUINDO...")
                    codigo = input("Digite o codigo do produto a ser excluido: ")
                    cursor.execute(f"DELETE FROM PRODUTO WHERE CODIGO=%s",(codigo))
                    con.commit()
                    print("Produto deletado...")
                    time.sleep(1)
                    
                elif op=='5':
                    print("-"*20)
                    print("MOVIMENTAÇÃO")
                    codigo = input("Digite o codigo do produto a ser movimentado: ")
                    cursor.execute(f"SELECT * FROM PRODUTO WHERE CODIGO=%s",(codigo))
                    item = cursor.fetchone()
                    produto_item = Produto(*item)
                    print(produto_item)
                    time.sleep(5)

                    