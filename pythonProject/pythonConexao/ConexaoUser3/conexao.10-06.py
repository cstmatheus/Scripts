import mysql.connector

id = input('ID ?')
nome = input('Nomes ?')
valor = input('valor ?')

dados = id + ',\'' + nome + '\',' + valor + ')'

declaracao = """insert into produto(id, nome, valor)values("""

sql = declaracao + dados

try:
    con = mysql.connector.connect(host='localhost', database='project', user='root', password='123')
    #inserir = sql
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    print(cursor.rowcount, 'REGISTRO INSERIDO')
    cursor.close()
except mysql.connector.Error as erro:
    print('FALHA {}'.format(erro))