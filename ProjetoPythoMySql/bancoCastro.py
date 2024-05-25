# fase 1 - conexão
import pymysql
import os
import time

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='fbradesco',
    database='castrosbank'
   )

os.system("cls")

with conexao:
    with conexao.cursor() as cursor:
        TABLE_NAME = 'Poupanca'
        #criação de uma tabela
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT AUTO_INCREMENT PRIMARY KEY , '
            'numero INT NOT NULL,'
            'cpf VARCHAR(20) NOT NULL, '
            'saldo DOUBLE(10,2) NOT NULL,'
            'ativo bool ,'
            'diaAniversarioPoupanca INT NOT NULL'
            ')'
        )
    conexao.commit()
    with conexao.cursor() as cursor:
        TABLE_NAME = 'Corrente'
        #criação de uma tabela
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT AUTO_INCREMENT PRIMARY KEY , '
            'numero INT NOT NULL,'
            'cpf VARCHAR(11) NOT NULL, '
            'saldo DOUBLE(10,2) NOT NULL,'
            'ativo bool ,'
            'contadorTalao INT NOT NULL'
            ')'
        )
    conexao.commit()
    with conexao.cursor() as cursor:
        TABLE_NAME = 'Especial'
        #criação de uma tabela
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT AUTO_INCREMENT PRIMARY KEY , '
            'numero INT NOT NULL,'
            'cpf VARCHAR(11) NOT NULL, '
            'saldo DOUBLE(10,2) NOT NULL,'
            'ativo bool ,'
            'limite double(10,2) NOT NULL'
            ')'
        )
    conexao.commit()
    with conexao.cursor() as cursor:
        TABLE_NAME = 'Empresa'
        #criação de uma tabela
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT AUTO_INCREMENT PRIMARY KEY , '
            'numero INT NOT NULL,'
            'cpf VARCHAR(11) NOT NULL, '
            'saldo DOUBLE(10,2) NOT NULL,'
            'ativo bool ,'
            'emprestimo double(10,2) NOT NULL'
            ')'
        )
    conexao.commit() 
    with conexao.cursor() as cursor:
        TABLE_NAME = 'Estudantil'
        #criação de uma tabela
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT AUTO_INCREMENT PRIMARY KEY , '
            'numero INT NOT NULL,'
            'cpf VARCHAR(11) NOT NULL, '
            'saldo DOUBLE(10,2) NOT NULL,'
            'ativo bool ,'
            'limite_estudantil double(10,2) NOT NULL'
            ')'
        )
    conexao.commit()     

    #MONTAGEM DO MENU DE ACESSO
    while True:
        os.system("cls")
        print('-'*80)
        print("Castro's Bank")
        print('-'*80)
        print("1 - Poupança")
        print("2 - Corrente")
        print("3 - Especial")
        print("4 - Empresa")
        print("5 - Estudantil")
        print("6 - Sair")
        opcao_menu_principal=input("Digite sua opção :")
        if opcao_menu_principal=='6':
            break
        elif opcao_menu_principal=='1':
            while True:
                os.system("cls")
                print('-'*80)
                print("Castro's Bank - Conta Poupanca")
                print('-'*80)
                print("1 - Cadastrar")
                print("2 - Alterar")
                print("3 - Apagar")
                print("4 - Movimentar")
                print("5 - Sair")
                sub_opcao_menu=input("Digite sua opção :")
                if sub_opcao_menu == '5':
                    break
                if sub_opcao_menu =='1':
                    with conexao.cursor() as cursor:
                        TABLE_NAME = "poupanca"
                        
                        #inserindo dados em produto
                        numero = int(input("Digite o numero da conta : "))
                        cpf = input("Digita o cpf do cliente da conta :")
                        diaAniversarioPoupanca = int(input("Digite o dia de aniversario da conta : "))
                        dados = (numero, cpf, 0.00, 1, diaAniversarioPoupanca)
                        sql = f'INSERT INTO {TABLE_NAME} (numero, cpf, saldo, ativo, diaAniversarioPoupanca) VALUES (%s,%s,%s,%s,%s)'
                        cursor.execute(sql,dados)
                        conexao.commit()

                        sql =f'SELECT * FROM {TABLE_NAME}'
                        cursor.execute(sql)
                        resposta = cursor.fetchall()
                        print("Dados cadastrados")                    
                        for linha in resposta:
                            print(linha)
                    conexao.commit()
                    time.sleep(3)


                    #DUVIDA
                elif sub_opcao_menu == '2':
                    # Lógica para alterar dados
                    with conexao.cursor() as cursor:
                        numero_conta = int(input("Digite o número da conta que deseja alterar: "))
                        novo_cpf = input("Digite o novo CPF: ")
                        novo_numero = int(input("Digite o novo número da conta: "))
                        novo_dia_aniversario = int(input("Digite o novo dia de aniversário da conta: "))
                        sql = f'UPDATE Poupanca SET cpf=%s, numero=%s, diaAniversarioPoupanca=%s WHERE numero=%s'
                        cursor.execute(sql, (novo_cpf, novo_numero, novo_dia_aniversario, numero_conta))
                        conexao.commit()
                        print("Dados atualizados com sucesso!")
                        time.sleep(3)
                elif sub_opcao_menu == '3':
                    # Lógica para apagar dados
                    with conexao.cursor() as cursor:
                        numero_conta = int(input("Digite o número da conta que deseja apagar: "))
                        sql = f'DELETE FROM Poupanca WHERE numero=%s'
                        cursor.execute(sql, (numero_conta,))
                        conexao.commit()
                        print("Dados apagados com sucesso!")
                        time.sleep(3)
                        #DAQUI PRA CIMA DUVIDA


        elif opcao_menu_principal=='2':
            while True:
                os.system("cls")
                print('-'*80)
                print("Castro's Bank - Conta Corrente")
                print('-'*80)
                print("1 - Cadastrar")
                print("2 - Alterar")
                print("3 - Apagar")
                print("4 - Movimentar")
                print("5 - Sair")
                sub_opcao_menu=input("Digite sua opção :")
                if sub_opcao_menu == '5':
                    break
            
                if sub_opcao_menu =='1':
                    with conexao.cursor() as cursor:
                        TABLE_NAME = "corrente"
                        
                        #inserindo dados em produto
                        numero = int(input("Digite o numero da conta : "))
                        cpf = input("Digita o cpf do cliente da conta :")
                        dados = (numero, cpf, 0.00, 1, 0)
                        sql = f'INSERT INTO {TABLE_NAME} (numero, cpf, saldo, ativa, contadorTalao) VALUES (%s,%s,%s,%s,%s)'
                        cursor.execute(sql,dados)
                        conexao.commit()

                        sql =f'SELECT * FROM {TABLE_NAME}'
                        cursor.execute(sql)
                        resposta = cursor.fetchall()
                        print("Dados cadastrados")                    
                        for linha in resposta:
                            print(linha)
                    conexao.commit()
                    time.sleep(3)

                
                # elif sub_opcao_menu == '2':
                #     # Lógica para alterar dados
                #     with conexao.cursor() as cursor:
                #         numero_conta = int(input("Digite o número da conta que deseja alterar: "))
                #         novo_cpf = input("Digite o novo CPF: ")
                #         novo_numero = int(input("Digite o novo número da conta: "))
                #         if numero_conta == novo_numero:
                #             contador_talao = int(input("Digite o número de talões usados: "))
                #             contador_atualizado = 3 - contador_talao
                #             sql = f'UPDATE Corrente SET cpf=%s, numero=%s, contadorTalao=%s WHERE numero=%s'
                #             cursor.execute(sql, (novo_cpf, novo_numero, contador_atualizado, numero_conta))
                #             conexao.commit()
                #             print("Dados atualizados com sucesso!")
                #         else:
                #             print("Você não pode alterar o número da conta diretamente.")
                #             time.sleep(3)
                # elif sub_opcao_menu == '3':
                #     # Lógica para apagar dados
                #     with conexao.cursor() as cursor:
                #         numero_conta = int(input("Digite o número da conta que deseja apagar: "))
                #         sql = f'DELETE FROM Corrente WHERE numero=%s'
                #         cursor.execute(sql, (numero_conta,))
                #         conexao.commit()
                #         print("Dados apagados com sucesso!")
                #         time.sleep(3)

        elif opcao_menu_principal=='3':
            while True:
                os.system("cls")
                print('-'*80)
                print("Castro's Bank - Conta Especial")
                print('-'*80)
                print("1 - Cadastrar")
                print("2 - Alterar")
                print("3 - Apagar")
                print("4 - Movimentar")
                print("5 - Sair")
                sub_opcao_menu=input("Digite sua opção :")
                if sub_opcao_menu == '5':
                    break
            
                if sub_opcao_menu =='1':
                    with conexao.cursor() as cursor:
                        TABLE_NAME = "especial"
                        
                        #inserindo dados em produto
                        numero = int(input("Digite o numero da conta : "))
                        cpf = input("Digita o cpf do cliente da conta :")
                        dados = (numero, cpf, 0.00, 1, 1000)
                        sql = f'INSERT INTO {TABLE_NAME} (numero, cpf, saldo, ativa, limite) VALUES (%s,%s,%s,%s,%s)'
                        cursor.execute(sql,dados)
                        conexao.commit()

                        sql =f'SELECT * FROM {TABLE_NAME}'
                        cursor.execute(sql)
                        resposta = cursor.fetchall()
                        print("Dados cadastrados")                    
                        for linha in resposta:
                            print(linha)
                    conexao.commit()
                    time.sleep(3)

        elif opcao_menu_principal=='4':
            while True:
                os.system("cls")
                print('-'*80)
                print("Castro's Bank - Conta Empresa")
                print('-'*80)
                print("1 - Cadastrar")
                print("2 - Alterar")
                print("3 - Apagar")
                print("4 - Movimentar")
                print("5 - Sair")
                sub_opcao_menu=input("Digite sua opção :")
                if sub_opcao_menu == '5':
                    break
            
                if sub_opcao_menu =='1':
                    with conexao.cursor() as cursor:
                        TABLE_NAME = "empresa"
                        
                        #inserindo dados em produto
                        numero = int(input("Digite o numero da conta : "))
                        cpf = input("Digita o cpf do cliente da conta :")
                        dados = (numero, cpf, 0.00, 1, 10000)
                        sql = f'INSERT INTO {TABLE_NAME} (numero, cpf, saldo, ativo, emprestimo) VALUES (%s,%s,%s,%s,%s)'
                        cursor.execute(sql,dados)
                        conexao.commit()

                        sql =f'SELECT * FROM {TABLE_NAME}'
                        cursor.execute(sql)
                        resposta = cursor.fetchall()
                        print("Dados cadastrados")                    
                        for linha in resposta:
                            print(linha)
                    conexao.commit()
                    time.sleep(3)
        
        elif opcao_menu_principal=='5':
            while True:
                os.system("cls")
                print('-'*80)
                print("Castro's Bank - Conta Estudantil")
                print('-'*80)
                print("1 - Cadastrar")
                print("2 - Alterar")
                print("3 - Apagar")
                print("4 - Movimentar")
                print("5 - Sair")
                sub_opcao_menu=input("Digite sua opção :")
                if sub_opcao_menu == '5':
                    break
            
                if sub_opcao_menu =='1':
                    with conexao.cursor() as cursor:
                        TABLE_NAME = "estudantil"
                        
                        #inserindo dados em produto
                        numero = int(input("Digite o numero da conta : "))
                        cpf = input("Digita o cpf do cliente da conta :")
                        dados = (numero, cpf, 0.00, 1, 5000)
                        sql = f'INSERT INTO {TABLE_NAME} (numero, cpf, saldo, ativo, limite_estudantil) VALUES (%s,%s,%s,%s,%s)'
                        cursor.execute(sql,dados)
                        conexao.commit()

                        sql =f'SELECT * FROM {TABLE_NAME}'
                        cursor.execute(sql)
                        resposta = cursor.fetchall()
                        print("Dados cadastrados")                    
                        for linha in resposta:
                            print(linha)
                    conexao.commit()
                    time.sleep(3)
            

