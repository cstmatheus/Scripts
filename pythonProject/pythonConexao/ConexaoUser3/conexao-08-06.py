import mysql.connector

from mysql.connector import Error

id = input('id ?')
nome = input('nome ?')
idade = input('Idade')

dados = id + ',\'' + nome + '\',' + idade + ')'

declaracao = """insert into pessoa(
id, nome, idade)values("""

sql = declaracao + dados

try:
    con = mysql.connector.connect(host='localhost', database='python', user='root', password='123')
    insereDados = sql
    cursor = con.cursor()
    cursor.execute(insereDados)
    con.commit()
    print(cursor.rowcount, 'Registro inserido')
    cursor.close()
except Error as erro:
    print('FALHA NA INSERCAO'.format(erro))