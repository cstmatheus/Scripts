"""
2	- Crie uma função “verificar_senha” no qual retorna true caso a senha inserida for correta e false caso o contrário.
Logo após elabore um “mini-sistema” de checar a senha inserida, onde o usuário tem 3 tentativas de senha e caso esse número
seja ultrapassado o programa é encerrado.
"""


def checaSenha(senha):
    padrao = 'manaus'
    if (senha == padrao):
        return True
    else:
        return False


# True e False SO FUNCIONA COM A PRIMEIRA LETRA MAIUSCULA


print('=/' * 20)
for i in range(3):
    senha = str(input('DIGITE A SENHA: '))
    # alt=checaSenha(senha) // USANDO VARIAVEL PARA ARMAZENAR O VALOR
    senha = senha.lower()

    # PASSANDO A FUNCAO DIRETO PARA A COMPARACAO
    if (checaSenha(senha) == True):
        print('CORRETO')
        break

    else:
        x = i
        x += 1
        print('ERRADO')
        print('=/' * 20)
        if (x == 3):
            print('USUARIO BLOQUEADO')
            print('=/' * 20)
print('SISTEMA DESATIVADO')

