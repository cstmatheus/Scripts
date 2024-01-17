"""
Usando a função do item anterior, elabore um programa que é inserido as respostas das provas de 3 alunos,
onde o gabarito da prova é “A-A-B-D-E-A-C-C-AD”, logo após é mostrado as notas que esses alunos obtiveram.
"""


def avaliaNota(resposta):
    gabarito = ['a', 'b', 'c']
    fail = 0
    acerto = 0

    for i in range(len(gabarito)):

        """COMPARA AS RESPOSTA (DEIXA ELAS EM MINUSCULO COMO DEFINIDO NO GABARITO)"""
        if (gabarito[i] == resposta[i].lower()):
            acerto += 1
        else:
            fail += 1

    """AVALIA APROVACAO"""
    if (acerto > 1):
        print('/=' * 30)
        print(f'APROVADO COM {acerto} ACERTOS')
        print('/=' * 30)

    else:
        print('/=' * 30)
        print(f'REPROVADO COM {fail} ERROS')
        print('/=' * 30)

alunos = []#VARIAVEL GLOBAL
def cadastraAluno(aluno):
    #alunos = []
    alunos.append(aluno)
    return alunos# print('nome cadastrado', alunos[0])
"""    if len(alunos) != 0:
        for i in range(alunos):
            print('ALUNO CADASTRADOS: ', i)
    else:
        print('NAO HA CADASTRO') 
"""



def listarAluno():
    for indice, nome in enumerate(alunos):
        print('ID: {}, NOME: {}'.format(indice, nome))



"""SE USAR RESPOSTA CHEIO, TEMOS QUE ZERAR PARA FAZER A ITERACAO"""
resposta = ['0', '0', '0']
print('=*'*30)
op = int(input('DIGITE UMA OPCAO:\n[1] CADASTRAR ALUNO\n[2] AVALIAR NOTA\n[3] LISTAR ALUNOS\n[0] FECHAR O SISTEMA\n'))

while (op != 0):
    if (op == 1):
        print('=*' * 30)
        nome = input('DIGITE O NOME DO ALUNO: ')
        cadastraAluno(nome)
        print('CADASTRADO COM SUCESSO')
        print('=*' * 30)

    elif (op == 2):
        print('/=' * 30)
        print('AVALIADOR DE NOTAS:')
        print('/=' * 30)

        """COLETA AS RESPOSTAS E ADICIONA A LISTA"""
        for i in range(3):
            print(f'QUESTAO: {i + 1}')
            resposta[i] = input('INFORME AS RESPOSTAS: ')
            # resposta.append(r)

        avaliaNota(resposta)
    elif (op == 3):
        print('=*'*30)
        listarAluno()
        print('=*' * 30)

    op = int(input('DIGITE UMA OPCAO:\n[1] CADASTRAR ALUNO\n[2] AVALIAR NOTA\n[3] LISTAR ALUNOS\n[0] FECHAR O SISTEMA\n'))
    # print('OP TA VALENDO: ', op)
print('SISTEMA FINALIZADO')
