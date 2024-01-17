x = 'João Papo-de-Pescador'
print('\033[1;31m{:#^40}\033[m'.format(x))
print('')
p = float(input('\033[1;36mINFORME O PESO:\033[m'))

if p > 0 and p<=50:
    print('\033[1;36mPARABENS ESTA DENTRO DO REGULAMENTO\033[m')

else:
    v = p - 50
    v = v*4
    print('\033[1;31mESTA ACIMA DO REGULAMENTO \nVOCE PAGARA MULTA NO VALOR DE {}\033[m'.format(v))