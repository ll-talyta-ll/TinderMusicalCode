#!/usr/bin/python3.9

import mysql.connector
    #criando conexão ao banco de dados
con = mysql.connector.connect(
    host='mysqlserver.ctxtwwh0ilx9.us-east-1.rds.amazonaws.com',
    user='admin',
    password='Brasilhexa2022',
    database='dbmysql',
    port='3306')
if con.is_connected():
    db_info = con.get_server_info()
    print("conectado ao servidor MySqL versão ", db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados", linha)

if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão ao MySQL foi encerrada")