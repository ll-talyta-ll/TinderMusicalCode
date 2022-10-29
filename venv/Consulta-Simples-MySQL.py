import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(
        host='mysqlserver.ctxtwwh0ilx9.us-east-1.rds.amazonaws.com',
        user='admin',
        password='Brasilhexa2022',
        database='dbmysql',
        port='3306')
    consulta_sql = "select * from auth_user"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount)
    print("\nMostrando os usuários cadastrados")
    for linha in linhas:
        print("Name:", linha[0])
        print("User:", linha[1])
        print("Password:", linha[2])
        print("PasswordConf:", linha[3])
        print("Email:", linha[4])
        print("Age:", linha[5],"\n")
except Error as e:
    print ("Erro ao acessar tabela MySQL", e)
finally:
    if(con.is_connected()):
        con.close()
        cursor.close()
        print("Conexão ao MySql encerrada")
