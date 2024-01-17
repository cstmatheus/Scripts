import mysql.connector
from mysql.connector import Error

#INSERE REGISTRO NA BASE DE DADOS

print('cadastro produto')
id = input('ID? ')
nome = input('Nome? ')
valor = input('Valor? ')

dados = id + ',\'' + nome + '\',' + valor +')'

declaracao = """ insert into produto
(id, nome, valor) values ("""
sql = declaracao + dados
#print(sql)

try:
    con = mysql.connector.connect(host='localhost', database='project', user='root', password='123')
    inserir_produto = sql
    cursor = con.cursor()
    cursor.execute(inserir_produto)
    con.commit()
    print(cursor.rowcount,'registro inserido')
    cursor.close()
except Error as erro:
    print('Falha na insercao {}'.format(erro))

    