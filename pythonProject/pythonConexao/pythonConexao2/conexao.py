import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host="localhost", database="project", user="root", password="123")

    inserir_produto = """ insert into produto
    (id, nome, valor) values
         (1, 'camera', 850.00), 
         (2, 'monitor', 630.00),
         (3, 'relogio', 575.00)
                    """
    cursor = con.cursor()
    cursor.execute(inserir_produto)
    con.commit()
    print(cursor.rowcount, 'registros inseridos na tabela')
    cursor.close()

except Error as erro:
    print('falha na insercao {}'.format(erro))
finally:
    if (con.is_connected()):
        con.close()
        print('CONEXAO FINALIZADA')


