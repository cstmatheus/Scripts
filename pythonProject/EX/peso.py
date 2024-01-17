m = 'CALCULA PESO IDEAL'
print('\033[1;35m{:^40}\033[m'.format(m))
print('='*40)

a = float(input('ALTURA ?\n'))

c = (72.7*a)-58
print('='*40)
print('PESO IDEAL: \033[1;35m{:.2f}\033[m'.format(c))
print('='*40)