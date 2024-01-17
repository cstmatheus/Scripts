m = 'TOTAL REFERIDO AO MES ATUAL'
print('\033[1;36m{:#^40}\033[m'.format(m))

sal = float(input('\nINFORME QUANTO GANHA POR HORA: \n'))
hora = int(input('\nHORAS TRABALHADAS: \n'))

sal = sal * hora

imposto = (sal * 11)/100
inss = (sal * 8)/100
sindicato = (sal * 5)/100
liquido = sal - (imposto + inss + sindicato)
print()
print('='*40)
print('\033[1;36m+ Salário Bruto : R$ {:.2f}\033[m\n\033[1;31m- IR (11%) : R$ {:.2f}\033[m\n\033[1;31m- INSS (8%) : R$ {:.2f}\033[m\n\033[1;31m- Sindicato ( 5%) : R$ {:.2f}\033[m\n\033[1;36m- Salário Liquido : R$ {:.2f}\033[m'.format(sal, imposto, inss, sindicato, liquido))
print('='*40)