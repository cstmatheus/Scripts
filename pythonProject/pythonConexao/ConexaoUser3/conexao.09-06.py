import mysql.connector

id = input('id ?')
nome = input('NOME ?')
valor = input('VALOR')

dados = id + ',\'' + nome + '\',' + valor + ')'

declaracao = """insert into produto (id, nome, valor)values("""

sql = declaracao + dados



try:
    c = mysql.connector.connect(host='localhost', database='project', user = 'root', password='123')
    inserir = sql
    cursor = c.cursor()
    cursor.execute(inserir)
    c.commit()
    print(cursor.rowcount, 'INSERIDOS')
    cursor.close()
except mysql.connector.Error as erro:
    print('FALHA NO {}'.format(erro))