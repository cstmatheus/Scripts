from numpy import random

print('=='*30)

m='JOGO DADOS'
print('{:^60}'.format(m))

print('=='*30)

print('======= O GANHADOR E AQUELE QUE TIRAR O NUMERO MAIOR =======')
print('=='*30)
op = int(input('DIGITE QUALQUER NUMERO PARA INICIAR OU ZERO PARA SAIR: '))
while op != 0:
    x = random.randint(6)


    print('[{:^58}]'.format(x+1))
    print('=='*30)
    op = int(input('DIGITE QUALQUER NUMERO PARA INICIAR OU ZERO PARA SAIR: '))

print('SISTEMA FINALIZADO')