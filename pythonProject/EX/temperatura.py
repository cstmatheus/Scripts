print('\033[1;32m=\033[m'*40)
m = 'CONVERSOR PARA CELCIUS'
print('\033[1;32m{:^40}\033[m'.format(m))
print('\033[1;32m=\033[m'*40)
#print('|                                      |\n'*5)
f = float(input('Fahrenheit ?'))

c = (f-32)/1.8

print('='*40)
print('Celsius = \033[1;35m{}\033[m'.format(c))
print('='*40)