
frutas = []
id = 0

op = 2
print('##########################################################################################')
print('                                         SYS                                              ')
print('##########################################################################################')
# a = int(input('DIGITE [0] PARA SAIR OU QUALQUER OUTRO NUMERO PARA CONTINUAR: '))


while (op != 0):

    print('(1) PARA CADASTRAR [INCLUIR NO FINAL]')
    print('(2) PARA DELETAR PELO ID')
    print('(3) PARA DELETAR PELO NOME')
    print('(4) PARA ALTERAR NOME')
    print('(9) PARA LISTAR')
    print('(0) PARA SAIR')
    op = int(input('DIGITE SUA OPCAO: '))
    print('##########################################################################################')

    if (op==1):
        n = str(input('DIGITE O NOME: '))
        frutas.append(n)

    if(op == 2):
        n = int(input('DIGITE O ID: '))
        frutas.pop(n)

    if(op==3):
        n = str(input('DIGITE O NOME PARA DELETAR: '))
        frutas.remove(n)

    if(op==4):
        id = int(input('DIGITE O ID DA FRUTA: '))
        n = str(input('DIGITE O NOVO NOME: '))
        frutas[id]= n

    if(op==9):
        print('FRUTAS CADASTRADAS')
        for indice, nome in enumerate(frutas):
            print('ID:[{}], NOME: {}'.format(indice, nome))
        """print('FRUTAS CADASTRADAS')
        for a in frutas:
            print('ID:[{}]{}'.format(id, a))
            id = id +1"""
    print('##########################################################################################')

    # a = int(input('DIGITE [0] PARA SAIR OU QUALQUER OUTRO NUMERO PARA CONTINUAR: '))

print('SISTEMA FINALIZADO')
