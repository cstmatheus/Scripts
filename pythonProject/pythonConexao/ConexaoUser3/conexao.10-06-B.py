import mysql.connector
from mysql.connector import Error


id = input('ID ?')
nome = input('NOME ?')
idade = input('IDADE ?')

dados = id + ',\'' + nome + '\',' + idade + ')'

declaracao = """insert into pessoa (id, nome, idade)values("""

sql = declaracao + dados

try:
    con = mysql.connector.connect(host='localhost', database='python', user='root', password='123')
    inserir = sql
    cursor = con.cursor()
    cursor.execute(inserir)
    con.commit()
    print(cursor.rowcount, 'INSERIDOS')
    cursor.close()
except Error as erro:
    print('FALHA NA INSERCAO {}'.format(erro))