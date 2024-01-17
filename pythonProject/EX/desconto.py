n = 'CONTANDO DESCONTO'
print('\033[1;31m{:-^40}\033[m'.format(n))

valor = float(input('VALOR ?\n'))

des = int(input('DESCONTO ?\n'))

m = 'AJUSTE'

print('{:=^40}'.format(m))

print('valor informado \033[1;36m{}\033[m\n'
      'desconto \033[1;36m{}\033[m\n'
      'valor com desconto \033[1;32m{}\033[m'.format(valor, des, valor-(valor*des)/100).replace('.', ','))

print('-'*40)