m = 'AREA DO CIRCULO'
print('\033[1;32m{:^40}\033[m'.format(m))
print('-'*40)

r = float(input('RAIO ?\n'))

a = 3.14*(pow(r, 2))
print('-'*40)
print('A AREA DO CIRCULO \033[1;32m{:.2f}\033[m'.format(a))
print('-'*40)