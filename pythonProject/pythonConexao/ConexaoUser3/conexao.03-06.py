import mysql.connector

from mysql.connector import Error

print('CADASTRO PRODUTO')

id = input('ID?')
nome = input('NOME?')
valor = input('Valor? ')

# inserindo string entre aspas usando caractere de escape

dados = id + ',\'' + nome + '\',' + valor + ')'

# inserindo dados na base de dados(TABELA)

declaracao = """ insert into produto
(id, nome, valor) values("""

# criando variavel com cocatenacao de declaracao + dados

sql = declaracao + dados

try:
    # CRIANDO CONEXAO COM BANCO
    con = mysql.connector.connect(host='localhost', database='project', user='root', password='123')

    inserir_produto = sql

    cursor = con.cursor()

    cursor.execute(inserir_produto)

    # valida o con

    con.commit()

    # conta numero de registros inseridos

    print(cursor.rowcount, 'registro inserido')

    # fecha o cursor

    cursor.close()
except Error as erro:
    print('falha na insercao'.format(erro))