m = 'CONVERSOR DE METRO PARA CENTIMETRO'
print('\033[1;32m{:-^50}\033[m'.format(m))

m = float(input('METROS ?'))

cen = m*100

m1 = 'CONVERSAO'
print('\n\033[1;32m{:-^20}\033[m'.format(m1))

print('\nQUANTIDADE EM CENTIMETRO \033[1;35m{:.2f}\033[m\n'.format(cen).replace('.' ,','))
print('\033[1;32m-\033[m'*20)