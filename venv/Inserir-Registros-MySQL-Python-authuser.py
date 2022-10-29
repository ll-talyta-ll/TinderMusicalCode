import mysql.connector
from mysql.connector import Error
# Inserir registros em um banco de dados MySQL

try:
    con = mysql.connector.connect(
        host='mysqlserver.ctxtwwh0ilx9.us-east-1.rds.amazonaws.com',
        user='admin',
        password='Brasilhexa2022',
        database='dbmysql',
        port='3306')
    inserir_produtos = """INSERT INTO auth_user
                            (Name, User, Password, PasswordConf, Email, Age)
                          VALUES
                            ('Talyta', 'Taly', 'Brasil', 'Brasil', 'talyta1405gmailcom', 12)
                           """
                            #('Vitroia', 'TaylorSwift', 'TaylorSwift', 'vitoriagmailcom', 13)
                            #('Guilherme', 'TomRiddle', 'TomRiddle', 'guilhermerodriguesgmailcom', 12)
                            

    cursor = con.cursor()
    cursor.execute(inserir_produtos)
    con.commit()
    print(cursor.rowcount, "registros inseridos na tabela!")
    cursor.close()
except Error as erro:
    print("Falha ao inserir dados no MySql: {}".format(erro))
finally:
    if(con.is_connected()):
        con.close()
        print("Conexão ao MySql finalizada")
