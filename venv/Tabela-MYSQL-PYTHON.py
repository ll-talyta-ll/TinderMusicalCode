#!/usr/bin/python3.9

import mysql.connector
try:
    #criando conexão ao banco de dados
    con = mysql.connector.connect(
    host='mysqlserver.ctxtwwh0ilx9.us-east-1.rds.amazonaws.com',
    user='admin',
    password='Brasilhexa2022',
    database='dbmysql',
    port='3306'
)
    #Declaração SQL a ser executada
    criar_tabela_SQL= """CREATE TABLE auth_user (
                            Name VARCHAR(70) NOT NULL,
                            User VARCHAR(70) NOT NULL,
                            Password VARCHAR(70) NOT NULL,
                            PasswordConf VARCHAR(70) NOT NULL,
                            Email VARCHAR(70) NOT NULL,
                            Age int(11) NOT NULL,
                            PRIMARY KEY (Name))"""
    #criar cursor e executar SQL no Banco de Dados
    cursor = con.cursor()
    cursor.execute(criar_tabela_SQL)
    print("Tabela de Usuário criada com sucesso!")
except mysql.connector.Error as erro:
    print("Falha ao criar a tabela no MySqL: {}".format(erro))
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi finalizada")
