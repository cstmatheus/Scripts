m=('INFORME AS NOTAS')

print('\033[1;36m{:-^40}\033[m'.format(m))
#print('\033[1;36m{:-^40}\033[m'.format(m))


n1 = float(input('N1 ?\n'))
n2 = float(input('N2 ?\n'))
n3 = float(input('N3 ?\n'))
n4 = float(input('N4 ?\n'))

print('\033[1;36m-\033[m'*40)

media = (n1+n2+n3+n4)/4
if media >= 6:
    print('APROVADO COM \033[1;36m{}\033[m'.format(media))
else:
    print('REPROVADO COM \033[1;31m{}\033[m'.format(media))
print('\033[1;36m-\033[m'*40)