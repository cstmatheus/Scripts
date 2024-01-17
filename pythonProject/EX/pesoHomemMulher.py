m = 'CALCULA PESO IDEAL HOMEM E MULHER'
print('\033[1;31m{:=^40}\033[m'.format(m))

a = int(input('(1) PARA HOMEM\n(2) PARA MULHER\n'))

altura = float(input('ALTURA ?\n'))

if a == 1:
    a = (72.7*altura)-58
    print('PESO IDEAL MASCULINO: \033[1;36m{:.2f}\033[m'.format(a).replace('.', ','))
else:
    a = (62.1*altura)-44.7
    print('PESO IDEL FEMININO: \033[1;31m{:.2f}\033[m'.format(a).replace('.', ','))