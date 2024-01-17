m = 'AREA DO QUADRADO'
print('\033[1;35m{:=^40}\033[m'.format(m))

b = float(input('BASE ?\n'))

h = float(input('ALTURA ?\n'))

area = b*h

m = 'AREA CALCULADA'
print('\033[1;35m{:^40}\033[m'.format(m))
print('\nO VALOR E \033[1;33m{:.2f}\033[m'.format(area).replace('.', ','))