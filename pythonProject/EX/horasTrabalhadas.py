print('='*40)
m = 'CALCULO DE HORAS TRABALHADAS'
print('\033[1;35m{:^40}\033[m'.format(m))
print('='*40)
sal = float(input('SALARIO POR HORA?'))

hora = float(input('HORAS ?'))

s = sal*hora

print('='*40)
print('VOCE IRA RECEBER \033[1;35m{:.2f}\033[m'.format(s))
print('='*40)


